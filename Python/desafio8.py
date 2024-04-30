def prever_fruta(peso, textura, cor):
    resposta = "Não foi possível classificar a fruta."
    # Lógica de decisão baseada nas características fornecidas
    if peso >= 150 and textura == "smooth" and cor == "red":
        resposta = "A fruta é um morango!"
    # TODO: Desenvolva a Função para prever a classe da fruta
    if peso >= 150 and textura == "rough" and cor == "yellow":
        resposta = "A fruta é uma banana!"
    if peso >= 130 and textura == "rough" and cor == "red":
        resposta = "A fruta é uma maçã!"
    if peso >= 120 and textura == "smooth" and cor == "orange":
        resposta = "A fruta é uma laranja!"    


    return resposta

# Entrada do usuário
peso_fruta = float(input())
textura_fruta = input()
cor_fruta = input()

# Chamada da função de previsão
resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)

# Saída da previsão
print(resultado)