# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

# TODO: Crie um loop para solicita os itens ao usuário:
contador = 3
while contador > 0:
    # TODO: Solicite o item e armazena na variável "item":
    resposta = input()
    # TODO: Adicione o item à lista "itens":
    itens.append(resposta)
    contador -= 1


# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")