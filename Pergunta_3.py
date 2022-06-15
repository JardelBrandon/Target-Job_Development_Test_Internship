import json

with open('assets/dados.json', 'r') as JSON:
    json_vetor = json.load(JSON)

menor_valor_de_faturamento = float("inf")
maior_valor_de_faturamento = 0
valor_medio_de_faturamento = 0
dias_uteis = 0
quantidade_dias_superiores_da_media = 0

for dados in json_vetor:
    if dados['valor'] != 0:
        dias_uteis += 1
        valor_medio_de_faturamento += dados['valor']

        if menor_valor_de_faturamento > dados['valor']:
            menor_valor_de_faturamento = dados['valor']
        if maior_valor_de_faturamento < dados['valor']:
            maior_valor_de_faturamento = dados['valor']

valor_medio_de_faturamento /= dias_uteis

for dados in json_vetor:
    if dados['valor'] > valor_medio_de_faturamento:
        quantidade_dias_superiores_da_media += 1

print("Menor valor de faturamento ocorrido no mês: ", menor_valor_de_faturamento)
print("Maio valor de faturamento ocorrido no mês: ", maior_valor_de_faturamento)
print("Quantidade de dias com o faturamento superior a média mensal: ", quantidade_dias_superiores_da_media)

