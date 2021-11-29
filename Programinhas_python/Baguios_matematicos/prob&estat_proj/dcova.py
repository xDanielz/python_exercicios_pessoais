import numpy as np
import statistics as st
from collections import Counter, namedtuple


class ConjutoDeDados:
    _frequencias = namedtuple('Frequência', 'simples relativa relativaPercentual')
    _frequenciasAcumuladas = namedtuple('FrequênciaAcumulada', 'simples relativa relativaPercentual')

    def __init__(self, conjdados):
        self._dados = np.array(sorted(conjdados))
        self._tamConj = len(self._dados)
        self._frequenciaSimples = Counter(self._dados)
        self._dadosSemRepetir = np.array([k for k in self._frequenciaSimples])
        self._frequenciaAcumuladaSimples = dict().fromkeys(sorted(set(self._dados)))
        self._amplitudeTotal = self._dados[-1] - self._dados[0]

    def __len__(self):
        return self._tamConj

    def frequencias(self, key=None):
        frequencias = {k: self._frequencias(v, v/self._tamConj, (v/self._tamConj)*100)
                       for k, v in self._frequenciaSimples.items()}
        if key is None:
            return frequencias
        return frequencias[key]

    def frequenciasAcumuladas(self, key=None):
        aux = 0
        for k, v in sorted(self._frequenciaSimples.items()):
            aux += v
            self._frequenciaAcumuladaSimples[k] = aux
        frequenciasAcumuladas = {k: self._frequenciasAcumuladas(v, v/self._tamConj, (v/self._tamConj)*100)
                                 for k, v in self._frequenciaAcumuladaSimples.items()}
        if key is None:
            return frequenciasAcumuladas
        return frequenciasAcumuladas[key]

    def mediana(self):
        return self._dados.mean()

    def moda(self):
        return st.multimode(self._dados)

    def mediaAritmetica(self):
        return self._dados.mean()

    def mediaGeometrica(self):
        return st.geometric_mean(self._dados)

    def quartil(self, q):
        op = {1: .25, 2: .50, 3: .75}
        if 1 <= q <= 3:
            return np.quantile(self._dados, op[q])
        raise ValueError("Quartil deve ser um valor no alcance [1, 3]")

    def decil(self, d):
        if 1 <= d <= 10:
            return self.percentil(d*10)
        raise ValueError("Decil deve ser um valor no alcance [1, 10]")

    def percentil(self, p):
        return np.percentile(self._dados, p)

    def variancia(self):
        return self._dados.var()

    def desvioPadrao(self):
        return self._dados.std()

    def coeficienteDeVariacao(self):
        return self.desvioPadrao()/self.mediaAritmetica()*100

    def amplitudeInterquartil(self):
        return self.quartil(3) - self.quartil(1)

    def amplitudeTotal(self):
        return self._amplitudeTotal


