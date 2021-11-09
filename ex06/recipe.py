import sys

class CookBook():
    def __init__(self):
        self.cookbook = {"sandwich" : {}, "cake" : {}, "salad" : {}}
        self.cookbook["sandwich"] = {"ingredients" : ["ham", "bread", "cheese", "tomatoes"], "meal" : "lunch", "prep_time" : 10}
        self.cookbook["cake"] = {"ingredients" : ["flour", "sugar", "eggs"], "meal" : "dessert", "prep_time" : 60}
        self.cookbook["salad"] = {"ingredients" : ["avocado", "arugula", "tomatoes", "spinach"], "meal" : "lunch", "prep_time" : 10}


    def print_recipe(self, name):
        print(f"\nRecipe for {name}:")
        print(f"Ingredients list : {self.cookbook[name]['ingredients']}")
        print(f"To be eaten for {self.cookbook[name]['meal']}")
        print(f"Takes {self.cookbook[name]['prep_time']} minutes of cooking.\n\n")

    def delete_recipe(self, name):
        del (self.cookbook[name])

    def add_recipe(self, name, ingredients, meal, prep_time):
        self.cookbook[name] = {"ingredients" : ingredients, "meal" : meal, "prep_time" : prep_time}
        
    def __str__(self):
        string = ""
        for key in self.cookbook.keys():
            string += f"{key}\n"
        return (f"\n{string}\n")

    def input_add_recipe(self):
        name = input("Please enter a name for this recipe:\n")
        while (name == ""):
            name = input("Please enter a name for this recipe:\n")
        

        ingredients = input("Please enter the list of INGREDIENTS needed for this new recipe:\n")
        if (ingredients != ""):
            ingredients = ingredients.split(" ")

        meal = input("Please enter the type of meal that corresponds to this recipe:\n")

        time = input("Please enter the TIME needed to prepare the recipe:\n")
        while (True):
            try:
                time = int(time)
                if (time >= 0):
                    break
            except:
                time = input("ERROR: Please enter the TIME needed to prepare the recipe: (positive integer)\n")
                continue
            time = input("ERROR: Please enter the TIME needed to prepare the recipe: (positive integer)\n")
            
                

        self.add_recipe(name, ingredients, meal, time)
        print(f"Recipe [{name}] added to the cookbook!\n\n")

    def input_delete_recipe(self):
        name = input("\nPlease enter the name of the recipe you want to delete between the existing ones:\n")
        while (True):
            if (name in self.cookbook.keys()):
                print(f"\nYou have deleted the following recipe from the cookbook: {name}\n\n")
                break
            else:
                name = input("\nERROR: Please enter the name of the recipe you want to delete between the existing ones:\n")
        self.delete_recipe(name)
        
    

if __name__=="__main__":
    mybook = CookBook()
    number = input('''Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
''')
    while (True):
        try:
            nb = int(number)
            if (nb < 1 or nb > 5):
                nb = -1
            if (nb == 1):
                mybook.input_add_recipe()
            if (nb == 2):
                mybook.input_delete_recipe()
            if (nb == 3):
                name = input("\nPlease enter the recipe's name to get its details:\n")
                while (True):
                    if (name in mybook.cookbook.keys()):
                        mybook.print_recipe(name)
                        break
                    else:
                        name = input("\nERROR: Please enter a valid recipe's name to get its details:\n")
            if (nb == 4):
                print(mybook)
            if (nb == 5):
                print("Cookbook closed.")
                sys.exit()
            number = input('''Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
''')
        except ValueError:
            number = input("This option does not exist, please type the corresponding number.\n")
    
            
        

    

 