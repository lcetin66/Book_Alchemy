# 📚 Book Alchemy

![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.1-green.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3.1-red.svg)
![Pylint Score](https://img.shields.io/badge/Pylint-10.0%2F10-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

**Book Alchemy** is a sophisticated, minimalist web application designed for bibliophiles to curate and manage their personal digital book archives. Built with Python and Flask, it features a high-end editorial design combined with powerful search and sorting capabilities.

## 🖼️ Screenshots

### Archive Dashboard
![Dashboard](screenshots/dashboard.png)
*Modern minimalist monochrome grid layout.*

### Detailed Record View
![Details](screenshots/details.png)
*High-quality book information with editorial typography.*

### Data Entry
![Cataloging](screenshots/catalog.png)
*Clean and focused forms for authors and books.*

## ✨ Key Features

- **Personal Archive**: Add and manage your collection of authors and books.
- **Advanced Search**: Instant filtering by book titles or author names using case-insensitive search.
- **Dynamic Sorting**: Organize your library by Title, Author, or Publication Year.
- **Detailed Views**: Dedicated profile pages for authors (with full bibliographies) and detailed book views.
- **Modern UI**: A premium, minimalist monochrome design with responsive layouts and glassmorphic elements.
- **Safe Management**: Secure deletion of records with confirmation prompts.
- **Quality Code**: 100% PEP8 compliant with a perfect 10.0/10 Pylint score.

## 🛠️ Technology Stack

- **Backend**: Python 3.13, Flask
- **Database**: SQLite with Flask-SQLAlchemy (ORM)
- **Frontend**: HTML5, Modern CSS3
- **Icons**: FontAwesome 6
- **Typography**: Playfair Display (Serif), Inter (Sans-serif)

## 📂 Project Structure

```text
.
├── app.py              # Main Flask application & routes
├── data_models.py      # Database models (Author & Book)
├── .env                # Environment variables (Configuration)
├── requirements.txt    # Project dependencies
├── screenshots/        # Project screenshots
├── static/
│   └── css/
│       └── style.css   # Custom minimalist design system
└── templates/          # Jinja2 HTML templates
```

## 🚀 Getting Started

1. **Setup Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # .venv\Scripts\activate  # On Windows
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**:
   Create a `.env` file in the root directory (already provided in this repo) and configure your `SECRET_KEY` and `DATABASE_URL`.

4. **Run the application**:
   ```bash
   python app.py
   ```
   *Note: If you are NOT using an activated virtual environment, use `./.venv/bin/python3 app.py`*

5. **Access the library**:
   Open [http://localhost:5001](http://localhost:5001) in your browser.

---
*Developed with ❤️ for book lovers.*
