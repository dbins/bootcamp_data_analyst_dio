# Função para prever a afinidade elemental do feiticeiro
def prever_afinidade_elemental(intensidade, componente_raro, fase_lunar, idade_feiticeiro, afinidade_animais):
    # Convertendo a resposta do componente raro e afinidade com animais para booleanos
    componente_raro = componente_raro.lower() == "sim"
    afinidade_animais = afinidade_animais.lower() == "sim"
    resposta = "A afinidade elemental do feiticeiro é com o elemento Ar!"
    # Desenvolva a Lógica de decisão para prever a afinidade elemental
    if intensidade >= 5 and fase_lunar == "crescente" and idade_feiticeiro > 100:
        resposta = "A afinidade elemental do feiticeiro é com o elemento Fogo!"
    if intensidade >= 7 and componente_raro == True and fase_lunar == "cheia" and idade_feiticeiro <= 100 and afinidade_animais == False:
        resposta = "A afinidade elemental do feiticeiro é com o elemento Água!"
    if intensidade >= 7 and componente_raro == True and fase_lunar == "cheia" and idade_feiticeiro <= 100 and afinidade_animais == True:
        resposta = "A afinidade elemental do feiticeiro é com o elemento Terra!"
    
    return resposta

# Entrada do usuário
intensidade_feitico = int(input())
componente_raro_feitico = input()
fase_lunar_feitico = input()
idade_feiticeiro = int(input ())
afinidade_animais_feiticeiro = input()

# Fazendo a previsão
resultado = prever_afinidade_elemental(intensidade_feitico, componente_raro_feitico, fase_lunar_feitico, idade_feiticeiro, afinidade_animais_feiticeiro)

# Saída da previsão
print(resultado)