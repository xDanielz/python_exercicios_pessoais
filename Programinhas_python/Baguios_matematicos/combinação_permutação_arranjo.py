class AnaliseCombinatoria:

    @staticmethod
    def fatorial(number, end=0):
        if end > number:
            end, number = number, end
            
        result = 1
        for n in range(number, end, -1):
            result *= n
        return result

    def permutacao_simples(self, n):
        return self.fatorial(n)

    def arranjo_simples(self, n, p):
        return self.fatorial(n)/self.fatorial(n-p)

    @staticmethod
    def arranjo_com_repeticao(n, p):
        return n ** p

    def combinacao_simples(self, n, p):
        r = n - p if p <= n else p - n
        end = max((r, p))
        return self.fatorial(n, end)/self.fatorial(min((r, p)))


print(AnaliseCombinatoria().combinacao_simples(1, 3))
