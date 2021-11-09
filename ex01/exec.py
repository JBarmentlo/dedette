import sys

def		reverse(argc, argv):
    if (argc <= 1):
        return
    string = None
    if (argc >= 2):
        for arg in argv[1:]:
            if string is None:
                string = ""
            string += arg
    
    if (string is not None):
        string = string[::-1]
        string = string.swapcase()
        print(string)
    return

if __name__ == "__main__":
    reverse(len(sys.argv), sys.argv)
