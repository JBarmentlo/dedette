import sys
import string

def is_long_enough(word, length):
    return (len(word) > length)

def remove_punctuaction(arg1):
    no_punctuation = arg1.translate(str.maketrans('', '', string.punctuation))
    return (no_punctuation)
    
    

def	filter_words(arg1, arg2):
    try:
        int(arg1)
        print("ERROR")
        return
    except:
        pass
    try:
        length = int(arg2)
    except:
        print("ERROR")
        return
    no_punctuation = remove_punctuaction(arg1)
    words = no_punctuation.split()
    to_keep = list(map(lambda x : is_long_enough(x, length), words))
    final = []
    for i, w in enumerate(words):
        if (to_keep[i] == True):
            final.append(w)
    print(final)
    return

if __name__== "__main__" :
    if (len(sys.argv) <= 2 or len(sys.argv) > 3):
        print("ERROR")
    else:
        filter_words(sys.argv[1], sys.argv[2])