if __name__ == "__main__":
	phrase = "The right format"
	for i in range(0, 42 - len(phrase)):
		print("-", end = "")
	print(phrase, end = "")