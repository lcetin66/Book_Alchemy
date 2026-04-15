"""
This is a simple web application that allows users to add and view books and authors.
"""
import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from data_models import db, Author, Book

# Load environment variables from .env file
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"
)

# Initialize db with app
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    """Add a new author to the database."""
    if request.method == 'POST':
        name = request.form.get('name')
        birthdate_str = request.form.get('birthdate')
        date_of_death_str = request.form.get('date_of_death')

        try:
            birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
            date_of_death = datetime.strptime(date_of_death_str, '%Y-%m-%d').date() \
                if date_of_death_str else None

            new_author = Author(name=name, birth_date=birthdate, death_date=date_of_death)
            db.session.add(new_author)
            db.session.commit()
            flash('Author added successfully!', 'success')
        except ValueError as e:
            flash(f'Date format error: {e}', 'error')
        except Exception as e: # pylint: disable=broad-exception-caught
            flash(f'Error adding author: {e}', 'error')

        return redirect(url_for('add_author'))

    return render_template('add_author.html')


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    """Add a new book to the database."""
    if request.method == 'POST':
        isbn = request.form.get('isbn')
        title = request.form.get('title')
        publication_year = request.form.get('publication_year')
        author_id = request.form.get('author_id')

        try:
            new_book = Book(isbn=isbn, title=title,
                            publication_year=publication_year,
                            author_id=author_id)
            db.session.add(new_book)
            db.session.commit()
            flash('Book added successfully!', 'success')
        except Exception as e: # pylint: disable=broad-exception-caught
            flash(f'Error adding book: {e}', 'error')

        return redirect(url_for('add_book'))

    authors = Author.query.all()
    return render_template('add_book.html', authors=authors)


@app.route('/', methods=['GET'])
def home():
    """Display all books in the database."""
    search_query = request.args.get('search', '')
    sort_by = request.args.get('sort_by', 'title')

    query = Book.query.join(Author)

    if search_query:
        query = query.filter(
            (Book.title.ilike(f"%{search_query}%")) |
            (Author.name.ilike(f"%{search_query}%"))
        )

    if sort_by == 'author':
        query = query.order_by(Author.name)
    elif sort_by == 'year':
        query = query.order_by(Book.publication_year)
    else:
        query = query.order_by(Book.title)

    books = query.all()
    return render_template('home.html', books=books, search_query=search_query)


@app.route('/book/<int:book_id>')
def book_details(book_id):
    """Display the details of a specific book."""
    book = Book.query.get_or_404(book_id)
    return render_template('book_details.html', book=book)


@app.route('/author/<int:author_id>')
def author_details(author_id):
    """Display the details of a specific author."""
    author = Author.query.get_or_404(author_id)
    return render_template('author_details.html', author=author)


@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    """Delete a specific book."""
    try:
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        flash('Book deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting book: {e}', 'error')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
