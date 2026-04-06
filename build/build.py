#!/usr/bin/env python3
"""Resume builder: resume.yaml -> Jinja2 -> HTML -> WeasyPrint -> PDF."""

import os
import platform
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

# macOS WeasyPrint library path workaround
if platform.system() == "Darwin":
    brew_lib = "/opt/homebrew/lib"
    if os.path.isdir(brew_lib):
        os.environ.setdefault("DYLD_FALLBACK_LIBRARY_PATH", brew_lib)

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
OUTPUT_DIR = SCRIPT_DIR / "output"
CSS_PATH = SCRIPT_DIR / "css" / "resume.css"
TEMPLATE_DIR = SCRIPT_DIR / "templates"
ICONS_DIR = PROJECT_ROOT / "icons"

ICON_MAP = {
    "email": "mail.svg",
    "linkedin": "linkedin.svg",
    "location": "location_on.svg",
    "web": "web.svg",
    "github": "github.svg",
    "medium": "medium.svg",
}


def load_resume_data() -> dict:
    """Load resume.yaml."""
    with open(SCRIPT_DIR / "resume.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_icons() -> dict:
    """Load SVG icons from icons/ directory."""
    icons = {}
    for key, filename in ICON_MAP.items():
        path = ICONS_DIR / filename
        if path.exists():
            icons[key] = path.read_text(encoding="utf-8").strip()
    return icons


def render_html(data: dict) -> str:
    """Render resume data through Jinja2 template."""
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=False,
    )
    template = env.get_template("resume.html.j2")
    icons = load_icons()
    return template.render(
        resume=data,
        icons=icons,
        css_path=CSS_PATH.resolve().as_uri(),
    )


def generate_pdf(html_path: Path, pdf_path: Path):
    """Convert HTML to PDF using WeasyPrint."""
    from weasyprint import HTML

    HTML(filename=str(html_path)).write_pdf(str(pdf_path))


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("1/3  Loading resume data...")
    data = load_resume_data()

    print("2/3  Rendering HTML...")
    html = render_html(data)
    html_path = OUTPUT_DIR / "resume.html"
    html_path.write_text(html, encoding="utf-8")

    print("3/3  Generating PDF...")
    pdf_path = OUTPUT_DIR / "resume.pdf"
    generate_pdf(html_path, pdf_path)

    print(f"\nDone -> {pdf_path}")


if __name__ == "__main__":
    main()
