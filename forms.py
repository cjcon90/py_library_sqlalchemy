from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange, ValidationError

# Define Library WTForm
class LibraryForm(FlaskForm):
    title = StringField(label='Title:', validators=[DataRequired('Please enter a book title')])
    author = StringField(label='Author:', validators=[DataRequired('Please enter an author')])
    rating = SelectField(label="Rating (0-10):", validators=[DataRequired('Please select a rating')], choices=['', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], )
    submit = SubmitField(label='Submit')

class EditRatingForm(FlaskForm):
    new_rating = SelectField(label="New Rating (0-10):", validators=[DataRequired('Please select a rating')], choices=['', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], )
    submit = SubmitField(label='Submit')