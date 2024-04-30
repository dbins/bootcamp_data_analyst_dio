# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo):
    resposta = ""
    # TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
    if consumo <= 10:
        resposta =  "Plano Essencial Fibra - 50Mbps"
    elif consumo <=20:
        resposta =  "Plano Prata Fibra - 100Mbps"
    elif consumo >20:
        resposta = "Plano Premium Fibra - 300Mbps"
    # TODO: Retorne o plano de internet adequado:
    return resposta
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))