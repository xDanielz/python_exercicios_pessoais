from Anagram_generator import anagram_generator as ana_gen

c = 0
word = str(input('Informe a palavra: '))
copy_word, go = word, True

print('Aguarde...')
while go or c == len(set(word)):
    for anagram in ana_gen(word):
        if anagram == anagram[::-1]:
            print(anagram)
            print(f"Foi necessario {c} letras adicionai/s")
            go = False
            break
    word += sorted(set(word))[c]
    c += 1
