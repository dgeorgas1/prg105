"""Chapter 02 Practice 2 Program - Ingredient Adjuster

Assignment Requirements:
Find a simple recipe online, provide a link to the recipe in the comments.
Display the ingredients with amounts and list the servings that will be made with the recipe.
Ask the user to enter how many servings they would like to make,
and display the required amount of ingredients they will need. Format to one decimal place.

Upload to GitHub and submit your URL.

Recipe link: https://www.allrecipes.com/recipe/17069/taco-dip-i/
"""

sour_cream = 16
cream_cheese = 8
taco_seasoning = 1.25
cheddar_cheese = 16
black_olives = 2.25
servings = 25

how_many_servings = input("How many servings of Taco Dip would you like to make? ")

serving_percent = int(how_many_servings) / servings

sour_cream = sour_cream * serving_percent
cream_cheese = cream_cheese * serving_percent
taco_seasoning = taco_seasoning * serving_percent
cheddar_cheese = cheddar_cheese * serving_percent
black_olives = black_olives * serving_percent

print("In order to make " + how_many_servings +
      " servings of Taco Dip you would need the following ingredient amounts:")
print("Sour Cream -", format(sour_cream, '.1f'), "ozs")
print("Cream Cheese -", format(cream_cheese, '.1f'), "ozs")
print("Taco Seasoning -", format(taco_seasoning, '.1f'), "ozs")
print("Cheddar Cheese -", format(cheddar_cheese, '.1f'), "ozs")
print("Black Olives -", format(black_olives, '.1f'), "ozs")
