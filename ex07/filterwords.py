import sys
import string

def delete_punctuaction(arg1):
    clean_str = arg1.translate(str.maketrans('', '', string.punctuation))
    return (clean_str)
    



if __name__== "__main__" :
    if (len(sys.argv) <= 2 or len(sys.argv) > 3):
        print("ERROR")
        exit()
    arg1, arg2 = (sys.argv[1], sys.argv[2])
    try:
        int(arg1)
        print("ERROR")
        exit()
    except:
        pass
    try:
        length = int(arg2)
    except:
        print("ERROR")
        exit()
    clean_str = delete_punctuaction(arg1)
    words = clean_str.split()
    to_keep = list(map(lambda x : len(x) > length, words))
    final = []
    for i, w in enumerate(words):
        if (to_keep[i] == True):
            final.append(w)
    print(final)
    exit()