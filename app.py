from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sleekbook@127.0.0.1:5000'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Varchar(20), unique=True, nullable=False)
    email = db.Column(db.Varchar(40), unique=True, nullable=False)
    password = db.Column(db.Varchar(20), unique=True, nullable=False)
    image_file = db.column(db.String(20), nullable=False, default='default.jpeg')
    user_ingredients = db.relationship('User_ingredients', backref= 'list', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}, '{self.image_file})"

class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.column(db.Varchar(30), unique=True, nullable= False)

class User_ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredients = db.Column(db.Varchar(20), db.ForeginKey("ingredients.ingredient_name"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class Drinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    recipe = db.Column(db.Varchar(1000))


class Drink_ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredients = db.Column(db.Varchar(20), db.ForeginKey("ingredients.ingredient_name"))
    drink_id = db.Column(db.Integer, db.ForeignKey("drinks.id"))

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
