# Aula de Funções
from typing import List

# Função de soma de valores

valor_1 = 50
valor_2 = 30

def soma(valor_1_soma: float, valor_2_soma: float = 10) -> float:
    """
    Uma função simples de soma de valores do tipo float e retorna valores do tipo float
    """
    resultado_da_soma = valor_1_soma + valor_2_soma
    return resultado_da_soma

def soma_valor2_em_branco(valor_1_soma: float, valor_2_soma: float = 10) -> float:
    """
    Uma função simples de soma de valores do tipo float e retorna valores do tipo float. Caso o valor 2 não seja informado, irá trazer o valor 10.
    """
    resultado_da_soma = valor_1_soma + valor_2_soma
    return resultado_da_soma

valor_3 = soma(valor_1_soma=valor_1, valor_2_soma=valor_2)
valor_4 = soma_valor2_em_branco(valor_1_soma=valor_1)

print(valor_3)
print(valor_4)


# Função para cálculo da média de valores.

valores_media:List = [5, 5, 5, 5, 5]


def calcular_media(valores_media: List[float]) -> float:
    """
    Função para calcular média. Recebe lista e divide a soma dos valores da lista pela quantidade de argumentos.
    """
    return sum(valores_media) / len(valores_media)

resultado_media = calcular_media(valores_media)

print(resultado_media)

# Função para filtrar dados acima de um limite.

valores_limite:List = [5, 10, 15, 20, 25]
limite:float = 10

def filtrar_acima_de_10(valores_limite: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores_limite:
        if valor > limite:
            resultado.append(valor)
    return resultado

resultado_acima_limite = filtrar_acima_de_10(valores_limite)

print(resultado_acima_limite)