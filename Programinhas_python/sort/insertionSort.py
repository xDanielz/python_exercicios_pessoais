def insertion_sort(vetor):
    for i in range(len(vetor)):
        for c in range(i):
            if vetor[i] <= vetor[c]:
                vetor.insert(c, vetor.pop(i))
                break


