def primo(n:int) -> bool:
    for c in range(2, (n//2)+1):
        if n % c == 0:
            return False
    return True if 1 != n != 0 else False

