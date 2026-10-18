"""
Extract design system and screen HTML from UI_Document.docx.
Usage: python design/extract_ui_doc.py design/UI_Document.docx design/extracted
Falls back to python-docx if pandoc is not available.
"""
import sys
import os
import re
import shutil
import subprocess
from pathlib import Path

def try_pandoc(docx_path: str, out_dir: str) -> bool:
    """Try to convert using pandoc, return True if successful."""
    pandoc = shutil.which("pandoc")
    if not pandoc:
        return False
    md_path = os.path.join(out_dir, "raw.md")
    media_dir = os.path.join(out_dir, "images")
    os.makedirs(media_dir, exist_ok=True)
    result = subprocess.run(
        [pandoc, docx_path, "-t", "markdown", "--extract-media", media_dir, "-o", md_path],
        capture_output=True, text=True
    )
    return result.returncode == 0 and os.path.exists(md_path)


def extract_with_docx(docx_path: str, out_dir: str):
    """Extract content using python-docx."""
    try:
        from docx import Document
        from docx.oxml.ns import qn
        import zipfile
    except ImportError:
        print("Installing python-docx...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx"])
        from docx import Document
        from docx.oxml.ns import qn
        import zipfile

    images_dir = os.path.join(out_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    # Extract images from docx zip
    with zipfile.ZipFile(docx_path, 'r') as z:
        for name in z.namelist():
            if name.startswith("word/media/"):
                img_name = os.path.basename(name)
                z.extract(name, out_dir)
                src = os.path.join(out_dir, name)
                dst = os.path.join(images_dir, img_name)
                if not os.path.exists(dst):
                    shutil.move(src, dst)

    doc = Document(docx_path)
    lines = []
    in_code = False
    code_buf = []

    for para in doc.paragraphs:
        style = para.style.name if para.style else ""
        text = para.text.strip()

        # Detect code / preformatted blocks
        if "Code" in style or style in ("Preformatted Text", "HTML"):
            if not in_code:
                code_buf = []
                in_code = True
            code_buf.append(para.text)
            continue
        else:
            if in_code:
                lines.append("```html")
                lines.extend(code_buf)
                lines.append("```")
                in_code = False
                code_buf = []

        if not text:
            lines.append("")
            continue

        if "Heading 1" in style:
            lines.append(f"# {text}")
        elif "Heading 2" in style:
            lines.append(f"## {text}")
        elif "Heading 3" in style:
            lines.append(f"### {text}")
        elif "Heading 4" in style:
            lines.append(f"#### {text}")
        elif style in ("List Bullet", "List Paragraph"):
            lines.append(f"- {text}")
        else:
            lines.append(text)

    if in_code:
        lines.append("```html")
        lines.extend(code_buf)
        lines.append("```")

    # Also grab tables
    for table in doc.tables:
        header = [cell.text.strip() for cell in table.rows[0].cells]
        lines.append("")
        lines.append("| " + " | ".join(header) + " |")
        lines.append("| " + " | ".join(["---"] * len(header)) + " |")
        for row in table.rows[1:]:
            cells = [cell.text.strip() for cell in row.cells]
            lines.append("| " + " | ".join(cells) + " |")
        lines.append("")

    return "\n".join(lines)


def split_screens(content: str, screens_dir: str):
    """Split markdown into individual screen files based on headings."""
    os.makedirs(screens_dir, exist_ok=True)

    # Find screen sections - look for ## Screen or ## <number>. patterns
    screen_pattern = re.compile(
        r'^(#{1,3})\s+(Screen\s+\d+|(?:S-\d+)|(?:\d+[\.\)]\s+\w))',
        re.MULTILINE | re.IGNORECASE
    )

    sections = []
    for m in screen_pattern.finditer(content):
        sections.append((m.start(), m.group(0).strip()))

    if not sections:
        # Try splitting on HTML code blocks as individual screens
        blocks = re.split(r'(```html)', content)
        # Just save whole content as single screen
        with open(os.path.join(screens_dir, "screen_01.html"), "w", encoding="utf-8") as f:
            f.write(content)
        return

    for i, (start, title) in enumerate(sections):
        end = sections[i + 1][0] if i + 1 < len(sections) else len(content)
        chunk = content[start:end].strip()
        slug = re.sub(r'[^a-z0-9]+', '_', title.lower()).strip('_')
        fname = f"screen_{i+1:02d}_{slug[:40]}.md"
        with open(os.path.join(screens_dir, fname), "w", encoding="utf-8") as f:
            f.write(chunk)


def extract_html_blocks(content: str, screens_dir: str):
    """Extract HTML code blocks from raw content and save as screen files."""
    os.makedirs(screens_dir, exist_ok=True)
    # Match ```html ... ``` blocks
    pattern = re.compile(r'```(?:html|HTML)(.*?)```', re.DOTALL)
    matches = list(pattern.finditer(content))

    if not matches:
        # Try without language specifier
        pattern2 = re.compile(r'```(<!DOCTYPE.*?)```', re.DOTALL)
        matches = list(pattern2.finditer(content))

    if matches:
        for i, m in enumerate(matches):
            html = m.group(1).strip()
            fname = os.path.join(screens_dir, f"screen_{i+1:02d}.html")
            with open(fname, "w", encoding="utf-8") as f:
                f.write(html)
        print(f"  Extracted {len(matches)} HTML screen blocks.")
    else:
        print("  No HTML blocks found; saving raw content.")
        with open(os.path.join(screens_dir, "screen_01.md"), "w", encoding="utf-8") as f:
            f.write(content)


def build_design_md(raw_content: str, out_dir: str):
    """Save the full extracted content as DESIGN.md."""
    design_path = os.path.join(out_dir, "DESIGN.md")
    with open(design_path, "w", encoding="utf-8") as f:
        f.write(raw_content)
    print(f"  Saved DESIGN.md ({len(raw_content)} chars)")


def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_ui_doc.py <docx_path> <out_dir>")
        sys.exit(1)

    docx_path = sys.argv[1]
    out_dir = sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)
    screens_dir = os.path.join(out_dir, "screens")

    print(f"Extracting: {docx_path} -> {out_dir}")

    # Try pandoc first
    raw_md_path = os.path.join(out_dir, "raw.md")
    pandoc_ok = try_pandoc(docx_path, out_dir)

    if pandoc_ok:
        print("  Using pandoc for extraction.")
        with open(raw_md_path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        print("  Pandoc not available; using python-docx.")
        content = extract_with_docx(docx_path, out_dir)
        with open(raw_md_path, "w", encoding="utf-8") as f:
            f.write(content)

    build_design_md(content, out_dir)
    extract_html_blocks(content, screens_dir)

    # Count output
    screen_files = list(Path(screens_dir).glob("*"))
    image_files = list(Path(os.path.join(out_dir, "images")).glob("*")) if os.path.exists(os.path.join(out_dir, "images")) else []
    print(f"  Screen files: {len(screen_files)}")
    print(f"  Images: {len(image_files)}")
    print("Done.")


if __name__ == "__main__":
    main()
