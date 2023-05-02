# dicionario para guardar os dados que serao usados para o jogo - tela/desenha
assets = {}

#fundos 
assets["fundo1"] = "fundo1.png"
assets["fundo4"] = "fundo4.png"
assets["fundo3"] = "fundo3.png"
assets["fundo5"] = "fundo5.png"
assets["tela_inicial"] = "fundo_inicial1.png"
assets["game_over"] = "game_over.png"
assets["grass"] = "grass.png"
assets["sand"] = "sand.png"
assets["terra"] = "terra.png"
assets["you_win"] = "you win.jpg"

#itens
assets["img_banana"] = "banana.png"
assets["img_berry"] = "berry.png"
assets["img_bola"] = "bola.png"
assets["img_bloco1"] = "bloco1.png"
assets["img_coracao"] = "coracao.png"
assets["img_coracao1"] = "coracao1.png"
assets["img_estrela"] = "estrela.png"
assets["trofeu"] = "trofeu.png"

#imagens 
assets["sanji"] = "sanji.png"
assets["img_gorila"] = "gorila.png"
assets["img_zoro"] = "zoro.png"
assets["tiro1"] = "tiro1.png"
assets["img_macaco"] = "macaco1.png"
assets["img_passaro"] = "passaro.png"
assets["img_parado"] = "parado.png"
assets["img_andando"] = "andando.png"
assets["img_pulando"] = "pulando.png"

#falas
assets["text_box1"] = "text_box1.png"
assets["text_box2"] = "text_box2.png"
assets["text_box3"] = "text_box3.png"
assets["text_box4"] = "text_box4.png"
assets["text_box5"] = "text_box5.png"

assets["tiro"] = 40
assets["window"] = (912.0,512.0)
assets["altura_tela"] = assets["window"][1]
assets["largura_tela"] = assets["window"][0]
assets["bloco"] = (32,24)
assets["vidas"] = 5
assets["estrela"] = 0
assets["monstro_img"] = "macaco1.png"
assets["gorila_img"] = "gorila.png"
assets["esquerda"] = False
assets["texto"] = False
assets["posicao_monstro"] = 'direita'
assets["gorila_vivo"] = True
assets["gorila_vivo2"] = True
assets["gorila_vivo3"] = True
assets["gorila_vivo4"] = True
assets["carne"] = False

# dicionario para guardar os dados que serao usados para o jogo - posicoes/movimento
state = {}

state["posicao_jogador"] = [0.0,400.0]
state["velocidade_jogador"] = [0.0,0.0]
state["aceleracao_gravidade"] = 1 # nao sei pq nao tem que ser negativo kkkkk
state["tempo_0"] = 0 
state["fps"] = 0
