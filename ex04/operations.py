import sys
import math
import string

usage = "Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3"

def print_and_exit(text):
    print(text)
    return(False)

def parse_arguments(argc):
    if (argc < 2):
        return(print_and_exit(usage))
    if (argc == 2):
        return(print_and_exit(f"InputError: missing one argument\n{usage}"))
    if (argc > 3):
        return(print_and_exit(f"InputError: too many arguments\n{usage}"))
    return (True)
    

def calculate_operations(argv):
    try:
        nb1 = int(argv[1])
        nb2 = int(argv[2])
        Sum = nb1 + nb2
        Difference = nb1 - nb2
        Product = nb1 * nb2
        if (nb2 != 0):
            Quotient = nb1 / nb2
            Remainder = nb1 % nb2
        else:
            Quotient = "ERROR (div by zero)"
            Remainder = "ERROR (modulo by zero)"
        print(f"Sum =\t\t{Sum}\nDifference =\t{Difference}\nProduct =\t{Product}\nQuotient =\t{Quotient}\nRemainder =\t{Remainder}")
        return (True)
    except:
        return(print_and_exit(f"InputError: only numbers\n{usage}"))

if __name__=="__main__":
    if (parse_arguments(len(sys.argv)) == True):
        calculate_operations(sys.argv)