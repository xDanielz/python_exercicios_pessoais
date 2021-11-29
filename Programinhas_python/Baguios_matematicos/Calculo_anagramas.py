# Algoritmo que informa a quantidade de anagramas que é possivel se formar com uma determinada palavra.


def numb_of_anagrams(word):
    len_word = len(word)
    more_than_one = [word.count(letter) for letter in set(word) if word.count(letter) > 1]
    a = b = 1
    for c in range(1, len_word+1):
        a *= c
    for num in more_than_one:
        for c in range(1, num+1):
            b *= c
    return a//b


if __name__ == '__main__':
    print(numb_of_anagrams(str(input('Informe a palavra: '))))
