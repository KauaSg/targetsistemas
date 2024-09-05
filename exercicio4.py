sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

faturamento_total = sp + rj + mg + es + outros

percentual_sp = (sp / faturamento_total) * 100
percentual_rj = (rj / faturamento_total) * 100
percentual_mg = (mg / faturamento_total) * 100
percentual_es = (es / faturamento_total) * 100
percentual_outros = (outros / faturamento_total) * 100

print(f"SP: {percentual_sp:.2f}%")
print(f"RJ: {percentual_rj:.2f}%")
print(f"MG: {percentual_mg:.2f}%")
print(f"ES: {percentual_es:.2f}%")
print(f"Outros: {percentual_outros:.2f}%")
