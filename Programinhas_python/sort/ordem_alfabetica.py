_iterable = ['danilo', 'daniel', 'lucas', 'matheus', 'luana', 'claudiane', 'luan']
alfa = [chr(l) for l in range(ord('a'), ord('z')+1]

for name1 in range(len(_iterable)):
    for name2 in range(name1+1, len(_iterable)):
        c = 0
        while True:
            if alfa.index(_iterable[name1][c]) != alfa.index(_iterable[name2][c]):
                if alfa.index(_iterable[name1][c]) > alfa.index(_iterable[name2][c]):
                    _iterable.insert(name1, _iterable.pop(name2))
                break
            if set(_iterable[name1]).difference(set(_iterable[name2])) == set():
                if len(_iterable[name1]) < len(_iterable[name2]):
                    small = name1
                    pos = name2
                else:
                    small = name2
                    pos = name1
                _iterable.insert(pos, _iterable.pop(small))
                break
            c += 1
print(_iterable)
print(sorted(_iterable))
