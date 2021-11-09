from tqdm import tqdm
from time import sleep

def ft_progress(lst):
    pbar = tqdm(total=len(lst))
    for elem in lst:
        pbar.update(1)
        yield (elem)
    return

if __name__=="__main__":
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)
