quantidade_passos = input()

#TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
# Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
# Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

if quantidade_passos.isnumeric() == False:
    quantidade_passos = 0
else:
    quantidade_passos = int(quantidade_passos)
    if quantidade_passos < 0:
        quantidade_passos = 0

contador = 1
if quantidade_passos == 0:
    print("Nenhum passo dado na floresta.")        
else:    
    while quantidade_passos > 0:
        if (contador ==1):
            print("Explorador: 1 passo")
        else:
            print(f"Explorador: {contador} passos") 

        quantidade_passos -= 1
        contador += 1

    
