from Combination_generator import combination_generator as comb_gen


# Algoritmo para geração de anagramas apartir de uma palavra
def anagram_generator(word: str):
    assert isinstance(word, str)
    set_of_words = set()
    for combination in comb_gen(iterable=range(len(word))):
        _anagram = ''
        for letter in combination:
            letter = word[letter]
            _anagram += letter
            if _anagram.count(letter) > word.count(letter):
                break
        else:
            if _anagram not in set_of_words:
                yield _anagram
            set_of_words.add(_anagram)
        continue


phrase = str(input('Palavra: '))
for a in anagram_generator(phrase):
    print(a)
