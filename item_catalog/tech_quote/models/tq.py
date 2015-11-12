"""Define models for tech_quote database (tq)."""

from datetime import datetime

from tech_quote.database import Column, Model, db
from tech_quote.models.user import User


class Author(Model):

    """An author in the tq app."""

    __tablename__ = 'author'

    author_id = Column(db.Integer, primary_key=True)
    author_name = Column(db.String(70), nullable=False)
    author_bio = Column(db.String(200), nullable=False)
    author_created = Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, bio):
        """Create instance for Author."""
        super(Author, self).__init__(author_name=name, author_bio=bio)

    def __repr__(self):
        """Represent Author instance as a string."""
        return '<Author author_id={0}, author_name={1}>'.format(
            self.author_id, self.author_name)


class Category(Model):

    """A category in the tq app."""

    __tablename__ = 'category'

    category_id = Column(db.Integer, primary_key=True)
    category_name = Column(db.String(70), nullable=False)
    category_description = Column(db.Text, nullable=False)
    category_icon_url = Column(db.String(200), nullable=False)

    def __init__(self, name, description, icon_url):
        """Create instance for Category."""
        super(Category, self).__init__(
            category_name=name,
            category_description=description,
            category_icon_url=icon_url)

    def __repr__(self):
        """Represent Category instance as a string."""
        return '<Category category_id={0}, category_name={1}>'.format(
            self.category_id, self.category_name)


class Quote(Model):

    """A quote in the tq app."""

    __tablename__ = 'quote'

    quote_id = Column(db.Integer, primary_key=True)
    quote_text = Column(db.Text, nullable=False)
    quote_source = Column(db.String(200), nullable=False)
    quote_created = Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    author_id = Column(db.Integer, db.ForeignKey('author.author_id'))
    author = db.relationship(Author)
    category_id = Column(db.Integer, db.ForeignKey('category.category_id'))
    category = db.relationship(Category)
    user_id = Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship(User, backref='quote')

    def __init__(self, text, source, **kwargs):
        """Create instance for Quote."""
        super(Quote, self).__init__(
            quote_text=text, quote_source=source, **kwargs)

    def __repr__(self):
        """Represent Quote instance as a string."""
        return '<Quote quote_id={0}, quote_text={1}>'.format(
            self.quote_id, self.quote_text)
