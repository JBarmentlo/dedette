from book import Book
from recipe import Recipe

if __name__ == "__main__":
	try:
		r1 = Recipe(None , 6, -1, [], "great pizza",  "stato")
	except:
		r2 = Recipe("pizza", 2, 20, ["dough", "tomat", "chees"], "delicious pizzzaaaa", "lunch")
	print(r2)

	b = Book("my recipe book")
	print(f"Book {b}")
	b.add_recipe("LOL")
	print(f"after failed update {b}")
	b.add_recipe(r2)
	print(f"after succesful update {b}")
