from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    death_date = db.Column(db.Date, nullable=True)
    
    def __repr__(self):
        return f"Author(id={self.id}, name='{self.name}', birth_date='{self.birth_date}', death_date='{self.death_date}')"

    def __str__(self):
        return self.name


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    publication_year = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"Book(id={self.id}, isbn='{self.isbn}', title='{self.title}', publication_year='{self.publication_year}')"

    def __str__(self):
        return self.title



