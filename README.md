# ATS-Killer Resume Builder

A resume builder that outputs clean, ATS-friendly PDFs from a single YAML file. Built with Python, Jinja2 templates, CSS styling, and WeasyPrint for PDF generation.

## How it works

```
resume.yaml  →  Jinja2 template  →  HTML + CSS  →  WeasyPrint  →  PDF
```

Edit your resume data in `build/resume.yaml`, run the build script, and get a styled PDF in `build/output/`.

## Installation

### Prerequisites

- Python 3.10+
- [WeasyPrint system dependencies](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)

On macOS (Homebrew):

```bash
brew install pango libffi
```

On Ubuntu/Debian:

```bash
sudo apt install libpango-1.0-0 libpangoft2-1.0-0 libffi-dev
```

### Setup

```bash
cd build
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

1. Edit `build/resume.yaml` with your information.

2. Run the build script:

```bash
cd build
python build.py
```

3. Find your files in `build/output/`:
   - `resume.html` — intermediate HTML
   - `resume.pdf` — final PDF

## Project structure

```
├── build/
│   ├── build.py              # Build script
│   ├── resume.yaml           # Your resume data
│   ├── requirements.txt      # Python dependencies
│   ├── css/
│   │   └── resume.css        # PDF styling
│   ├── templates/
│   │   └── resume.html.j2    # Jinja2 template
│   └── output/               # Generated files (gitignored)
├── icons/                    # SVG icons for contact info
└── docs/
    └── references/           # Reference PDFs
```

## Customization

- **Content** — Edit `build/resume.yaml`. The YAML structure maps directly to the template sections: contact, summary, skills, languages, experience, articles, and shipped projects.
- **Add or remove sections** — The resume is fully driven by YAML. To add a new section, define it in `resume.yaml` and add a matching block in `resume.html.j2`. To remove one, delete it from both files. You can use AI (Claude, ChatGPT, etc.) to generate new YAML sections or rewrite existing ones. The simplest approach is to give the AI your existing CV in whatever format you have it (PDF, Word, plain text) and let it generate the `resume.yaml` for you. The tool takes care of making the exported PDF ATS-friendly — all your data gets parsed from a single, ultra-lightweight YAML file.
- **Styling** — Edit `build/css/resume.css` to change fonts, spacing, colors, and layout.
- **Layout** — Edit `build/templates/resume.html.j2` to change the HTML structure.
- **Icons** — Drop SVG files into `icons/` and map them in `build.py`'s `ICON_MAP`.

---

#### Found this useful? Give it a star to support the project!

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=giorris&button_colour=5146e6&font_colour=ffffff&font_family=Comic&outline_colour=ffffff&coffee_colour=FFDD00)](https://www.buymeacoffee.com/giorris)
