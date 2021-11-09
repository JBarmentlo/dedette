import sys

def		whois(argc, argv):
	if argc != 2:
		print("ERROR")
	elif argc == 2:
		try:
			number = int(argv[1])
			if number == 0:
				print("I'm a Zero.")
			elif number % 2 == 0:
				print("I'm Even.")
			elif number % 2 != 0:
				print("I'm Odd.")
		except ValueError:
			print("ERROR")

if __name__=="__main__":
    whois(len(sys.argv), sys.argv)

