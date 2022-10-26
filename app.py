from email.mime import image
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import sqlite3



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class Ingredients(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(30), unique=True, nullable= False)
    image = db.Column(db.String(100))

class Drinks(db.Model):
    __tablename__ = 'drinks'
    id = db.Column(db.Integer, primary_key=True)
    drink_name = db.Column(db.String(30), unique=True, nullable=False)
    recipe = db.Column(db.String(1000))
    image = db.Column(db.String(100))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

class User_ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    ingredients_id = db.Column(db.Integer, db.ForeignKey(Ingredients.id))

class Drink_ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drink_id = db.Column(db.Integer, db.ForeignKey(Drinks.id))
    ingredient_id = db.Column(db.Integer, db.ForeignKey(Ingredients.id))

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


@app.route('/drinkresults', methods=['GET', 'POST'])
@login_required
def results():
    if request.method == 'POST':
        print(request.form.getlist('ing_checkbox'))
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

texas_tea = Drinks(drink_name='Texas Tea', recipe='Fill your highball glass with ice. Fill your cocktail shaker 2/3 full with cracked ice. Pour .5oz gin, .05oz vodka, .05oz tequila, .05oz rum, .05 oz whiskey, .75oz lemon juice, .75oz simple syrup into the cocktail shaker. Shake your cocktail for 10-15 seconds. Strain the shaker contents into the highball glass. Top off the glass with cola. Gently stir with a straw. Lastly, garnish your cocktail with a lemon wedge', image='https://www.makemycocktail.com/images/cocktails/TexasTea.jpg')
champagne_pick_me_up= Drinks(drink_name='Champagne Pick-Me-Up', recipe='Chill your champagne flute before preparing the cocktail. Fill a shaker 2/3 full with cracked ice. Add 1oz brndy, 1.5oz orange juice and .25oz simple syrup to the shaker. Shake your cocktail for 10-15 seconds. Strain the shaker contents into the champagne flute. Top off the flute with 3.5oz champagne. Lastly, garnish your cocktail with an orange twist', image='https://www.makemycocktail.com/images/cocktails/ChampagnePickMeUp.jpg')
french_75 = Drinks(drink_name='French 75', recipe='Chill your champagne flute before preparing the cocktail. Fill a shaker 2/3 full with cracked ice. Add 1oz gin, .5oz lemon juice and .5oz simple syrup to the shaker. Shake your cocktail for 10-15 seconds. Strain the shaker contents into the champagne flute. Top off the flute with 3oz champagne. Lastly, garnish your cocktail with a lemon twist', image='https://www.makemycocktail.com/images/cocktails/French75.jpg')
gentle_ben = Drinks(drink_name='Gentle Ben', recipe='Fill your highball glass with ice. Pour .75oz vodka, .75oz gin, .75oz tequila and 4oz orange juice directly into the glass. Gently stir with a straw. Lastly, garnish your cocktail with an orange slice', image='https://www.makemycocktail.com/images/cocktails/GentleBen.jpg')
gin_sour = Drinks(drink_name='Gin Sour', recipe='Fill your rocks glass with ice. Add 2oz gin, .75oz lemon juice, and .75oz simple syrup to the shaker. Shake your cocktail without ice for 20-25 seconds. Fill a shaker 2/3 full with cracked ice. Shake your cocktail for 20-25 seconds. Strain the shaker contents into the rocks glass. Lastly, garnish your cocktail with an orange slice and a cherry', image='https://www.makemycocktail.com/images/cocktails/GinSour.jpg')
infante = Drinks(drink_name='Infante', recipe='Fill your rocks glass with ice. Fill a shaker 2/3 full with cracked ice. Add 2oz tequila, 1oz lime juice, 1oz simple syrup and 1 dash bitters to the shaker. Shake your cocktail for 10-15 seconds. Strain the shaker contents into the rocks glass. Lastly, garnish your cocktail with grated nutmeg', image='https://www.makemycocktail.com/images/cocktails/Infante.jpg')
pineapple_daiquiri= Drinks(drink_name='Pineapple Daiquiri', recipe='Chill your coupe glass before preparing the cocktail. Fill a shaker 2/3 full with cracked ice. Add 2oz rum, .75oz pineapple juice, .5oz lime juice and .5oz simple syrup to the shaker. Shake your cocktail for 10-15 seconds. Strain the shaker contents into the chilled coupe glass. Lastly, garnish your cocktail with a lime wheel', image='https://www.makemycocktail.com/images/cocktails/PineappleDaiquiri.jpg')
sazerac = Drinks(drink_name='Sazerac', recipe='Lightly coat the inside of a chilled rocks glass with Pernod. Fill a mixing glass 2/3 full with cracked ice. Add 2oz whiskey, .25oz simple syrup and 4 dashes bitters to the mixing glass. Stir your cocktail for 30-45 seconds. Strain the mixing glass contents into the rocks glass. Lastly, garnish your cocktail with a lemon peel', image='https://www.makemycocktail.com/images/cocktails/Sazerac.jpg')
whiskey_sour= Drinks(drink_name='Whiskey Sour', recipe='Fill your rocks glass with ice. Add 2oz whiskey, .75oz lemon juice and .75oz simple syrup to the shake. Shake your cocktail without ice for 20-25 second. Fill a shaker 2/3 full with cracked ice. Shake your cocktail for 20-25 second. Strain the shaker contents into the rocks glass. Lastly, garnish your cocktail with an orange slice and a cherry', image='https://www.makemycocktail.com/images/cocktails/WhiskeySour.jpg')
zombie = Drinks(drink_name='Zombie', recipe='Fill your hurricane glass with ice. Fill your cocktail shaker 2/3 full with cracked ice. Pour 3oz rum, 2oz pineapple juice, 1oz lime juice and 1oz orange juice into the cocktail shaker. Shake your cocktail for 10-15 seconds. Strain the shaker contents into the hurricane glass. Lastly, garnish your cocktail with a pineapple wedge', image='https://www.makemycocktail.com/images/cocktails/Zombie.jpg')
brandy_old_fashioned= Drinks(drink_name='Brandy Old Fashioned', recipe='Fill your rocks glass with large ice. Fill a mixing glass 2/3 full with cracked ice. Add 2oz brandy, .25oz simple syrup and 3 dashes bitters to the mixing glass. Stir your cocktail for 30-45 seconds. Strain the mixing glass contents into the rocks glass. Lastly, garnish your cocktail with an orange twist', image='https://www.makemycocktail.com/images/cocktails/BrandyOldFashioned.jpg')


bulldog_highball = Drinks(drink_name='Bulldog Highball', recipe='Fill your highball glass with ice. Pour 2oz gin and 1oz orange juice directly into the glass. Top off the glass with 4oz ginger ale. Lastly, garnish your cocktail with an orange slice', image='https://www.makemycocktail.com/images/cocktails/BulldogHighball.jpg')
camerons_kick = Drinks(drink_name='Cameron\'s Kick', recipe='Chill your coupe glass before preparing the cocktail. Fill a shaker 2/3 full with cracked ice. Add 2oz whiskey, .5oz simple syrup and .5oz lemon juice to the shaker. Shake your cocktail for 10-15 seconds. Strain the shaker contents into the chilled coupe glass. Lastly, garnish your cocktail with a lemon peel', image='https://www.makemycocktail.com/images/cocktails/CameronsKick.jpg')
champagne_cocktail = Drinks(drink_name='Champagne Cocktail', recipe='Chill your champagne flute before preparing the cocktail. Pour 5.75oz champagne, .25oz simple syrup and 2 dash bitters directly into the champagne flute. Lastly, garnish your cocktail with a cherry', image='https://www.makemycocktail.com/images/cocktails/ChampagneCocktail.jpg')
cuba_libre = Drinks(drink_name='Cuba Libre', recipe='Fill your highball glass with ice. Pour 2oz rum and .5oz lime juice directly into the glass. Top off the glass with 4.5oz cola. Lastly, garnish your cocktail with a lime wedge', image='https://www.makemycocktail.com/images/cocktails/CubaLibre.jpg')
daiquiri = Drinks(drink_name='Daiquiri', recipe='Chill your coupe glass before preparing the cocktail. Fill a shaker 2/3 full with cracked ice. Add 2oz rum, 1oz lime juice and .75oz simple syrup to the shaker. Shake your cocktail for 10-15 seconds. Strain the shaker contents into the chilled coupe glass. Lastly, garnish your cocktail with a lime twist', image='https://www.makemycocktail.com/images/cocktails/Daiquiri.jpg')
gimlet = Drinks(drink_name='Gimlet', recipe='Chill your coupe glass before preparing the cocktail. Fill a shaker 2/3 full with cracked ice. Add 2oz gin, .75oz lime juice and .75oz simple syrup to the shaker. Shake your cocktail for 10-15 seconds. Strain the shaker contents into the chilled coupe glass. Lastly, garnish your cocktail with a lime wedge', image='https://www.makemycocktail.com/images/cocktails/Gimlet.jpg')
gin_buck = Drinks(drink_name='Gin Buck', recipe='Fill your highball glass with ice. Pour 2oz gin and .5oz lemon juice directly into the glass. Top off the glass with 4.5oz ginger ale. Gently stir with a straw. Lastly, garnish your cocktail with a lemon wedge', image='https://www.makemycocktail.com/images/cocktails/GinBuck.jpg')
old_fashioned = Drinks(drink_name='Old Fashioned', recipe='Fill your rocks glass with large ice. Fill a mixing glass 2/3 full with cracked ice. Add 2oz whiskey, .25oz simple syrup and 3 dash bitters to the mixing glass. Stir your cocktail for 30-45 seconds. Strain the mixing glass contents into the rocks glass. Lastly, garnish your cocktail with an orange twist', image='https://www.makemycocktail.com/images/cocktails/OldFashioned.jpg')
planters_punch = Drinks(drink_name='Planter\'s Punch', recipe='Fill your highball glass with ice. Fill your cocktail shaker 2/3 full with cracked ice. Pour 2oz rum, 2oz lime juice and 2oz simple syrup into the cocktail shaker. Shake your cocktail for 10-15 seconds. Strain the shaker contents into the highball glass. Lastly, garnish your cocktail with an orange slice', image='https://www.makemycocktail.com/images/cocktails/PlantersPunch.jpg')
rum_old_fashioned= Drinks(drink_name='Rum Old Fashioned', recipe='Fill your rocks glass with large ice. Fill a mixing glass 2/3 full with cracked ice. Add 2oz rum, 2oz simple syrup and 2 dash bitters to the mixing glass. Stir your cocktail for 30-45 seconds. Strain the mixing glass contents into the rocks glass. Lastly, garnish your cocktail with an orange twist', image='https://www.makemycocktail.com/images/cocktails/RumOldFashioned.jpg')
tequila_old_fashioned= Drinks(drink_name='Tequila Old Fashioned', recipe='Fill your rocks glass with large ice. Fill a mixing glass 2/3 full with cracked ice. Add 2oz tequila, .25oz simple syrup and 2 dash bitters to the mixing glass. Stir your cocktail for 30-45 seconds. Strain the mixing glass contents into the rocks glass. Lastly, garnish your cocktail with an orange twist', image='https://www.makemycocktail.com/images/cocktails/TequilaOldFashioned.jpg')
gin_orange_juice= Drinks(drink_name='Gin & Orange Juice', recipe='Fill your highball glass with ice. Pour 2oz gin and 5oz orange juice directly into the glass. Gently stir with a straw. Lastly, garnish your cocktail with an orange wedge', image='https://www.makemycocktail.com/images/cocktails/GinOJ.jpg')


gin_tonic = Drinks(drink_name='Gin and Tonic', recipe='Fill your highball glass with ice. Pour 2oz gin directly into the glass. Top off the glass with 5oz tonic water. Lastly, garnish your cocktail with a lime wedge', image='https://www.makemycocktail.com/images/cocktails/GinTonic.jpg')
gin_highball = Drinks(drink_name='Gin Highball', recipe='Fill your highball glass with ice. Pour 2oz gin directly into the glass. Top off the glass with 5oz ginger ale. Lastly, garnish your cocktail with a lemon wedge', image='https://www.makemycocktail.com/images/cocktails/GinHighball.jpg')
mexican_screw = Drinks(drink_name='Mexican Screw', recipe='Fill your highball glass with ice. Pour 2oz tequila and 5oz orange juice directly into the glass. Gently stir with a straw. Lastly, garnish your cocktail with an orange wedge', image='https://www.makemycocktail.com/images/cocktails/MexicanScrew.jpg')
mexicola = Drinks(drink_name='Mexicola', recipe='Fill your highball glass with ice. Pour 2oz tequila directly into the glass. Top off the glass with 5oz cola. Lastly, garnish your cocktail with a lime wedge', image='https://www.makemycocktail.com/images/cocktails/Mexicola.jpg')
mimosa = Drinks(drink_name='Mimosa', recipe='Chill your champagne flute before preparing the cocktail. Pour 3oz champagne and 3oz orange juice directly into the champagne flute. Lastly, garnish your cocktail with an orange wedge', image='https://www.makemycocktail.com/images/cocktails/Mimosa.jpg')
rum_orange_juice = Drinks(drink_name='Rum & Orange Juice', recipe='Fill your highball glass with ice. Pour 2oz rum and 5oz orange juice directly into the glass. Gently stir with a straw. Lastly, garnish your cocktail with an orange wheel', image='https://www.makemycocktail.com/images/cocktails/RumOJ.jpg')
rum_pineapple_juice = Drinks(drink_name='Rum & Pineapple Juice', recipe='Fill your highball glass with ice. Pour 2oz rum and 5oz pineapple juice directly into the glass. Gently stir with a straw. Lastly, garnish your cocktail with a cherry', image='https://www.makemycocktail.com/images/cocktails/RumPJ.jpg')
rum_coke = Drinks(drink_name='Rum and Coke', recipe='Fill your highball glass with ice. Pour 2oz rum directly into the glass. Top off the glass with 5oz cola.', image='https://www.makemycocktail.com/images/cocktails/RumCoke.jpg')
rum_tonic = Drinks(drink_name='Rum and Tonic', recipe='Fill your highball glass with ice. Pour 2oz rum and 5oz tonic directly into the glass. Gently stir with a straw. Lastly, garnish your cocktail with a lime wedge', image='https://www.makemycocktail.com/images/cocktails/RumTonic.jpg')
rum_highball = Drinks(drink_name='Rum Highball', recipe='Fill your highball glass with ice. Pour 2oz rum directly into the glass. Top off the glass with 5oz ginger ale. Lastly, garnish your cocktail with a lemon twist', image='https://www.makemycocktail.com/images/cocktails/RumHighball.jpg')
screwdriver = Drinks(drink_name='Screwdriver', recipe='Fill your highball glass with ice. Pour 2oz vodka and 5oz orange juice directly into the glass. Gently stir with a straw. Lastly, garnish your cocktail with an orange wheel', image='https://www.makemycocktail.com/images/cocktails/Screwdriver.jpg')
vodka_tonic = Drinks(drink_name='Vodka & Tonic', recipe='Fill your highball glass with ice. Pour 2oz vodka directly into the glass. Top off the glass with 5oz tonic water. Lastly, garnish your cocktail with a lime wedge', image='https://www.makemycocktail.com/images/cocktails/VodkaTonic.jpg')


vodka_gimlet = Drinks(drink_name='Vodka Gimlet', recipe='Chill your coupe glass before preparing the cocktail. Fill a shaker 2/3 full with cracked ice. Add 2oz vodka, .75oz lime juice and .75oz simple syrup to the shaker. Shake your cocktail for 10-15 seconds. Strain the shaker contents into the chilled coupe glass. Lastly, garnish your cocktail with a lime wedge', image='https://www.makemycocktail.com/images/cocktails/VodkaGimlet.jpg')
vodka_highball = Drinks(drink_name='Vodka Highball', recipe='Fill your highball glass with ice. Pour 2oz vodka directly into the glass. Top off the glass with 5oz ginger ale. Lastly, garnish your cocktail with a lime wedge', image='https://www.makemycocktail.com/images/cocktails/VodkaHighball.jpg')
whiskey_cola= Drinks(drink_name='Whiskey & Cola', recipe='Fill your highball glass with ice. Pour 2oz whiskey directly into the glass. Top off the glass with 5oz cola. Lastly, garnish your cocktail with a lime wedge', image='https://www.makemycocktail.com/images/cocktails/WhiskeyCola.jpg')
whiskey_highball= Drinks(drink_name='Whiskey Highball', recipe='Fill your highball glass with ice. Pour 2oz whiskey directly into the glass. Top off the glass with 5oz ginger ale. Lastly, garnish your cocktail with a lemon wedge', image='https://www.makemycocktail.com/images/cocktails/WhiskeyHighball.jpg')

gin = Ingredients(ingredient_name='Gin', image='https://www.makemycocktail.com/images/ingredient/Spirit/Spirit_Gin.jpg?ezimgfmt=rs:43x100/rscb9/ng:webp/ngcb9')
rum = Ingredients(ingredient_name='Rum', image='https://www.makemycocktail.com/images/ingredient/Spirit/Spirit_Rum.jpg?ezimgfmt=rs:33x100/rscb9/ng:webp/ngcb9')
vodka = Ingredients(ingredient_name='Vodka', image='https://www.makemycocktail.com/images/ingredient/Spirit/Spirit_Vodka.jpg?ezimgfmt=rs:32x100/rscb9/ng:webp/ngcb9')
whiskey = Ingredients(ingredient_name='Whiskey', image='https://www.makemycocktail.com/images/ingredient/Spirit/Spirit_Whiskey.jpg?ezimgfmt=rs:39x100/rscb9/ng:webp/ngcb9')
tequila = Ingredients(ingredient_name='Tequila', image='https://www.makemycocktail.com/images/ingredient/Spirit/Spirit_Tequila.jpg?ezimgfmt=rs:33x100/rscb9/ng:webp/ngcb9')
coke = Ingredients(ingredient_name='Coke', image='https://www.makemycocktail.com/images/ingredient/Carbonated/Carbonated_Cola.jpg?ezimgfmt=rs:55x100/rscb9/ng:webp/ngcb9')
ginger_ale = Ingredients(ingredient_name='Ginger Ale', image='https://www.makemycocktail.com/images/ingredient/Carbonated/Carbonated_Gingerale.jpg?ezimgfmt=rs:54x100/rscb9/ng:webp/ngcb9')
soda_water = Ingredients(ingredient_name='Soda Water', image='https://www.makemycocktail.com/images/ingredient/Carbonated/Carbonated_Sodawater.jpg?ezimgfmt=rs:54x100/rscb9/ng:webp/ngcb9')
lemon = Ingredients(ingredient_name='Lemon', image='https://www.makemycocktail.com/images/ingredient/Juice/Juice_Lemonjuice.jpg?ezimgfmt=rs:135x86/rscb9/ng:webp/ngcb9')
lime = Ingredients(ingredient_name='Lime', image='https://www.makemycocktail.com/images/ingredient/Juice/Juice_Limejuice.jpg?ezimgfmt=rs:135x89/rscb9/ng:webp/ngcb9')
orange = Ingredients(ingredient_name='Orange', image='https://www.makemycocktail.com/images/ingredient/Juice/Juice_Orangejuice.jpg?ezimgfmt=rs:135x92/rscb9/ng:webp/ngcb9')
pineapple = Ingredients(ingredient_name='Pineapple', image='https://www.makemycocktail.com/images/ingredient/Juice/Juice_Pineapplejuice.jpg?ezimgfmt=rs:118x100/rscb9/ng:webp/ngcb9')
simple_syrup = Ingredients(ingredient_name='Simple Syrup', image='https://www.makemycocktail.com/images/ingredient/Other/Other_Simplesyrup.jpg?ezimgfmt=rs:30x100/rscb9/ng:webp/ngcb9')
bitters = Ingredients(ingredient_name='Bitters', image='https://www.makemycocktail.com/images/ingredient/Other/Other_Bitters.jpg?ezimgfmt=rs:33x100/rscb9/ng:webp/ngcb9')
champagne = Ingredients(ingredient_name='Champagne', image='https://www.makemycocktail.com/images/ingredient/Wine/Wine_Champagne.jpg?ezimgfmt=rs:36x100/rscb9/ng:webp/ngcb9')

def add_ing_to_drink(drink_name, ingredient_name):
    drink= Drinks.query.filter_by(drink_name=drink_name).first()
    ingredient= Ingredients.query.filter_by(ingredient_name=ingredient_name).first()
    if drink == None or ingredient == None:
        print('drink or ing failed')
        return
    try:
        drink_ing= Drink_ingredients(drink_id=drink.id, ingredient_id=ingredient.id)
        db.session.add(drink_ing)
        db.session.commit()
    except:
        print('failed')
# add_ing_to_drink('Texas Tea','Lemon')
# add_ing_to_drink('Texas Tea','Simple Syrup')
# add_ing_to_drink('Texas Tea','Coke')
# add_ing_to_drink('Champagne Pick-Me-Up','Brandy')
# add_ing_to_drink('Champagne Pick-Me-Up','Orange')
# add_ing_to_drink('Champagne Pick-Me-Up','Simple Syrup')
# add_ing_to_drink('Champagne Pick-Me-Up','Champagne')

def get_ings_for_drink(drink_name):
    drink= Drinks.query.filter_by(drink_name=drink_name).first()
    results= Drink_ingredients.query.filter_by(drink_id=drink.id).all()
    ings_in_drink=[]
    for i in results:
        ings_in_drink.append(Ingredients.query.filter_by(id=i.ingredient_id).first().ingredient_name)
    return ings_in_drink

def find_cocktails(ingredients):
    matching_drinks = []
    for i in Drinks.query.all():
        ings= get_ings_for_drink(i.drink_name)
        if set(ings).issubset(set(ingredients)):
            matching_drinks.append(i)
    return(matching_drinks)

if __name__ == "__main__":
    app.run(debug=True)