#!/usr/bin/env python3
"""
Convert Clerk docs from MDX to clean Markdown.

Reads from .clerk-docs-source/docs/ and writes to docs/.
Handles:
  - YAML frontmatter → title heading + description
  - <Include src="..." /> → inline partial content (recursive)
  - <Steps> / <Tab> / <Tabs> / <CodeBlockTabs> → plain markdown
  - <Properties> → definition lists
  - <If> / <Show> / <SignedIn> / <SignedOut> → keep content, strip tags
  - <TutorialHero> / <Cards> / <Typedoc> / <Icon> → remove
  - Extended code block syntax {{ filename: '...' }} → comment header
  - JSX comments {/* ... */} → strip
  - Remaining JSX tags → strip tags, keep inner content
"""

import os
import re
import sys
import shutil
from pathlib import Path

SOURCE_DIR = Path(__file__).parent / ".clerk-docs-source" / "docs"
OUTPUT_DIR = Path(__file__).parent / "docs"
PARTIALS_DIR = SOURCE_DIR / "_partials"

# Directories to skip entirely (they're source material, not docs)
SKIP_DIRS = {"_partials", "_tooltips"}

# Track include depth to prevent infinite recursion
MAX_INCLUDE_DEPTH = 10

# ── Partial resolution ──────────────────────────────────────────────

def resolve_partial(src_attr: str, depth: int = 0) -> str:
    """Resolve an <Include src="..." /> to its file content."""
    if depth > MAX_INCLUDE_DEPTH:
        return f"<!-- Include depth exceeded for {src_attr} -->\n"

    # src is relative to the docs root, e.g. "_partials/backend/usage"
    # Try with .mdx extension first, then without
    candidates = [
        SOURCE_DIR / f"{src_attr}.mdx",
        SOURCE_DIR / f"{src_attr}.md",
        SOURCE_DIR / src_attr,
    ]

    for candidate in candidates:
        if candidate.is_file():
            content = candidate.read_text(encoding="utf-8", errors="ignore")
            # Recursively resolve includes in the partial
            content = resolve_includes(content, depth + 1)
            # Strip frontmatter from partials (they shouldn't have titles)
            content = strip_frontmatter(content)
            return content

    return f"<!-- Partial not found: {src_attr} -->\n"


def resolve_includes(content: str, depth: int = 0) -> str:
    """Replace all <Include src="..." /> tags with their content."""
    # Match <Include src="..." /> with optional whitespace
    pattern = r'<Include\s+src=["\']([^"\']+)["\']\s*/>'
    
    def replacer(match):
        src = match.group(1)
        return resolve_partial(src, depth)
    
    return re.sub(pattern, replacer, content)


# ── Frontmatter handling ────────────────────────────────────────────

def extract_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and return (metadata, remaining_content)."""
    if not content.startswith("---"):
        return {}, content
    
    end = content.find("---", 3)
    if end == -1:
        return {}, content
    
    fm_text = content[3:end].strip()
    remaining = content[end + 3:].lstrip("\n")
    
    metadata = {}
    for line in fm_text.split("\n"):
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip("'\"")
            metadata[key] = value
    
    return metadata, remaining


def strip_frontmatter(content: str) -> str:
    """Remove frontmatter without extracting it."""
    if not content.startswith("---"):
        return content
    end = content.find("---", 3)
    if end == -1:
        return content
    return content[end + 3:].lstrip("\n")


# ── JSX component stripping ────────────────────────────────────────

def strip_jsx_comments(content: str) -> str:
    """Remove {/* ... */} JSX comments."""
    return re.sub(r'\{/\*.*?\*/\}', '', content, flags=re.DOTALL)


def convert_properties(content: str) -> str:
    """Convert <Properties> blocks to markdown definition lists.
    
    Format in MDX:
    <Properties>
      - `name`
      - `type`
      
      Description text.
    </Properties>
    
    Output:
    - **`name`** `type`
    
      Description text.
    """
    def replace_properties(match):
        inner = match.group(1)
        # Each property is a group of list items followed by description
        # Parse the items: lines starting with "  - " are property attributes
        lines = inner.split("\n")
        result = []
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Start of a property: first list item is the name
            if line.startswith("- `"):
                name = line[2:].strip()  # e.g. `paramName`
                i += 1
                
                # Next list item(s) might be the type
                type_str = ""
                while i < len(lines) and lines[i].strip().startswith("- "):
                    type_item = lines[i].strip()[2:].strip()
                    if type_str:
                        type_str += " "
                    type_str += type_item
                    i += 1
                
                # Build the definition header
                if type_str:
                    result.append(f"- **{name}** {type_str}")
                else:
                    result.append(f"- **{name}**")
                
                # Collect description lines until next property or end
                desc_lines = []
                while i < len(lines):
                    curr = lines[i]
                    curr_stripped = curr.strip()
                    # Next property starts with "- `"
                    if curr_stripped.startswith("- `"):
                        break
                    desc_lines.append(curr)
                    i += 1
                
                # Add description indented
                desc = "\n".join(desc_lines).strip()
                if desc:
                    # Indent description under the property
                    result.append("")
                    for dl in desc.split("\n"):
                        result.append(f"  {dl}" if dl.strip() else "")
                result.append("")
            else:
                i += 1
        
        return "\n".join(result)
    
    return re.sub(
        r'<Properties>(.*?)</Properties>',
        replace_properties,
        content,
        flags=re.DOTALL
    )


def convert_tabs(content: str) -> str:
    """Convert <Tabs> and <Tab> to markdown sections.
    
    <Tabs items={['Next.js', 'Express']}>
      <Tab>
        content1
      </Tab>
      <Tab>
        content2
      </Tab>
    </Tabs>
    
    →
    
    #### Next.js
    content1
    
    #### Express
    content2
    """
    def replace_tabs(match):
        full = match.group(0)
        
        # Extract tab names from items attribute
        items_match = re.search(r"items=\{?\[([^\]]+)\]\}?", full)
        tab_names = []
        if items_match:
            items_str = items_match.group(1)
            # Parse quoted strings
            tab_names = re.findall(r"['\"]([^'\"]+)['\"]", items_str)
        
        # Split content by <Tab> tags
        # Remove the outer <Tabs ...> and </Tabs>
        inner = re.sub(r'<Tabs[^>]*>', '', full, count=1)
        inner = re.sub(r'</Tabs>\s*$', '', inner)
        
        # Split by <Tab> / </Tab>
        tab_contents = re.split(r'<Tab[^>]*>|</Tab>', inner)
        # Filter out empty/whitespace-only segments
        tab_contents = [tc for tc in tab_contents if tc.strip()]
        
        result_parts = []
        for idx, tc in enumerate(tab_contents):
            name = tab_names[idx] if idx < len(tab_names) else f"Tab {idx + 1}"
            result_parts.append(f"\n#### {name}\n")
            # Dedent content
            result_parts.append(dedent_content(tc))
        
        return "\n".join(result_parts)
    
    # Match <Tabs ...>...</Tabs> (non-greedy, but Tabs can be nested so be careful)
    # Use a simpler approach: match from <Tabs to </Tabs>
    content = re.sub(
        r'<Tabs\s[^>]*>.*?</Tabs>',
        replace_tabs,
        content,
        flags=re.DOTALL
    )
    
    return content


def convert_codeblock_tabs(content: str) -> str:
    """Convert <CodeBlockTabs> to sequential code blocks.
    
    <CodeBlockTabs options={["npm", "yarn", "pnpm"]}>
      ```sh
      npm install @clerk/nextjs
      ```
      ```sh
      yarn add @clerk/nextjs
      ```
      ```sh
      pnpm add @clerk/nextjs
      ```
    </CodeBlockTabs>
    """
    def replace_cbt(match):
        full = match.group(0)
        
        # Extract option names
        options_match = re.search(r'options=\{?\[([^\]]+)\]\}?', full)
        option_names = []
        if options_match:
            option_names = re.findall(r"['\"]([^'\"]+)['\"]", options_match.group(1))
        
        # Remove the wrapper tags
        inner = re.sub(r'<CodeBlockTabs[^>]*>', '', full, count=1)
        inner = re.sub(r'</CodeBlockTabs>\s*$', '', inner)
        
        # Find all code blocks
        blocks = list(re.finditer(r'```(\w*)\n(.*?)```', inner, re.DOTALL))
        
        result_parts = []
        for idx, block in enumerate(blocks):
            lang = block.group(1)
            code = block.group(2)
            name = option_names[idx] if idx < len(option_names) else ""
            if name:
                result_parts.append(f"\n**{name}:**\n")
            result_parts.append(f"```{lang}\n{code}```\n")
        
        if result_parts:
            return "\n".join(result_parts)
        return inner  # fallback
    
    content = re.sub(
        r'<CodeBlockTabs\s[^>]*>.*?</CodeBlockTabs>',
        replace_cbt,
        content,
        flags=re.DOTALL
    )
    
    return content


def convert_accordion(content: str) -> str:
    """Convert <Accordion> / <AccordionPanel> to markdown details.
    
    <AccordionPanel title="Question?">
      Answer content
    </AccordionPanel>
    
    → **Question?**
    
      Answer content
    """
    def replace_panel(match):
        title_match = re.search(r'title=["\']([^"\']*)["\']', match.group(0))
        title = title_match.group(1) if title_match else "Details"
        inner = match.group(1).strip()
        return f"\n**{title}**\n\n{inner}\n"
    
    content = re.sub(
        r'<AccordionPanel[^>]*>(.*?)</AccordionPanel>',
        replace_panel,
        content,
        flags=re.DOTALL
    )
    # Remove <Accordion> wrappers
    content = re.sub(r'</?Accordion>', '', content)
    
    return content


def convert_code_blocks(content: str) -> str:
    """Normalize extended code block syntax.
    
    ```tsx {{ filename: 'app/page.tsx', mark: [2, [29, 44]] }}
    →
    ```tsx
    // Filename: app/page.tsx
    """
    def replace_code_header(match):
        lang = match.group(1) or ""
        attrs_str = match.group(2)
        
        # Extract filename if present
        filename_match = re.search(r"filename:\s*['\"]([^'\"]+)['\"]", attrs_str)
        filename = filename_match.group(1) if filename_match else None
        
        result = f"```{lang}\n"
        if filename:
            # Add filename as a comment in the appropriate style
            comment_styles = {
                "tsx": "//", "ts": "//", "jsx": "//", "js": "//",
                "go": "//", "java": "//", "swift": "//", "kotlin": "//",
                "rb": "#", "py": "#", "python": "#", "ruby": "#",
                "sh": "#", "bash": "#", "zsh": "#", "shell": "#",
                "css": "/*", "html": "<!--",
                "php": "//", "csharp": "//", "c": "//", "cpp": "//",
                "yaml": "#", "yml": "#", "toml": "#",
                "sql": "--", "astro": "---",
            }
            comment = comment_styles.get(lang.lower(), "//")
            if comment == "/*":
                result += f"/* Filename: {filename} */\n"
            elif comment == "<!--":
                result += f"<!-- Filename: {filename} -->\n"
            elif comment == "---":
                result += f"// Filename: {filename}\n"
            else:
                result += f"{comment} Filename: {filename}\n"
        
        return result
    
    # Match code block openings with {{ ... }}
    content = re.sub(
        r'```(\w*)\s*\{\{([^}]*(?:\{[^}]*\}[^}]*)*)\}\}',
        replace_code_header,
        content
    )
    
    return content


def convert_callouts(content: str) -> str:
    """Convert <Callout> components to GitHub-style alerts.
    
    <Callout type="warning">
      Content
    </Callout>
    
    → > [!WARNING]
      > Content
    """
    def replace_callout(match):
        attrs = match.group(1)
        inner = match.group(2).strip()
        
        type_match = re.search(r'type=["\'](\w+)["\']', attrs)
        callout_type = type_match.group(1).upper() if type_match else "NOTE"
        
        # Map callout types
        type_map = {
            "WARNING": "WARNING",
            "DANGER": "CAUTION",
            "ERROR": "CAUTION", 
            "INFO": "NOTE",
            "SUCCESS": "TIP",
            "TIP": "TIP",
            "NOTE": "NOTE",
            "CAUTION": "CAUTION",
            "IMPORTANT": "IMPORTANT",
        }
        alert_type = type_map.get(callout_type, "NOTE")
        
        lines = inner.split("\n")
        quoted = "\n".join(f"> {l}" if l.strip() else ">" for l in lines)
        return f"> [!{alert_type}]\n{quoted}\n"
    
    content = re.sub(
        r'<Callout([^>]*)>(.*?)</Callout>',
        replace_callout,
        content,
        flags=re.DOTALL
    )
    
    return content


def strip_self_closing_components(content: str) -> str:
    """Remove self-closing JSX components that don't render text.
    
    <TutorialHero ... /> → removed
    <Icon ... /> → removed
    <Typedoc ... /> → removed (generated content, not in source)
    """
    # Remove specific self-closing components
    components_to_remove = [
        "TutorialHero", "Icon", "Typedoc", "SignedIn", "SignedOut",
        "Images", "Image",
    ]
    for comp in components_to_remove:
        content = re.sub(rf'<{comp}\s[^>]*/>\s*\n?', '', content)
        content = re.sub(rf'<{comp}/>\s*\n?', '', content)
    
    return content


def strip_wrapper_tags(content: str) -> str:
    """Remove wrapper-only JSX tags, keeping their inner content.
    
    <Steps> ... </Steps> → ...
    <If sdk="nextjs"> ... </If> → ...
    <Show when="signed-in"> ... </Show> → ...
    <SignedIn> ... </SignedIn> → ...
    """
    # Tags that are just wrappers — strip open and close, keep content
    wrapper_tags = [
        "Steps", "If", "Show", "SignedIn", "SignedOut",
        "Cards", "Card",
    ]
    for tag in wrapper_tags:
        # Opening tags with attributes
        content = re.sub(rf'<{tag}\s[^>]*>', '', content)
        # Opening tags without attributes 
        content = re.sub(rf'<{tag}>', '', content)
        # Closing tags
        content = re.sub(rf'</{tag}>', '', content)
    
    return content


def strip_remaining_jsx(content: str) -> str:
    """Strip any remaining JSX-like tags that aren't standard HTML.
    
    Only strips tags that start with uppercase (React components).
    Keeps standard HTML tags like <div>, <p>, <code>, etc.
    """
    # Remove self-closing uppercase components
    content = re.sub(r'<[A-Z]\w+\s[^>]*/>\s*\n?', '', content)
    content = re.sub(r'<[A-Z]\w+/>\s*\n?', '', content)
    
    # Remove opening/closing uppercase component tags (keep content between)
    content = re.sub(r'<[A-Z]\w+[^>]*>', '', content)
    content = re.sub(r'</[A-Z]\w+>', '', content)
    
    return content


def convert_links(content: str) -> str:
    """Convert internal doc links.
    
    [text](/docs/reference/...) → [text](./reference/...)
    [text](!tooltip-id) → text
    [text](/docs/...) → [text](./...)
    """
    # Remove tooltip links [text](!tooltip-id)
    content = re.sub(r'\[([^\]]+)\]\(![^\)]+\)', r'\1', content)
    
    # Convert absolute /docs/ links to relative
    content = re.sub(r'\]\(/docs/', '](/', content)
    
    # Strip {{ target: '_blank' }} from links
    content = re.sub(r'\{\{\s*target:\s*["\']_blank["\']\s*\}\}', '', content)
    
    return content


def strip_images_and_svgs(content: str) -> str:
    """Remove standard markdown images, HTML images, and raw SVGs."""
    # Remove markdown images: ![alt](url) or ![alt](url){{metadata}}
    content = re.sub(r'!\[.*?\]\(.*?\)(?:\{\{.*?\}\})?', '', content)
    
    # Remove HTML img tags
    content = re.sub(r'<img[^>]*>', '', content)
    
    # Remove raw SVGs (could be inside {})
    content = re.sub(r'\{?<svg.*?</svg>\}?', '', content, flags=re.DOTALL)
    
    return content


def dedent_content(text: str) -> str:
    """Remove common leading whitespace from text block."""
    lines = text.split("\n")
    # Find minimum indentation (ignoring empty lines)
    non_empty = [l for l in lines if l.strip()]
    if not non_empty:
        return text
    
    min_indent = min(len(l) - len(l.lstrip()) for l in non_empty)
    if min_indent == 0:
        return text
    
    return "\n".join(l[min_indent:] if len(l) >= min_indent else l for l in lines)


def clean_excessive_blank_lines(content: str) -> str:
    """Collapse 3+ consecutive blank lines into 2."""
    return re.sub(r'\n{4,}', '\n\n\n', content)


# ── Main conversion pipeline ───────────────────────────────────────

def convert_mdx_to_md(content: str, filepath: Path) -> str:
    """Full conversion pipeline for a single MDX file."""
    
    # 1. Extract frontmatter
    metadata, content = extract_frontmatter(content)
    
    # 2. Resolve <Include> partials
    content = resolve_includes(content)
    
    # 3. Strip JSX comments
    content = strip_jsx_comments(content)
    
    # 4. Convert structured components
    content = convert_code_blocks(content)
    content = convert_properties(content)
    content = convert_callouts(content)
    content = convert_codeblock_tabs(content)
    content = convert_tabs(content)
    content = convert_accordion(content)
    
    # 5. Strip self-closing and wrapper components
    content = strip_self_closing_components(content)
    content = strip_wrapper_tags(content)
    
    # 6. Strip remaining JSX
    content = strip_remaining_jsx(content)
    
    # 7. Convert links
    content = convert_links(content)
    
    # 8. Strip images and svgs
    content = strip_images_and_svgs(content)
    
    # 9. Clean up
    content = clean_excessive_blank_lines(content)
    content = content.strip() + "\n"
    
    # 10. Add title from frontmatter
    header_parts = []
    title = metadata.get("title", "")
    if title:
        # Remove backticks from title for heading (they're common in Clerk docs)
        clean_title = title.strip("`")
        header_parts.append(f"# {clean_title}\n")
    
    description = metadata.get("description", "")
    if description:
        header_parts.append(f"\n> {description}\n")
    
    if header_parts:
        content = "\n".join(header_parts) + "\n" + content
    
    return content


def process_directory():
    """Walk source docs and convert all MDX files."""
    if not SOURCE_DIR.exists():
        print(f"Error: Source directory {SOURCE_DIR} does not exist.")
        print("Please clone clerk-docs first:")
        print("  git clone --depth 1 https://github.com/clerk/clerk-docs.git .clerk-docs-source")
        sys.exit(1)
    
    # Clean output directory
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    
    count = 0
    errors = 0
    skipped = 0
    
    for root, dirs, files in os.walk(SOURCE_DIR):
        root_path = Path(root)
        
        # Skip special directories
        rel_root = root_path.relative_to(SOURCE_DIR)
        if any(part in SKIP_DIRS for part in rel_root.parts):
            continue
        
        # Skip non-doc files
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        
        for filename in sorted(files):
            if not filename.endswith(".mdx"):
                # Copy non-MDX files (like manifest.json) as-is
                if filename.endswith((".json", ".md")):
                    src = root_path / filename
                    rel = src.relative_to(SOURCE_DIR)
                    dst = OUTPUT_DIR / rel
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
                continue
            
            src_file = root_path / filename
            rel_path = src_file.relative_to(SOURCE_DIR)
            
            # Change extension to .md
            dst_file = OUTPUT_DIR / rel_path.with_suffix(".md")
            dst_file.parent.mkdir(parents=True, exist_ok=True)
            
            try:
                content = src_file.read_text(encoding="utf-8", errors="ignore")
                converted = convert_mdx_to_md(content, src_file)
                dst_file.write_text(converted, encoding="utf-8")
                count += 1
            except Exception as e:
                print(f"  ERROR: {rel_path}: {e}")
                errors += 1
    
    print(f"\nConversion complete!")
    print(f"  Converted: {count} files")
    print(f"  Errors:    {errors} files")
    print(f"  Output:    {OUTPUT_DIR}")


if __name__ == "__main__":
    process_directory()
