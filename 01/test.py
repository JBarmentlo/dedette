from game import GotCharacter, Stark

arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print(arya.is_alive)
True
arya.die()
print(arya.is_alive)