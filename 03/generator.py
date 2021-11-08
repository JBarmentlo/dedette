import random

def generator(text : str, sep = " ", option = None):
	if (type(text) != str or option not in [None, "shuffle", "unique", "ordered"]):
		yield "ERROR"
		return
	
	if (option == None):
		arr = text.split(sep)
		for w in arr:
			yield w

	if (option == "unique"):
		arr = text.split(sep)
		while (len(arr) != 0):
			w = arr[0]
			arr.pop(0)
			while (w in arr):
				arr.pop(arr.index(w))
			yield w

	if (option == "sort"):
		arr = text.split(sep)
		arr = arr.sort()
		for w in arr:
			yield w

	if (option == "shuffle"):
		arr = text.split(sep)
		while (len(arr) != 0):
			index = random.randrange(len(arr))
			w = arr[index]
			arr.pop(index)
			yield w
