

itens = []
contador = 3
while contador > 0:
    resposta = input()
    itens.append(resposta)
    contador -= 1

print("Lista de itens:")
for item in itens:
    print(f"- {item}")

