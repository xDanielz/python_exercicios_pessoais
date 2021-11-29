def calc4travel(fuelprice: float, averagecons: float, km: float) -> float:
    """
    Função para calcular o valor gasto em combustivel para uma viagem de X Km (ida e volta).
    fuelprice: representa o preço do combustivel;
    averagecons: consumo médio do veiculo;
    km: distância em km.
    Retorna o valor em reais da quantia aproximada que será gasta
    em combustivel.
    """
    return (km/averagecons*fuelprice)*2


def trans_value(km: float, val4km: float) -> float:
    """
    Função para calcular um preço sugerido para um frete.
    km: distância em km;
    val4km: preço cobrado por km rodado.
    Retorna o valor sugerido baseado na quantia cobrado por km.
    """
    return val4km*km*2
