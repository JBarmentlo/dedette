from datetime import date, datetime
from typing import Dict, List

from recipe import Recipe

class Book():
	name			: str
	last_update 	: datetime
	creation_date 	: datetime
	recipes_list 	: Dict[str, List[Recipe]]

	def __init__(self, name):
		self.creation_date = datetime.now()
		if (type(name) != str):
			raise ValueError
		self.name = name
		self.recipes_list = {"starter" : [], "lunch" : [], "dessert" : []}
		self.last_update = datetime.now()


	def get_recipe_by_name(self, name):
		"""
		Prints a recipe with the name \texttt{name} and returns the instance
		"""
		for rtype in self.recipes_list.values():
			for recipe in rtype:
				if (recipe.name == name):
					print(recipe)
					return recipe

		return None


	def get_recipes_by_types(self, recipe_type):
		try:
			return (self.recipes_list[recipe_type])
		except:
			return ([])


	def add_recipe(self, recipe : Recipe):
		if (type(recipe) == Recipe and recipe.recipe_type in ["starter", "lunch", "dessert"]):
			self.last_update = datetime.now()
			self.recipes_list[recipe.recipe_type].append(recipe)
		else:
			print("please input ze recipe my man")
			

	def __str__(self):
		return (f"{self.name = }, created :{self.creation_date.strftime('%d/%m/%Y, %H:%M:%S')}, updated: {self.last_update.strftime('%m/%d/%Y, %H:%M:%S')}")
