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



>> from app import *
>>> orange = Ingredients(ingredient_name='Orange', image='dsfwd')
>>> db.session.add(orange)
>>> db.session.commit()
>>> screwdriver= Drinks(drink_name='Screwdriver', recipe='asjkdhfbakjsd', image='alsdfjhads') 
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
  File "<stdin>", line 4
    )
    ^
SyntaxError: unmatched ')'
>>> for i in ing_ids:
     ingredients.append(Ingredients.query.filter_by(id=i.ingredient_id).first())

print(ingredients)
[<Ingredients 1>]