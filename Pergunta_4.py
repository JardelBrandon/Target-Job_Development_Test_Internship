faturamento_mensal = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}

faturamento_total_mensal = sum(faturamento_mensal.values())
percentual_faturamento_mensal = dict()
for estado in faturamento_mensal:
    percentual_faturamento_mensal[estado] = '{:.2%}'.format(faturamento_mensal[estado] / faturamento_total_mensal)

print("\nFaturamento mensal por estado: ", faturamento_mensal)
print("\nFaturamento total mensal: ", faturamento_total_mensal)
print("\nPercentual de representação por estado: ", percentual_faturamento_mensal)