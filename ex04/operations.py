import sys
import math
import string


def parse_arguments(argc):
    usage = "Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3"
    if (argc < 2):
        print(usage)
        return False
    if (argc == 2):
        print(f"InputError: missing one argument\n{usage}")
        return False
    if (argc > 3):
        print(f"InputError: too many arguments\n{usage}")
        return False
    return (True)


def calculate(argv):
    usage = "Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3"
    try:
        nb1 = int(argv[1])
        nb2 = int(argv[2])
        add = nb1 + nb2
        diff = nb1 - nb2
        mul = nb1 * nb2
        if (nb2 != 0):
            div = nb1 / nb2
            reste = nb1 % nb2
        else:
            div = "ERROR (div by zero)"
            reste = "ERROR (modulo by zero)"
        return (add, diff, mul, div, reste)
    except:
        print(f"InputError: only numbers\n\n{usage}")
        exit()


if __name__=="__main__":
    usage = "Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3"
    if (len(sys.argv) < 2):
        print(usage)
        exit()
    if (len(sys.argv) == 2):
        print(f"InputError: missing one argument\n\n{usage}")
        exit()
    if (len(sys.argv) > 3):
        print(f"InputError: too many arguments\n\n{usage}")
        exit()
    add, diff, mul, div, reste = calculate(sys.argv)
    print(f"Sum =\t\t{add}\nDifference =\t{diff}\nProduct =\t{mul}\nQuotient =\t{div}\nRemainder =\t{reste}")
