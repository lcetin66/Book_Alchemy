"""
This module contains the database models for the application.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    """Represents an author in the library."""
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    death_date = db.Column(db.Date, nullable=True)

    books = db.relationship("Book", backref="author", lazy=True)

    def __repr__(self):
        """Return a string representation of the author."""
        return f"<Author {self.id} {self.name}>"

    def __str__(self):
        """Return a string representation of the author."""
        return self.name


class Book(db.Model):
    """Represents a book in the library."""
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    publication_year = db.Column(db.String(100), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    def __repr__(self):
        """Return a string representation of the book."""
        return f"Book(id={self.id}, isbn='{self.isbn}', title='{self.title}', " \
               f"publication_year='{self.publication_year}')"

    def __str__(self):
        """Return a string representation of the book."""
        return self.title
