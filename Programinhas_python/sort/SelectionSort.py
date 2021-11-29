def possmall(lis: list, start: int = 0):
    small = 0
    for c in range(start, len(lis)):
        if c == start or lis[c] < lis[small]:
            small = c
    return small


def changepos(lis: list, pos1: int, pos2: int) -> None:
    x = lis[pos1]
    lis[pos1] = lis[pos2]
    lis[pos2] = x


def selectionsort(listt: list) -> list:
    listt = listt[:]
    for c in range(len(listt)):
        m = possmall(listt, c)
        changepos(listt, c, m)
    return listt
