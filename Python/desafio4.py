valor = float(input())

if valor > 0:
    #TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
    resultado = "{:.2f}".format(valor)
    print(f"Deposito realizado com sucesso!\nSaldo atual: R$ {resultado}")
elif valor < 0:
   #TODO: Imprimir a mensagem de valor inválido.
   print("Valor invalido! Digite um valor maior que zero.") 
else:
   #TODO: Imprimir a mensagem de encerrar o programa.
   print("Encerrando o programa...")


 