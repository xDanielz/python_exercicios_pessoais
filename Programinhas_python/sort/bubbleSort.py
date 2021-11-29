def bubble_sort(interable: list) -> None:
    size = len(interable)-1
    for k in range(size):
        for i in range(size, k, -1):
            if interable[i] < interable[i-1]:
                aux = interable[i-1]
                interable[i-1] = interable[i]
                interable[i] = aux


l = [13, 23, 3, 8, 1]
bubble_sort(l)
print(l)
