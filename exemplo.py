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

resultado_acima_limite = filtrar_acima_de_10(valores_limite, limite)

print(resultado_acima_limite)


# Função para contar valores únicos numa lista.

lista_valores_unicos = [1,2,2,3,4,5,5,5,5,7,7,9]

def contar_valores_unicos(lista_valores_unicos: List[int]) -> int:
    return len(set(lista_valores_unicos))

resultado_valores_unicos = contar_valores_unicos(lista_valores_unicos)

print(f"A quantidade de valores únicos é {resultado_valores_unicos}.")

# Função de conversão de celcius para fahrenheit.

temp_celsius = [15,16,20,25,30,35]

def celsius_para_fahrenheit(temp_celsius: List[float]) -> List[float]:
    """
    Essa é uma função simples de conversão de temperatura de Fahrenheit para Celsius.
    """
    return [(9/5) * temp + 32 for temp in temp_celsius]

temp_em_fahrenheit = celsius_para_fahrenheit(temp_celsius)

print(temp_em_fahrenheit)

# Função de cálculo de desvio padrão.

valores_dp = [5,10,15,20]

def calcular_desvio_padrao(valores_dp: List[float]) -> float:
    """
    Função básica para o cálculo de desvio padrão.
    """
    media = sum(valores_dp) / len(valores_dp)
    variancia = sum((x - media) ** 2 for x in valores_dp) / len(valores_dp)
    return variancia ** 0.5

resultado_desvio_padrao = calcular_desvio_padrao(valores_dp)

print(resultado_desvio_padrao)

