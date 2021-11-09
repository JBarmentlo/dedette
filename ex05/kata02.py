if __name__ == "__main__":
    t = (3,30,2019,9,25)
    hour, minutes, year, month, day = t
    date = ""
    date += "{:0>2d}".format(month) + "/"
    date += "{:0>2d}".format(day) + "/"
    date += str(year) + " "
    date += "{:0>2d}".format(hour) + ":"
    date += "{:0>2d}".format(minutes)
    print(date)