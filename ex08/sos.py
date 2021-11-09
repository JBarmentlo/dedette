import sys

if __name__ == "__main__":
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----'}
    if len(sys.argv) < 2:
        exit()
    string = ""
    for i, arg in enumerate(sys.argv[1:]):
        for j, c in enumerate(arg):
            if c.isspace():
                string += "/ "
                continue
            try:
                string += MORSE_CODE_DICT[c.upper()]
                if (j + 1 != len(arg)):
                    string += " "
            except:
                print("ERROR")
                exit()
        if (i + 1 != len(sys.argv[1:])):
            string += " / "
    print(string)