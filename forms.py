from flask_wtf import FlaskForm
from wtforms import StringField, SearchField, SubmitField, BooleanField, IntegerField, PasswordField
from wtforms.validators import DataRequired, URL, Email


class SearchForm(FlaskForm):
    search_input = SearchField("", validators=[DataRequired()],
                               render_kw={"placeholder": "cafe name or location"})
    submit = SubmitField("Search")


class AddCafeForm(FlaskForm):
    name = StringField("Cafe name", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    img_url = StringField("Image link", validators=[DataRequired(), URL()])
    map_url = StringField("Map link", validators=[DataRequired(), URL()])
    seats = StringField("Seats", validators=[DataRequired()])
    coffee_price = StringField("Coffee price", validators=[DataRequired()])
    has_sockets = BooleanField("Sockets")  # , validators=[DataRequired()])
    has_wifi = BooleanField("Wifi")  # , validators=[DataRequired()])
    has_toilet = BooleanField("Toilets")  # , validators=[DataRequired()])
    can_take_calls = BooleanField("Can take calls")  # , validators=[DataRequired()])
    submit = SubmitField("Add cafe")


class DeleteForm(FlaskForm):
    id = IntegerField("Cafe ID", validators=[DataRequired()])
    delete = SubmitField("Delete cafe")


class AdminForm(FlaskForm):
    username = StringField("Email address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    login = SubmitField("Login")
