string = str(input("insira uma palavra"))

def inverter_string(string):
    invertida = ""
    for i in range(len(string) - 1, -1, -1):
        invertida += string[i]
    return invertida

print(f"String original: {string}")
print(f"String invertida: {inverter_string(string)}")