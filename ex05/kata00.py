
if __name__ == "__main__":
    t = (19,42,21)
    print(f"The {len(t)} numbers are:", end="")
    for i, tt in enumerate(t):
        if (i != len(t) - 1):
            a = ","
        else:
            a = ""
        print(f" {tt}{a}", end="")