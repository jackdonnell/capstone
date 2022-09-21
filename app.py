from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sleekbook@127.0.0.1:5000'


user_ingredients = db.Table('user_ingredients',
    db.Column(db.Integer, primary_key=True),
    db.Column('users_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('ingredients_id', db.Integer, db.ForeignKey('ingredients.id'), primary_key=True)
)
    

drinks_ingredients = db.Table('drinks_ingredients',
    db.Column(db.Integer, primary_key=True),
    db.Column('drinks_id', db.Integer, db.ForeignKey('drinks.id'), primary_key=True),
    db.Column('ingredients_id', db.Integer, db.ForeignKey('ingredients.id'), primary_key=True)
)


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.relationship('Ingredients', secondary='user_ingredients', lazy='subquery', backref=db.backref('ingredients', lazy=True))
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Varchar(20), unique=True, nullable=False)
    email = db.Column(db.Varchar(40), unique=True, nullable=False)
    password = db.Column(db.Varchar(20), unique=True, nullable=False)
    image_file = db.column(db.String(20), nullable=False, default='default.jpeg')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}, '{self.image_file})"
        

class Ingredients(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.column(db.Varchar(30), unique=True, nullable= False)

class Drinks(db.Model):
    __tablename__ = 'drinks'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    recipe = db.Column(db.Varchar(1000))

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
