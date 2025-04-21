from flask import Flask, render_template, url_for, redirect, request, flash, abort, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import Integer, String, Boolean
from forms import SearchForm, AddCafeForm, DeleteForm, AdminForm
from flask_bootstrap import Bootstrap5
from werkzeug.security import check_password_hash
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donbQlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.column}


class Admin(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[int] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)


with app.app_context():
    db.create_all()


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("admin_logged_in"):
            return abort(403)
            # Otherwise continue with the route function
        return f(*args, **kwargs)
    return decorated_function


@app.route("/", methods=["GET", "POST"])
def homepage():

    # load all cafe
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()

    # add search bar/function to the page
    find_form = SearchForm()
    if find_form.validate_on_submit():

        # get data from the search bar
        cafe_to_find = find_form.search_input.data

        # go to result page and use input as part of url
        return redirect(url_for("find_cafe", search_input=cafe_to_find))

    return render_template("index.html", cafe_list=all_cafes, form=find_form, num=len(all_cafes))


# add search by location route, html element and css
@app.route("/find-cafe", methods=["GET", "POST"])
def find_cafe():
    cafes_found = []
    num_cafe_found = []
    find_form = SearchForm()

    # since the cafe location in the db are in title case, user input needs to be converted into title case
    cafe_to_find = request.args.get("search_input", "").strip().title()

    # check the input in location column
    try:
        results = db.session.execute(db.select(Cafe).where(Cafe.location == cafe_to_find))
        cafes_found = results.scalars().all()

        # check the input in name column
        if not cafes_found:
            results = db.session.execute(db.select(Cafe).where(Cafe.name == cafe_to_find))
            cafes_found = results.scalars().all()

        # check number of cafes found
        num_cafe_found = len(cafes_found) if cafes_found else 0

    except SQLAlchemyError as e:
        print(f"Database error {e}")

    except AttributeError as e:
        print(f"Attribute error {e}")


    # search function while on the search page
    if find_form.validate_on_submit():

        # get data from the search bar
        cafe_to_find = find_form.search_input.data

        # go to result page and use input as part of url
        return redirect(url_for("find_cafe", search_input=cafe_to_find))

    return render_template("search.html", searched_cafes=cafes_found, form=find_form,
                           num=num_cafe_found, current_user=current_user)


@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    admin_form = AdminForm()
    find_form = SearchForm()

    user_name = admin_form.username.data
    password = admin_form.password.data

    adm_username = db.get_or_404(Admin, 1).username
    adm_password = db.get_or_404(Admin, 1).password

    if admin_form.validate_on_submit():
        if user_name == adm_username and check_password_hash(adm_password, password):
            session["admin_logged_in"] = True
            return redirect(url_for("homepage"))
        else:
            return flash("Wrong credentials, try again!")

    return render_template("admin.html", form_adm=admin_form, session=True, form=find_form)


@admin_only
@app.route("/add_cafe", methods=["GET", "POST"])
def add_cafe():
    cafe_form = AddCafeForm()
    find_form = SearchForm()
    if cafe_form.validate_on_submit():
        new_cafe = Cafe(
            name=cafe_form.name.data,
            map_url=cafe_form.map_url.data,
            img_url=cafe_form.img_url.data,
            location=cafe_form.location.data,
            has_sockets=bool(cafe_form.has_sockets.data),
            has_wifi=bool(cafe_form.has_wifi.data),
            has_toilet=bool(cafe_form.has_toilet.data),
            can_take_calls=bool(cafe_form.can_take_calls.data),
            seats=cafe_form.seats.data,
            coffee_price=cafe_form.coffee_price.data,
        )
        print(new_cafe.has_wifi)
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template("add_cafe.html", add_form=cafe_form, form=find_form)


@app.route("/delete-cafe/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        try:
            db.session.delete(cafe)
            db.session.commit()
            return '', 204  # No content, successful deletion
        except Exception as e:
            db.session.rollback()
            return f"Failed to delete cafe: {str(e)}", 500
    else:
        return "Cafe not found", 404
    # return render_template("homepage.html")  # , form=delete_form)


@app.route("/logout")
def logout():
    session.pop("admin_logged_in", None)
    return redirect(url_for("homepage"))


if __name__ == "__main__":
    app.run(debug=True)
