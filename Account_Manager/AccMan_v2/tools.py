import os

def correct_op(text: str, func, wrong_text: str) -> str:
    """
    :param text: text to be applied in the input function
    :param func: function that returns a boolean
    :param wrong_text: text to be displayed if option is false
    :return: returns the correct option when entered
    """

    while True:
        pos = input(text)
        if func(pos):
            os.system('cls')
            return pos
        print_pause(wrong_text)
        os.system('cls')


def print_pause(text):
    print(text)
    os.system('pause')
