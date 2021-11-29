class CesarCipher:
    def __init__(self, word, key):
        self.word = word
        self.key = key
        self.result = None

    def encrypt(self):
        try:
            self.result = ''.join(chr(ord(letter) + self.key) for letter in self.word)
        except ValueError:
            self.result = 'Chave Invalida'
        finally:
            return self.result

    def decrypt(self):
        try:
            self.result = ''.join(chr(ord(letter) - self.key) for letter in self.word)
        except ValueError:
            self.result = self.encrypt()
        finally:
            return self.result


phrase = str(input('Informe a palavra: '))
k = int(input('Informe a chave: '))
CC = CesarCipher(phrase, k)

operation = int(input('Criptografar[1] ou Decriptografar[2]: ')) - 1
print(CC.encrypt() if not operation else CC.decrypt())
