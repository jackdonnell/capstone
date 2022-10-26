from tkinter import XView


api_key = "9973533"
# Filter by multi-ingredient (only available to $2+ Patreon supporters)
# www.thecocktaildb.com/api/json/v1/1/filter.php?i=Dry_Vermouth,Gin,Anis
# so what i need to do is have this file send a request to the api with the ingredients that are checked in the boxes by the user on the website
# but first i will have to format a request with those ingredients by checking iof they have c=been selected and if they are then we can add them into that request being sent to the api
# then we need to take the data from the api response and find the name of the drink, the ingredients, recipe and image file
# we have to use the name and image to generate a list of the cocktails you can make with the name and picture and recipe and ingredients reqd
# take all the ingredients that are not selected and send an individual api call for each of them, collect the drink ids of all the drinkls for each one of the calls. make a list of all the unique drink ids from those requests. save a list of all the drink ids to a variable. use that list to subtract the drink ids that are collected from the unselected ingredients drink id list. display those drinks that do not contain any of the banned ingredients
# ingredient = ingredient.checked 
# if ingredient.checked == True:
#     request == 'www.thecocktaildb.com/api/json/v1/1/filter.php?i='

drink_ids = ["17222",
"13501",
"17225",
"17837",
"13938",
"14610",
"17833",
"17839",
"15106",
"15266",
"17835",
"11023",
"17228",
"17836",
"17840",
"11046",
"17180",
"11014",
"11020",
"11021",
"11055",
"12560",
"12756",
"13162",
"15182",
"15941",
"16311",
"16333",
"16419",
"17227",
"11024",
"11034",
"11052",
"13807",
"17226",
"178319",
"12790",
"14360",
"14364",
"14622",
"11029",
"11050",
"12564",
"13423",
"15567",
"16289",
"17066",
"11026",
"11027",
"11053",
"13086",
"13683",
"13731",
"15849",
"17223",
"178321",
"178325",
"17834",
"11019",
"12562",
"15194",
"16405",
"178353",
"17838",
"11012",
"11013",
"11022",
"11054",
"12870",
"14272",
"17074",
"17168",
"11028",
"12792",
"12794",
"14564",
"14578",
"14584",
"17118",
"178337",
"12862",
"12864",
"14372",
"14374",
"15597",
"17020",
"17831",
"11025",
"14107",
"15200",
"16354",
"14306",
"16943",
"17094",
"17224",
"12710",
"16134",
"17005",
"11010",
"11011",
"16202",
"17229",
"15675",
"16958",
"17832",
"16082",
"14560",
"15024",
"16100",]

# # it will create a databse with name sqlite.db
# connection= sqlite3.connect('db.sqlite3') 
# cursor= connection.cursor()

# drinks_data = [
#  ['Mimosa',"Chill your champagne flute before preparing the cocktail\nPour the champagne and orange juice directly into the champagne flute\nLastly, garnish your cocktail with an orange wedge","https://www.makemycocktail.com/images/cocktails/Mimosa.jpg?ezimgfmt=rs:383x511/rscb9/ngcb9/notWebP","3 oz. Orange Juice, 3 oz. Champagne"]
# ]
# insert_q = []

# # creating the insert query for each student
# for data in drinks_data:
#     name = data[0]
#     recipe = data[1]
#     img = data[2]
#     ingredients = data[3]
#     q=f"INSERT INTO Drinks VALUES ('{name}','{recipe}','{img}', '{ingredients}';"
#     insert_q.append(q)

# # executing the insert queries
# for q in insert_q:
#     cursor.execute(q)

# # you need to commit changes as well
# connection.commit()
# # you also need to close  the connection
# connection.close()


screwdriver= Drinks(drink_name='Screwdriver', recipe='asjkdhfbakjsd', image='alsdfjhads') 
db.session.add(screwdriver)
db.session.commit()

ing_ids = Drink_ingredients.query.filter_by(drink_id=screwdriver.id).all()
print(ing_ids)

for i in ing_ids:
    ingredients.append(Ingredients.query.filter_by(id=i.ingredient_id).first())

>> from app import *
>>> orange = Ingredients(ingredient_name='Orange', image='dsfwd')
>>> db.session.add(orange)
>>> db.session.commit()
>>> screwdriver= Drinks(drink_name='Screwdriver', recipe='asjkdhfbakjsd', image='') 
>>> db.session.add(screwdriver)
>>> db.session.commit()                                                                        
>>> ing1 = Drink_ingredients(drink_id=screwdriver.id, ingredient_id=orange.id)
>>> db.session.add(ing1)
>>> db.session.commit()
>>> ing_ids = Drink_ingredients.query.filter_by(drink_id=screwdriver.id)
>>> ing_ids = Drink_ingredients.query.filter_by(drink_id=screwdriver.id).all()
>>> print(ing_ids)
[<Drink_ingredients 1>]
>>> ingredients= []
>>> for i in ing_ids:
...     ingredients.append(Ingredients.query.filter_by(id=i.ingredient_id).first())
...
... )

>>> for i in ing_ids:
     ingredients.append(Ingredients.query.filter_by(id=i.ingredient_id).first())

print(ingredients)
[<Ingredients 1>]

texas_tea= Drinks(drink_name='Texas Tea', recipe='Fill your highball glass with ice. Fill your cocktail shaker 2/3 full with cracked ice. Pour .5oz gin, .05oz vodka, .05oz tequila, .05oz rum, .05 oz whiskey, .75oz lemon juice, .75oz simple syrup into the cocktail shaker. Shake your cocktail for 10-15 seconds. Strain the shaker contents into the highball glass. Top off the glass with cola. Gently stir with a straw. Lastly, garnish your cocktail with a lemon wedge', image='https://www.makemycocktail.com/images/cocktails/TexasTea.jpg')
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