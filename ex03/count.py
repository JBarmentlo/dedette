import sys
import string

def 	is_punctuation(char):
	if (char not in string.punctuation):
		return False
	return True


def	ft_carac(text):
	up = sum(map(str.isupper, text))
	low = sum(map(str.islower, text))
	sp = sum(map(str.isspace, text))
	punc = sum(map(is_punctuation, text))
	print("The text contains", len(text), "characters:")
	print("-",up, "upper letters")
	print("-",low, "lower letters")
	print("-",punc, "punctuation marks")
	print("-",sp, "spaces")

def	text_analyzer(*args, **kwargs):
	"""
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	"""
	if (len(args) > 1):
		print("ERROR")
		return
	elif (len(args) < 1):
		txt = ""
		while txt == "":
			txt = input("What is the text to analyse?\n")
	else:
 		txt = args[0]

	print(f"The text contains {len(txt)} characters:")
	print(f"- {sum(map(str.isupper, txt))} upper letters")
	print(f"- {sum(map(str.islower, txt))} lower letters")
	print(f"- {sum(map(lambda x: (x in string.punctuation), txt))} punctuation marks")
	print(f"- {sum(map(str.isspace, txt))} spaces")