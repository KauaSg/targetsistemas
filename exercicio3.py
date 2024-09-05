import json

with open('dados.json') as f:
    dados = json.load(f)

faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

media_faturamento = sum(faturamentos) / len(faturamentos)

dias_acima = len([dia for dia in faturamentos if dia > media_faturamento])

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento superior à média: {dias_acima}")
