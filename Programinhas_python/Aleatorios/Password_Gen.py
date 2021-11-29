from random import randint


def password_gen(size=8, num=True, char=True):

    password = str()
    characters = list('!@#$%&*_-.')
    alphabet_upper = [chr(letter) for letter in range(65, 91)]
    alphabet_lower = [letter.lower() for letter in alphabet_upper]
    numbers = [str(num) for num in range(10)]
    selected = [alphabet_upper, alphabet_lower]
  
    if num:
        selected.append(numbers)
    if char:
        selected.append(characters)
  
    while len(password) < size:
        chosen = selected[randint(0, len(selected)-1)]
        for _ in range(randint(1, 2)):
            password += chosen[randint(1, len(chosen)-1)]
            if len(password) == size:
                break
      
    return password

print(password_gen())