from generator import generator

text = "est Le Lorem Le Ipsum est simplement du faux texte texte ."
print("Normal\n\n")
for word in generator(text):
	print(word)


print("Shuffle\n\n")
for word in generator(text, option="shuffle"):
	print(word)


print("Ordered\n\n")
for word in generator(text, option="ordered"):
	print(word)


print("Unique\n\n")
for word in generator(text, option="unique"):
	print(word)