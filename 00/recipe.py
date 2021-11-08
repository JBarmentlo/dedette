from typing import List

class Recipe():
	name		: str
	cooking_lvl	: int
	cooking_time: int
	ingredients	: List[str]
	description	: str
	recipe_type : str
	
	def __init__(self, name, lvl, time, ingredients, desc, r_type):
		if (not self.check_input(name, lvl, time, ingredients, desc, r_type)):
			raise ValueError
		
		self.name			= name
		self.cooking_lvl	= lvl
		self.cooking_time	= time
		self.ingredients	= ingredients
		self.description	= desc
		self.recipe_type	= r_type



	def check_input(self, name, lvl, time, ingredients, desc, r_type):
		out = True
		if (type(name) != str):
			print(f"name input incorrect")
			out = False
		
		if (type(lvl) != int or lvl < 1 or lvl > 5):
			print(f"cooking level input incorrect")
			out = False

		if (type(ingredients) != list or len(ingredients) == 0 or type(ingredients[0]) != str):
			print(f"Ingredients input incorrect")
			out = False

		if (type(desc) != str):
			print(f"Description input incorrect")
			out = False

		if (type(r_type) != str or not (r_type in ["starter", "lunch", "dessert"])):
			print(f"recipe_type input incorrect")
			out = False
		
		if (type(time) != int or time < 0):
			print(f"cooking_time input incorrect")
			out = False


		return out


	def __str__(self):
		return (f"{self.name = }, {self.cooking_lvl = }, {self.cooking_time = }, {self.ingredients = }, {self.description = }, {self.recipe_type = }")

