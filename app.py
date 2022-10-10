from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import sqlite3

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'thisisasecretkey'


# # it will create a databse with name sqlite.db
# connection= sqlite3.connect('db.sqlite3') 
# cursor= connection.cursor()
# table_query = '''CREATE TABLE  if not Exists Student
#                (Name text, Course text, Age real)'''
       
# cursor.execute(table_query)   

# # student list 

# drinks_data = [
#  ['AlixaProDev','CS',19],
#  ['Alixawebdev','BBa',21],
#   ['AskALixa','Software',22]
# ]
# insert_q = []


# # creating the insert query for each student
# for std_data in students_data:
#     name = std_data[0]
#     course = std_data[1]
#     age = std_data[2]
#     q=f"INSERT INTO Student VALUES ('{name}','{course}','{age}')"
#     insert_q.append(q)

# # executing the insert queries
# for q in insert_q:
#     cursor.execute(q)


user_ingredients = db.Table('user_ingredients',
    db.Column("id", db.Integer, primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('ingredients_id', db.Integer, db.ForeignKey('ingredients.id'))
)
    
drinks_ingredients = db.Table('drinks_ingredients',
    db.Column("id",db.Integer, primary_key=True),
    db.Column('drinks_id', db.Integer, db.ForeignKey('drinks.id')),
    db.Column('ingredients_id', db.Integer, db.ForeignKey('ingredients.id'))
)

class Ingredients(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(30), unique=True, nullable= False)
    user_list_of_ingredients = db.relationship('user', secondary=user_ingredients, backref='user_list')
    drinks_ings = db.relationship('drinks', secondary=drinks_ingredients, backref='ingredients_in_drinks')


class Drinks(db.Model):
    __tablename__ = 'drinks'
    id = db.Column(db.Integer, primary_key=True)
    drink_name = db.Column(db.String(30), unique=True, nullable=False)
    recipe = db.Column(db.String(1000))
    drink_ings = db.relationship('ingredients', secondary=drinks_ingredients, backref='ingredients_in_drinks')

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    ingredient_list = db.relationship('ingredients', secondary=user_ingredients, backref='user_list')

# # you need to commit changes as well
# connection.commit()
# # you also need to close  the connection
# connection.close()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class RegisterForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
         InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/templates/results.html', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        print(request.form.getlist('checkbox'))
        return "done"
    return render_template('results.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)