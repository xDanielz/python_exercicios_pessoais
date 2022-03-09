w = 'batatinha         x           frita   um dos  tres'


def word_counter_easy(words):
    return len([word for word in words.split() if len(word) > 1])


def word_counter_hard(word):
    letters = 0
    words   = 0
    
    for l in word:
        if l == ' ':
            if letters >= 2:
                words += 1
            letters = 0
            continue
        letters += 1
            
    return words if not words else words + 1
        


print(word_counter_hard(w))

print(word_counter_easy(w))


