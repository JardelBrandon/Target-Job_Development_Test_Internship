string = input("Digite uma sequência de caracteres: ")

string_invertida = str()
for indice in range(len(string) - 1, -1, -1):
    string_invertida += string[indice]

print("Sequência de caracteres invertida: ", string_invertida)