from datetime import datetime

if __name__ == "__main__":
    t = (3,30,2019,9,25)
    d = datetime(t[2], t[3], t[4], t[0], t[1])
    s = d.strftime("%m/%d/%Y %H:%M")
    print(s)