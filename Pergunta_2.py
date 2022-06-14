import math

# Um número é pertencente a série de Fibonacci se 5*n*n + 4 ou 5*n*n - 4 forem quadrados perfeitos

def eh_quadrado_perfeito(verificar_numero):
    raiz_numero = int(math.sqrt(verificar_numero))
    return raiz_numero * raiz_numero == verificar_numero


def eh_pertencente_a_serie_de_fibonacci(verificar_numero):
    primeiro_caso = eh_quadrado_perfeito(5 * pow(verificar_numero, 2) + 4)
    segundo_caso = eh_quadrado_perfeito(5 * pow(verificar_numero, 2) - 4)
    return primeiro_caso or segundo_caso

valor_inserido = int(input("Digite um valor inteiro para ser verificado se pertence a sequência de Fibonacci:"))
if(eh_pertencente_a_serie_de_fibonacci(valor_inserido)):
    print("O valor informado está contido na sequência de Fibonacci!")
else:
    print("O valor informado não está contido na sequência de Fibonacci!")
