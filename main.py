from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import LibraryForm, EditRatingForm


# Initialise Flask App
app = Flask(__name__)
# Set Secret Key for Form
app.config['SECRET_KEY'] = 'key12345678'
# Set Database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialise Database
db = SQLAlchemy(app)

# Define Database Columns
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Integer(), unique=False, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title
# Create Database w/ Columns
db.create_all()

# Home Page
@app.route('/')
def home():
    return render_template('index.html', library=db.session.query(Book).all())


@app.route("/add", methods=('GET', 'POST'))
def add():
    form = LibraryForm()
    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data.title()
        author = form.author.data.title()
        rating = int(form.rating.data)
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect('/')
    return render_template('add.html', form=form)


@app.route('/edit', methods=('GET', 'POST'))
def edit_rating():
    book_id = request.args.get('id')
    book_to_update = Book.query.get(book_id)
    print(book_to_update)
    form = EditRatingForm()
    if request.method == 'POST' and form.validate_on_submit():
        book_to_update.rating = int(form.new_rating.data)
        db.session.commit()
        return redirect('/')
    return render_template('edit-rating.html', book=book_to_update, form=form)

@app.route('/delete')
def delete_book():
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

