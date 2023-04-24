# dicionario para guardar os dados que serao usados para o jogo - tela/desenha
assets = {}

assets["fundo1"] = "fundo1.png"
assets["window"] = (912.0,512.0)
assets["altura_tela"] = assets["window"][1]
assets["largura_tela"] = assets["window"][0]
assets["bloco"] = (32,24)

# dicionario para guardar os dados que serao usados para o jogo - posicoes/movimento
state = {}

state["posicao_jogador"] = [0.0,400.0]
state["velocidade_jogador"] = [0.0,0.0]
state["aceleracao_gravidade"] = 1 # nao sei pq nao tem que ser negativo kkkkk
state["tempo_0"] = 0 
state["fps"] = 0