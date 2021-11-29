from math import pow


def nthroot(n, nth) -> float:
    """
    n: O número que vai ser obtido a enésima raiz
    nth: A énesima raiz de n
    return: Retorna a enésima raiz de n
    """
    return pow(n, (1/nth))
