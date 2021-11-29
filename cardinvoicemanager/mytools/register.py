class Register:
    def __init__(self):
        self.functions = {}

    def __call__(self, op: int):
        assert op, int

        def deco(func):
            self.functions[op] = func
        return deco

    def __getitem__(self, pos: int):
        assert pos, int
        return self.functions[pos]

