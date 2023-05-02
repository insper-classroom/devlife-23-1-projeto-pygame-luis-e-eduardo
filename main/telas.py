from random import randint
import pygame
from assets import *
from funcoes_adicionais import *
from classes_adicionais import *

#Comentários
#A função load_spritesheet server para "recortar um png com os frames do movimento do jogador e nós pegamos essa função do snippets do github"
#Para fazer o pulo do jogador, nos tambem nos baseamos no algoritimo do snippets

class GameOver():
    def __init__(self, window):

        fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(fonte_padrao, 24)
        self.window = window
        imagem = pygame.image.load("game_over.png")
        self.image = pygame.transform.scale(imagem,(912,580))


    def recebe_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None 
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                assets["vidas"] = 5
                assets["estrela"] = 0
                assets["tiro"] = 20
                return Tela1(self.window)
        return self

    def desenha(self, window):
        window.fill((0, 0, 0))
        window.blit(self.image,(0,0))

class YouWin():
    def __init__(self, window):

        
        fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(fonte_padrao, 24)
        self.window = window
        imagem = pygame.image.load("you win.jpg")
        self.image = pygame.transform.scale(imagem,(912,580))


    def recebe_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None 
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                assets["vidas"] = 5
                assets["estrela"] = 0
                assets["tiro"] = 20
                return Tela1(self.window)
        return self

    def desenha(self, window):
        window.fill((0, 0, 0))
        window.blit(self.image,(0,0))
  
class TelaInicial:
    def __init__(self, window):
        
        #chamando a musica 
        #musica("musica_MFDOOM.mp3")
        
        fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(fonte_padrao, 24)
        self.window = window
        imagem = pygame.image.load("fundo_inicial.png")
        self.image = pygame.transform.scale(imagem,(912,512))


    def recebe_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None 
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                posicao = pygame.mouse.get_pos()
                if posicao[0] >= (912-200)/2 - 35 and posicao[0] <= 912-(912-200)/2 +32:
                    if posicao[1] >=400 and posicao[1]<=470: #nao pode apertar as teclas de andar nao sei pq kkkk
                        return Tela3_1(self.window)
                        
            elif evento.type == pygame.USEREVENT:#tocando a musica durante o jogo inteiro 
                pygame.mixer.music.play()
        return self

    def desenha(self, window):
        window.fill((0, 0, 0))
        largura = 200
        diferenca_largura = (912 - largura)/2
        window.blit(self.image,(0,0))
        pygame.draw.polygon(window,(235,180,51),[(diferenca_largura,400),(912 - diferenca_largura,400),(912 - diferenca_largura,470),(diferenca_largura,470)])
        pygame.draw.circle(window,(235,180,51),(diferenca_largura, 435), 35)
        pygame.draw.circle(window,(235,180,51),(912-diferenca_largura, 435), 35)
        img_mensagem = self.fonte.render("Jogar", True,(255,255,255))
        mensagem = pygame.transform.scale(img_mensagem, (150,60))
        window.blit(mensagem,(diferenca_largura+20, 405))

class Telas():
    def __init__(self, window): 
        
        self.window = window
        self.sprites = pygame.sprite.Group()
        self.plataform = pygame.sprite.Group()
        self.plataformas_quebraveis = pygame.sprite.Group()
        fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(fonte_padrao, 24)
        self.tiro_monstro = pygame.sprite.Group()
        
        self.vidas = 5
        img_coracao = pygame.image.load("coracao.png")
        self.img_coracao = pygame.transform.scale(img_coracao, (25,25))

        self.last_updated = 0

        assets["gorila_vivo"] = True

        chao = pygame.image.load("grass.png")
        self.chao = pygame.transform.scale(chao,(50,15))
        self.plataforma = pygame.sprite.Group()
        self.monstros = pygame.sprite.Group()
        self.gorilas = pygame.sprite.Group()
        self.estrela = pygame.sprite.Group()
        self.passaro = pygame.sprite.Group()
        self.coracao = pygame.sprite.Group()
        self.pocao = pygame.sprite.Group()
        self.jogador = Jogador(self.plataforma,self.monstros,self.estrela, self.coracao,self.gorilas, self.pocao,self.plataformas_quebraveis,self.passaro,self.tiro_monstro)
        self.sprites.add(self.jogador)
        
        assets["estrela"] = 0 #iniciando as coroas com 0 pem toda tela nova 

        self.window = window

    def movimenta_monstro(self,lista_limitantes_x):

        for monstro in self.lista_de_monstros:    
            num_aleatorio1 = randint(0,1)
            if lista_limitantes_x[0] < monstro.rect.x < lista_limitantes_x[1]:
                if num_aleatorio1 > 0.5:
                    monstro.rect.x += 10 #direita 
                    assets["posicao_monstro"] = 'direita'
                else:
                    monstro.rect.x -= 10 #esquerda
                    assets["posicao_monstro"] = 'esquerda'
            elif monstro.rect.x >= lista_limitantes_x[1]:
                monstro.rect.x -= 10 #esquerda
                assets["posicao_monstro"] = 'esquerda'
            elif monstro.rect.x <= lista_limitantes_x[0]:
                monstro.rect.x += 10 #direita 
                assets["posicao_monstro"] = 'direita'
            
    def desenha(self,window):
        
        #colocando o fundo do jogo 
        window.blit(self.fundo,(0,0))

        #desenhando ochao embaixo da plataforma 
        x = 0
        for i in range(30):
            x = 32*i
            window.blit(self.chao,(x,512))
        for i in range(30):
            x = 32*i
            window.blit(self.chao,(x,504))
        for i in range(30):
            x = 32*i
            window.blit(self.chao,(x,496))
        for i in range(30):
            x = 32*i
            window.blit(self.chao,(x,488))

class Tela1_0: #Tela1.0: tutorial de mudança de mapa e coleta de estrelas 
    
    def __init__(self, window):

        #criando o fund0
        fundo = pygame.image.load(assets["fundo1"]) #imagem gerdada pela AI "https://www.scenario.com/""
        self.fundo = pygame.transform.scale(fundo, (912,512))

        #pre-stes de todas as telas 
        Telas.__init__(self,window)

        #gerando as plataformas dos mapas 
        self.gera_mapa()

        #npc para dar as instrucoes do "tutorial"
        zoro = pygame.image.load("zoro.png")
        self.zoro = pygame.transform.smoothscale(zoro,(70,80))
        text_box3 = pygame.image.load("text_box3.png")
        self.text_box1 = pygame.transform.smoothscale(text_box3,(230,230))
        self.aparece_text_box = False 
        self.jogador.speedx = 0


    def gera_mapa(self):
        
        #criando o chao
        for i in range(30):
            x = 32*i
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,x, 480, 'grass')

        Estrela(self.sprites,self.estrela, 700, 440)
     
    def recebe_eventos(self):

        velocidade_x = 3

        clock = pygame.time.Clock()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            
            #caso o botao seja apertado, ele soma a velocidade ate parar de apertar 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.jogador.speedx = velocidade_x
                assets["esquerda"] = False #Para o tiro
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.jogador.speedx = 0
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.jogador.speedx = -velocidade_x
                assets["esquerda"] = True #Para o tiro
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.jogador.speedx = 0
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.jogador.jump()
            if self.jogador.rect.x > 850:
                return Tela1(self.window)
            if assets["vidas"] <= 0:
                return GameOver(self.window)
            
            if 100 > self.jogador.rect.x < 300:
                self.aparece_text_box = True  
            if 100 < self.jogador.rect.x > 300:
                self.aparece_text_box = False 

        ultimo_tempo = self.last_updated 
        tempo = pygame.time.get_ticks()
        delta_t = (tempo-ultimo_tempo)/1000
        self.last_updated = tempo
        self.sprites.update(delta_t)

        clock.tick(120)

        return self

    def desenha(self, window):
        
        #pre-sets de desenho de todas as telas
        Telas.desenha(self,window)

        #desenhando a vida do usuario 
        for i in range(assets["vidas"]):
            window.blit(self.img_coracao,(i*20,0))
        
        #desenhando o zoro npc, para instrucoes 
        window.blit(self.zoro,(200,408))
        #desenhando a fala do zoro caso o jogador esteja perto dele 
        if self.aparece_text_box:
            window.blit(self.text_box1,(62,275))

        self.sprites.draw(self.window)

class Tela1: #Tela1: tutorial de movimentacao e pulo
    
    def __init__(self, window):

        #criando o fund0
        fundo = pygame.image.load(assets["fundo1"]) #imagem gerdada pela AI "https://www.scenario.com/""
        self.fundo = pygame.transform.scale(fundo, (912,512))

        #pre-stes de todas as telas 
        Telas.__init__(self,window)

        #gerando as plataformas dos mapas 
        self.gera_mapa()

        #npc para dar as instrucoes do "tutorial"
        zoro = pygame.image.load("zoro.png")
        self.zoro = pygame.transform.smoothscale(zoro,(70,80))
        text_box1 = pygame.image.load("text_box1.png")
        self.text_box1 = pygame.transform.smoothscale(text_box1,(230,230))
        self.aparece_text_box = False 
        self.jogador.speedx = 0


    def gera_mapa(self):
        
        #criando o chao
        for i in range(30):
            x = 32*i
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,x, 480, 'grass')

        gera_plataforma(self,4,'x',274,430)
        gera_plataforma(self,4,'x',414,400)
        gera_plataforma(self,4,'x',554,430)
        gera_plataforma(self,4,'y',452,750)

        Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,726, 380, 'bloco')
        Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,774, 380, 'bloco')

        Estrela(self.sprites,self.estrela, 760, 337)
     
    def recebe_eventos(self):

        velocidade_x = 3

        clock = pygame.time.Clock()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            
            #caso o botao seja apertado, ele soma a velocidade ate parar de apertar 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.jogador.speedx = velocidade_x
                assets["esquerda"] = False #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.jogador.speedx = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.jogador.speedx = -velocidade_x
                assets["esquerda"] = True #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.jogador.speedx = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.jogador.jump()
            if self.jogador.rect.x > 850 and assets["estrela"] == 1:
                return Tela1_2(self.window)
            if assets["vidas"] <= 0:
                return GameOver(self.window)
            
            if 100 > self.jogador.rect.x < 300:
                self.aparece_text_box = True  
            if 100 < self.jogador.rect.x > 300:
                self.aparece_text_box = False 

        ultimo_tempo = self.last_updated 
        tempo = pygame.time.get_ticks()
        delta_t = (tempo-ultimo_tempo)/1000
        self.last_updated = tempo
        self.sprites.update(delta_t)

        clock.tick(120)

        return self

    def desenha(self, window):
        
        #pre-sets de desenho de todas as telas
        Telas.desenha(self,window)

        #desenhando a vida do usuario 
        for i in range(assets["vidas"]):
            window.blit(self.img_coracao,(i*20,0))
        
        #desenhando o zoro npc, para instrucoes 
        window.blit(self.zoro,(200,408))
        #desenhando a fala do zoro caso o jogador esteja perto dele 
        if self.aparece_text_box:
            window.blit(self.text_box1,(62,275))

        self.sprites.draw(self.window)
        
class Tela1_2(Telas):
    
    def __init__(self, window):
        #criando o fund0
        fundo = pygame.image.load(assets["fundo1"]) #imagem gerdada pela AI "https://www.scenario.com/""
        self.fundo = pygame.transform.scale(fundo, (912,512))

        #pre-stes de todas as telas 
        Telas.__init__(self,window)

        #gerando as plataformas dos mapas 
        self.gera_mapa()

        #npc para dar as instrucoes do "tutorial"
        zoro = pygame.image.load("zoro.png")
        self.zoro = pygame.transform.smoothscale(zoro,(70,80))
        text_box1 = pygame.image.load("text_box2.png")
        self.text_box1 = pygame.transform.smoothscale(text_box1,(230,230))
        self.aparece_text_box = False 

        img_tiro = pygame.image.load('bola.png')
        self.tiro = pygame.transform.scale(img_tiro,(15,15))

        #gerando os monstros no mapa 
        self.limita_monstros_x = [350,750]
        self.lista_de_monstros = []
        for i in range(8):
            x = randint(self.limita_monstros_x[0],self.limita_monstros_x[1])
            self.monstro = Monstro(self.sprites,self.monstros, x, 440) 
            self.lista_de_monstros.append(self.monstro) 
    
    def gera_mapa(self):
        
        #criando o chao
        for i in range(30):
            x = 32*i
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,x, 480, 'grass')

        diferenca_entre_blocos_y = 25
        #colocar bloco no chao, y = 452
        
        #criando as plataformas 
        Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,300, 452, 'bloco')
        Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,300, 452 - diferenca_entre_blocos_y, 'bloco')

        Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,800, 452, 'bloco')
        Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,800, 452 - diferenca_entre_blocos_y, 'bloco')

        gera_plataforma(self,10,'x',434,390)
        gera_plataforma(self,6,'x',600,300)
        gera_plataforma(self,6,'x',400,210)
        gera_plataforma(self,6,'x',180,260)
        gera_plataforma(self,3,'x',50,180)

        Estrela(self.sprites,self.estrela, 84, 140)
        Coracao(self.sprites, self.coracao, 410, 140)
        Coracao(self.sprites, self.coracao, 700, 200)
        Pocao(self.sprites, self.pocao, 600, 350)
        Pocao(self.sprites, self.pocao, 200, 200)



    def recebe_eventos(self):

        velocidade_x = 3

        clock = pygame.time.Clock()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            
            #caso o botao seja apertado, ele soma a velocidade ate parar de apertar 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.jogador.speedx = velocidade_x
                assets["esquerda"] = False #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.jogador.speedx = 0
                print(self.jogador.speedx)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.jogador.speedx = -velocidade_x
                assets["esquerda"] = True #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.jogador.speedx = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.jogador.jump()
            if event.type==pygame.KEYDOWN and event.key == pygame.K_e:
                assets["tiro"] -= 1
                if assets["tiro"] >= 0:
                    Tiro(self.sprites, self.monstros, self.plataforma,self.plataformas_quebraveis,self.gorilas,self.passaro, self.jogador.rect.x, self.jogador.rect.y+25)

            if self.jogador.rect.x > 850 and assets["estrela"] == 1:
                return Tela2_0(self.window)
            if assets["vidas"] <= 0:
                return GameOver(self.window)
            
            if 100 > self.jogador.rect.x < 300:
                self.aparece_text_box = True  
            if 100 < self.jogador.rect.x > 300:
                self.aparece_text_box = False 

            if event.type==pygame.KEYDOWN: #movimentacao dos monstros 
                Telas.movimenta_monstro(self,self.limita_monstros_x)
            #self.aparece_text_box = False 

        ultimo_tempo = self.last_updated 
        tempo = pygame.time.get_ticks()
        delta_t = (tempo-ultimo_tempo)/1000
        self.last_updated = tempo
        self.sprites.update(delta_t)

        clock.tick(120)

        return self

    def desenha(self,window):
                
        #pre-sets de desenho de todas as telas
        Telas.desenha(self,window)

        #desenhando a vida do usuario 
        for i in range(assets["vidas"]):
            window.blit(self.img_coracao,(i*20,0))
        for i in range(assets["tiro"]):
            if i<10:
                window.blit(self.tiro,(i*14 + 770,0))
            if i < 20 and i >= 10:
                window.blit(self.tiro,(i*14-70+700,13))
            if i < 30 and i>=20:
                window.blit(self.tiro,(i*14-140+630,26))
            if i < 40 and i>=30:
                window.blit(self.tiro,(i*14-210+560,39))

        # quant_tiros = assets["tiro"]
        # tiro = pygame.transform.scale(self.tiro,(40,40))
        # window.blit(tiro,(850,0))
        # fonte = pygame.font.get_default_font()
        # fonte = pygame.font.Font(fonte,20)
        # img_quant_tiros = fonte.render(f"{quant_tiros}", True, (0,0,0))
        # window.blit(img_quant_tiros,(860,13))

        
        #desenhando o zoro npc, para instrucoes 
        window.blit(self.zoro,(200,408))
        #desenhando a fala do zoro caso o jogador esteja perto dele 
        if self.aparece_text_box:
            window.blit(self.text_box1,(62,275))

        self.sprites.draw(self.window)

class Tela2_0:
    
    def __init__(self, window):
        #criando o fund0
        fundo = pygame.image.load(assets["fundo4"]) #imagem gerdada pela AI "https://www.scenario.com/""
        self.fundo = pygame.transform.scale(fundo, (912,512))

        #pre-stes de todas as telas 
        Telas.__init__(self,window)

        #gerando as plataformas dos mapas 
        self.gera_mapa()

        #gerando os monstros no mapa 
        self.limita_monstros_x = [565,650]
        self.lista_de_monstros = []
        for i in range(2):
            #x = randint(self.limita_monstros_x[0],self.limita_monstros_x[1])
            self.monstro = Monstro(self.sprites,self.monstros, 600, 150) 
            self.lista_de_monstros.append(self.monstro)
        
        img_tiro = pygame.image.load('bola.png')
        self.tiro = pygame.transform.scale(img_tiro,(15,15))
    
    def gera_mapa(self):
        
        #criando o chao
        for i in range(30):
            x = 32*i
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,self.gorilas,self.passaro, x, 480, 'grass')

        #criando as plataformas 

        gera_plataforma(self,4,'x',50,180)
        Estrela(self.sprites,self.estrela, 96, 145)


        gera_plataforma(self,4,'x',360,270)
        Estrela(self.sprites,self.estrela, 400, 235)

        gera_plataforma(self,2,'x',110,420)
        gera_plataforma(self,2,'x',200,200)
        gera_plataforma(self,2,'x',240,350)

        gera_plataforma(self,12,'y',455,550)
        gera_plataforma(self,12,'y',455,780)
        gera_plataforma(self,4,'x',574,191)
        gera_plataforma(self,5,'x',780,191)
        gera_plataforma(self,3,'x',574,390)
        gera_plataforma(self,3,'x',710,290)
        Estrela(self.sprites,self.estrela, 680, 445)

        Coracao(self.sprites, self.coracao, 850, 145)
        Coracao(self.sprites, self.coracao, 280, 300)
        Pocao(self.sprites, self.pocao, 600, 350)

    def recebe_eventos(self):

        velocidade_x = 3

        clock = pygame.time.Clock()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            
            #caso o botao seja apertado, ele soma a velocidade ate parar de apertar 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.jogador.speedx = velocidade_x
                assets["esquerda"] = False #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.jogador.speedx = 0
                print(self.jogador.speedx)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.jogador.speedx = -velocidade_x
                assets["esquerda"] = True #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.jogador.speedx = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.jogador.jump()
            if event.type==pygame.KEYDOWN and event.key == pygame.K_e:
                assets["tiro"] -= 1
                if assets["tiro"] >= 0:
                    Tiro(self.sprites, self.monstros, self.plataforma,self.plataformas_quebraveis,self.jogador.rect.x, self.jogador.rect.y+25)
            if self.jogador.rect.x > 850 and assets["estrela"] == 3:
                return Tela2_1(self.window)
            if assets["vidas"] <= 0:
                return GameOver(self.window)
            
            if 100 > self.jogador.rect.x < 300:
                self.aparece_text_box = True  
            if 100 < self.jogador.rect.x > 300:
                self.aparece_text_box = False 

            if event.type==pygame.KEYDOWN: #movimentacao dos monstros 
                Telas.movimenta_monstro(self,self.limita_monstros_x)
            #self.aparece_text_box = False 

        ultimo_tempo = self.last_updated 
        tempo = pygame.time.get_ticks()
        delta_t = (tempo-ultimo_tempo)/1000
        self.last_updated = tempo
        self.sprites.update(delta_t)

        clock.tick(120)

        return self

    def desenha(self,window):
                
        #pre-sets de desenho de todas as telas
        Telas.desenha(self,window)

        #desenhando a vida do usuario 
        for i in range(assets["vidas"]):
            window.blit(self.img_coracao,(i*20,0))
        
        for i in range(assets["tiro"]):
            if i<10:
                window.blit(self.tiro,(i*14 + 770,0))
            if i < 20 and i >= 10:
                window.blit(self.tiro,(i*14-70+700,13))
            if i < 30 and i>=20:
                window.blit(self.tiro,(i*14-140+630,26))
            if i < 40 and i>=30:
                window.blit(self.tiro,(i*14-210+560,39))

        self.sprites.draw(self.window)

class Tela2_1:
    
    def __init__(self, window):
        #criando o fund0
        fundo = pygame.image.load(assets["fundo4"]) #imagem gerdada pela AI "https://www.scenario.com/""
        self.fundo = pygame.transform.scale(fundo, (912,512))

        #pre-stes de todas as telas 
        Telas.__init__(self,window)

        #gerando as plataformas dos mapas 
        self.gera_mapa()

        #gerando os monstros no mapa 
        self.limita_monstros_x = [0,500]
        self.lista_de_monstros = []
        for i in range(6):
            x = randint(self.limita_monstros_x[0],self.limita_monstros_x[1])
            a = Monstro(self.sprites,self.monstros, x, 412) 
            self.lista_de_monstros.append(a)

        self.lista_de_gorilas = []
        for i in range(1):
            b = Gorila(self.sprites,self.gorilas, 50, 220, 'esquerda') 
            self.lista_de_gorilas.append(b)

        self.lista_passaros = []
        for i in range(1):
            x = randint(200,800)
            c = Passaro(self.sprites,self.passaro, x, 30,self.jogador,self.lista_passaros) 
            self.lista_de_gorilas.append(c)
        
        img_tiro = pygame.image.load('bola.png')
        self.tiro = pygame.transform.scale(img_tiro,(15,15))

        self.contador = 0

    def gera_mapa(self):
        
        #criando o chao
        for i in range(30):
            x = 32*i
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,x, 480, 'grass')

        #criando as plataformas e as estrelas 
        gera_plataforma(self,40, 'x', -50, 450)
        Estrela(self.sprites,self.estrela, 10, 415)
        gera_plataforma(self,25, 'x', -50, 320)
        Estrela(self.sprites,self.estrela, 10, 285)
        gera_plataforma(self,15, 'x', -50, 190)

        gera_plataforma(self,4, 'x', 610, 220)
        Estrela(self.sprites,self.estrela, 655, 185)
        gera_plataforma(self,2, 'x', 630, 380)

        Coracao(self.sprites, self.coracao, 830, 390)
        Pocao(self.sprites, self.pocao, 650, 350)
        Pocao(self.sprites, self.pocao, 120, 250)
    
    def recebe_eventos(self):

        velocidade_x = 3

        clock = pygame.time.Clock()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            
            #caso o botao seja apertado, ele soma a velocidade ate parar de apertar 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.jogador.speedx = velocidade_x
                assets["esquerda"] = False #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.jogador.speedx = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.jogador.speedx = -velocidade_x
                assets["esquerda"] = True #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.jogador.speedx = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.jogador.jump()
            if event.type==pygame.KEYDOWN and event.key == pygame.K_e:
                assets["tiro"] -= 1
                if assets["tiro"] >= 0:
                    Tiro(self.sprites, self.monstros, self.plataforma,self.plataformas_quebraveis,self.gorilas,self.passaro, self.jogador.rect.x, self.jogador.rect.y+25)
            if self.jogador.rect.x > 850 and assets["estrela"] == 3:
                return Tela2_2(self.window)
            if assets["vidas"] <= 0:
                return GameOver(self.window)

            if event.type==pygame.KEYDOWN: #movimentacao dos monstros 
                Telas.movimenta_monstro(self,self.limita_monstros_x)
            
            #self.aparece_text_box = False 

        ultimo_tempo = self.last_updated 
        tempo = pygame.time.get_ticks()
        delta_t = (tempo-ultimo_tempo)/1000
        self.last_updated = tempo
        self.sprites.update(delta_t)

        clock.tick(120)

        return self

    def desenha(self,window):
                
        #pre-sets de desenho de todas as telas
        Telas.desenha(self,window)

        #desenhando a vida do usuario 
        for i in range(assets["vidas"]):
            window.blit(self.img_coracao,(i*20,0))
        
        for i in range(assets["tiro"]):
            if i<10:
                window.blit(self.tiro,(i*14 + 770,0))
            if i < 20 and i >= 10:
                window.blit(self.tiro,(i*14-70+700,13))
            if i < 30 and i>=20:
                window.blit(self.tiro,(i*14-140+630,26))
            if i < 40 and i>=30:
                window.blit(self.tiro,(i*14-210+560,39))
        
        self.contador+=1
        if self.contador == 120:
            self.contador = 0
            if assets["gorila_vivo"]:
                Tiro_monstro(self.sprites, self.plataforma,self.plataformas_quebraveis,140, 290, self.tiro_monstro,"direita")


        self.sprites.draw(self.window)

class Tela2_2:
    
    def __init__(self, window):
        #criando o fund0
        fundo = pygame.image.load(assets["fundo4"]) #imagem gerdada pela AI "https://www.scenario.com/""
        self.fundo = pygame.transform.scale(fundo, (912,512))

        #pre-stes de todas as telas 
        Telas.__init__(self,window)

        #gerando as plataformas dos mapas 
        self.gera_mapa()

        #gerando os monstros no mapa 
        self.limita_monstros_x = [0,100]
        self.lista_de_monstros = []
        for i in range(2):
            x = randint(self.limita_monstros_x[0],self.limita_monstros_x[1])
            monstro = Monstro(self.sprites,self.monstros, x, 412) 
            self.lista_de_monstros.append(monstro)

        self.lista_de_gorilas = []
        for i in range(1):
            gorilas = Gorila(self.sprites,self.gorilas, 750, 200, 'direita') 
            self.lista_de_gorilas.append(gorilas)

        self.lista_passaros = []
        for i in range(1):
            x = randint(200,800)
            passaro = Passaro(self.sprites,self.passaro, x, 30,self.jogador,self.lista_passaros) 
            self.lista_de_gorilas.append(passaro)

        img_tiro = pygame.image.load('bola.png')
        self.tiro = pygame.transform.scale(img_tiro,(15,15))

        self.contador = 0
        assets["gorila_vivo"] = True
    
    def gera_mapa(self):
        
        #criando o chao
        for i in range(30):
            x = 32*i
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,x, 480, 'grass')

        gera_plataforma(self,40, 'x', -50, 450)
        gera_plataforma(self,18, 'x', -50, 300)
        gera_plataforma(self,20, 'x', 550, 300)

        gera_plataforma(self,5, 'x', 150, 220)
        gera_plataforma(self,5, 'x', 620, 220)
        gera_plataforma(self,5, 'x', 380, 140)
        
        x = 0
        for i in range(5):
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,200, 428 - x, 'sand')
            x += 25
        x = 0
        for i in range(5):
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,225, 428 - x, 'sand')
            x += 25
        Estrela(self.sprites,self.estrela, 20, 415)
        x = 0
        for i in range(5):
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,700, 428 - x, 'sand')
            x += 25
        x = 0
        for i in range(5):
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,725, 428 - x, 'sand')
            x += 25
        Estrela(self.sprites,self.estrela, 850, 415)

        Coracao(self.sprites, self.coracao, 150, 260)
        Coracao(self.sprites, self.coracao, 600, 260)
        Pocao(self.sprites, self.pocao, 100, 260)
        Pocao(self.sprites, self.pocao, 700, 260)
        Pocao(self.sprites, self.pocao, 420, 90)
        Pocao(self.sprites, self.pocao, 380, 410)
        Pocao(self.sprites, self.pocao, 480, 410)

    def recebe_eventos(self):

        velocidade_x = 3

        clock = pygame.time.Clock()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            
            #caso o botao seja apertado, ele soma a velocidade ate parar de apertar 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.jogador.speedx = velocidade_x
                assets["esquerda"] = False #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.jogador.speedx = 0
                print(self.jogador.speedx)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.jogador.speedx = -velocidade_x
                assets["esquerda"] = True #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.jogador.speedx = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.jogador.jump()
            if event.type==pygame.KEYDOWN and event.key == pygame.K_e:
                assets["tiro"] -= 1
                if assets["tiro"] >= 0:
                    Tiro(self.sprites, self.monstros, self.plataforma,self.plataformas_quebraveis,self.gorilas,self.passaro,self.jogador.rect.x, self.jogador.rect.y+25)
            if self.jogador.rect.x > 850 and assets["estrela"] == 2:
                assets["gorila_vivo"] = True
                return Tela3_0(self.window)
            if assets["vidas"] <= 0:
                return GameOver(self.window)

            if event.type==pygame.KEYDOWN: #movimentacao dos monstros 
                Telas.movimenta_monstro(self,self.limita_monstros_x)
            #self.aparece_text_box = False 

        ultimo_tempo = self.last_updated 
        tempo = pygame.time.get_ticks()
        delta_t = (tempo-ultimo_tempo)/1000
        self.last_updated = tempo
        self.sprites.update(delta_t)

        clock.tick(120)

        return self

    def desenha(self,window):
                
        #pre-sets de desenho de todas as telas
        Telas.desenha(self,window)

        #desenhando a vida do usuario 
        for i in range(assets["vidas"]):
            window.blit(self.img_coracao,(i*20,0))
        
        for i in range(assets["tiro"]):
            if i<10:
                window.blit(self.tiro,(i*14 + 770,0))
            if i < 20 and i >= 10:
                window.blit(self.tiro,(i*14-70+700,13))
            if i < 30 and i>=20:
                window.blit(self.tiro,(i*14-140+630,26))
            if i < 40 and i>=30:
                window.blit(self.tiro,(i*14-210+560,39))

        self.contador+=1
        if self.contador == 120:
            self.contador = 0
            if assets["gorila_vivo"]:
          
                Tiro_monstro(self.sprites, self.plataforma,self.plataformas_quebraveis,780, 270, self.tiro_monstro,"esquerda")
        self.sprites.draw(self.window)

class Tela3_0:
    
    def __init__(self, window):
        #criando o fund0
        fundo = pygame.image.load(assets["fundo3"]) #imagem gerdada pela AI "https://www.scenario.com/""
        self.fundo = pygame.transform.scale(fundo, (912,512))

        #pre-stes de todas as telas 
        Telas.__init__(self,window)

        #gerando as plataformas dos mapas 
        self.gera_mapa()

        #gerando os monstros no mapa 
        self.limita_monstros_x = [0,100]
        self.lista_de_monstros = []
        for i in range(0):
            x = randint(self.limita_monstros_x[0],self.limita_monstros_x[1])
            self.monstro = Monstro(self.sprites,self.monstros, x, 412) 
            self.lista_de_monstros.append(self.monstro)

        self.lista_de_gorilas = []
        for i in range(1):
            gorilas = Gorila(self.sprites,self.gorilas, 690, 250, 'direita') 
            self.lista_de_gorilas.append(gorilas)

        self.lista_passaros = []
        for i in range(2):
            x = randint(200,800)
            y = randint(31,81)
            passaro = Passaro(self.sprites,self.passaro, x, y,self.jogador,self.lista_passaros) 
            self.lista_de_gorilas.append(passaro)

        img_tiro = pygame.image.load('bola.png')
        self.tiro = pygame.transform.scale(img_tiro,(15,15))

        self.contador = 0
    
    def gera_mapa(self):
        
        #criando o chao
        for i in range(30):
            x = 32*i
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,x, 480, 'grass')

        gera_plataforma(self,4,'x',100,410)
        gera_plataforma(self,4,'x',210,350)
        gera_plataforma(self,6,'x',320,290)
        gera_plataforma(self,8,'x',100,190)
        Estrela(self.sprites,self.estrela, 140, 155)
        Coracao(self.sprites, self.coracao, 200, 152)
        
        gera_plataforma(self,3,'x',500,250)

        gera_plataforma(self,12,'x',650,200)
        gera_plataforma(self,12,'x',650,50)
        gera_plataforma(self,20,'x',550,350)
        gera_plataforma(self,7,'y',200,890)
        Estrela(self.sprites,self.estrela, 800, 315)

        x = 0
        for i in range(5):
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,663, 179 - x, 'sand')
            x += 25
        x = 0
        for i in range(5):
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,878, 179 - x, 'sand')
            x += 25
        x = 0
        for i in range(5):
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,854, 179 - x, 'sand')
            x += 25
        x = 0
        for i in range(5):
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,830, 179 - x, 'sand')
            x += 25
        Pocao(self.sprites, self.pocao, 690, 160)
        Pocao(self.sprites, self.pocao, 750, 160)
        Coracao(self.sprites, self.coracao, 705, 165)
        Coracao(self.sprites, self.coracao, 730, 165)
        Pocao(self.sprites, self.pocao, 720, 160)
        Coracao(self.sprites, self.coracao, 770, 165)
        Pocao(self.sprites, self.pocao, 780, 160)

    def recebe_eventos(self):

        velocidade_x = 3

        clock = pygame.time.Clock()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            
            #caso o botao seja apertado, ele soma a velocidade ate parar de apertar 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.jogador.speedx = velocidade_x
                assets["esquerda"] = False #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.jogador.speedx = 0
                print(self.jogador.speedx)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.jogador.speedx = -velocidade_x
                assets["esquerda"] = True #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.jogador.speedx = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.jogador.jump()
            if event.type==pygame.KEYDOWN and event.key == pygame.K_e:
                assets["tiro"] -= 1
                if assets["tiro"] >= 0:
                    Tiro(self.sprites, self.monstros, self.plataforma,self.plataformas_quebraveis,self.gorilas, self.passaro, self.jogador.rect.x, self.jogador.rect.y+25)
            if self.jogador.rect.x > 850 and assets["estrela"] == 2:
                return Tela3_1(self.window)
            if assets["vidas"] <= 0:
                return GameOver(self.window)

            if event.type==pygame.KEYDOWN: #movimentacao dos monstros 
                Telas.movimenta_monstro(self,self.limita_monstros_x)
            #self.aparece_text_box = False 

        ultimo_tempo = self.last_updated 
        tempo = pygame.time.get_ticks()
        delta_t = (tempo-ultimo_tempo)/1000
        self.last_updated = tempo
        self.sprites.update(delta_t)

        clock.tick(120)

        return self

    def desenha(self,window):
                
        #pre-sets de desenho de todas as telas
        Telas.desenha(self,window)

        #desenhando a vida do usuario 
        for i in range(assets["vidas"]):
            window.blit(self.img_coracao,(i*20,0))
        
        for i in range(assets["tiro"]):
            if i<10:
                window.blit(self.tiro,(i*14 + 770,0))
            if i < 20 and i >= 10:
                window.blit(self.tiro,(i*14-70+700,13))
            if i < 30 and i>=20:
                window.blit(self.tiro,(i*14-140+630,26))
            if i < 40 and i>=30:
                window.blit(self.tiro,(i*14-210+560,39))

        self.sprites.draw(self.window)

class Tela3_1:
    
    def __init__(self, window):
        #criando o fund0
        fundo = pygame.image.load(assets["fundo3"]) #imagem gerdada pela AI "https://www.scenario.com/""
        self.fundo = pygame.transform.scale(fundo, (912,512))

        #pre-stes de todas as telas 
        Telas.__init__(self,window)

        #gerando as plataformas dos mapas 
        self.gera_mapa()

        self.lista_passaros = []
        for i in range(6):
            x = randint(200,800)
            y = randint(31,81)
            passaro = Passaro(self.sprites,self.passaro, x, y,self.jogador,self.lista_passaros) 
            self.lista_passaros.append(passaro)

        img_tiro = pygame.image.load('bola.png')
        self.tiro = pygame.transform.scale(img_tiro,(15,15))
        self.contador = 0

        #npc para dar as instrucoes do final do jogo 
        sanji = pygame.image.load(assets["sanji"])
        sanji_certo = pygame.transform.smoothscale(sanji,(90,110))
        self.sanji = pygame.transform.flip(sanji_certo, True, False)
        text_box4 = pygame.image.load(assets["text_box4"])
        self.text_box4 = pygame.transform.smoothscale(text_box4,(230,230))
        self.aparece_text_box = False 
    
    def gera_mapa(self):
        
        #criando o chao
        for i in range(30):
            x = 32*i
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,x, 480, 'grass')

    def recebe_eventos(self):

        velocidade_x = 3

        clock = pygame.time.Clock()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            
            #caso o botao seja apertado, ele soma a velocidade ate parar de apertar 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.jogador.speedx = velocidade_x
                assets["esquerda"] = False #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.jogador.speedx = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.jogador.speedx = -velocidade_x
                assets["esquerda"] = True #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.jogador.speedx = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.jogador.jump()
            if event.type==pygame.KEYDOWN and event.key == pygame.K_e:
                assets["tiro"] -= 1
                if assets["tiro"] >= 0:
                    Tiro(self.sprites, self.monstros, self.plataforma,self.plataformas_quebraveis,self.gorilas, self.passaro, self.jogador.rect.x, self.jogador.rect.y+25)
            if self.jogador.rect.x > 850:
                return Tela3_2(self.window)
            if assets["vidas"] <= 0:
                return GameOver(self.window)

            if  50 < self.jogador.rect.x < 400:
                self.aparece_text_box = True  
            if 50 < self.jogador.rect.x > 400:
                self.aparece_text_box = False 

        ultimo_tempo = self.last_updated 
        tempo = pygame.time.get_ticks()
        delta_t = (tempo-ultimo_tempo)/1000
        self.last_updated = tempo
        self.sprites.update(delta_t)

        clock.tick(120)

        return self

    def desenha(self,window):
                
        #pre-sets de desenho de todas as telas
        Telas.desenha(self,window)

        #desenhando a vida do usuario 
        for i in range(assets["vidas"]):
            window.blit(self.img_coracao,(i*20,0))
        
        for i in range(assets["tiro"]):
            if i<10:
                window.blit(self.tiro,(i*14 + 770,0))
            if i < 20 and i >= 10:
                window.blit(self.tiro,(i*14-70+700,13))
            if i < 30 and i>=20:
                window.blit(self.tiro,(i*14-140+630,26))
            if i < 40 and i>=30:
                window.blit(self.tiro,(i*14-210+560,39))

        #desenhando o sanji npc, para instrucoes 
        window.blit(self.sanji,(200,380))
        #desenhando a fala do sanji caso o jogador esteja perto dele 
        if self.aparece_text_box:
            window.blit(self.text_box4,(60,265))    

        self.sprites.draw(self.window)

class Tela3_2:
    
    def __init__(self, window):
        #criando o fund0
        fundo = pygame.image.load(assets["fundo3"]) #imagem gerdada pela AI "https://www.scenario.com/""
        self.fundo = pygame.transform.scale(fundo, (912,512))

        #pre-stes de todas as telas 
        Telas.__init__(self,window)

        #gerando as plataformas dos mapas 
        self.gera_mapa()

        #gerando os monstros no mapa 
        self.limita_monstros_x = [0,100]
        self.lista_de_monstros = []
        for i in range(0):
            x = randint(self.limita_monstros_x[0],self.limita_monstros_x[1])
            self.monstro = Monstro(self.sprites,self.monstros, x, 412) 
            self.lista_de_monstros.append(self.monstro)

        self.lista_de_gorilas = []
        for i in range(1):
            gorilas = Gorila(self.sprites,self.gorilas, 690, 250, 'direita') 
            self.lista_de_gorilas.append(gorilas)

        self.lista_passaros = []
        for i in range(6):
            x = randint(200,800)
            y = randint(31,81)
            passaro = Passaro(self.sprites,self.passaro, x, y,self.jogador,self.lista_passaros) 
            self.lista_de_gorilas.append(passaro)

        img_tiro = pygame.image.load('bola.png')
        self.tiro = pygame.transform.scale(img_tiro,(15,15))
        self.contador = 0

    def gera_mapa(self):
        
        #criando o chao
        for i in range(30):
            x = 32*i
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,x, 480, 'grass')

    def recebe_eventos(self):

        velocidade_x = 3

        clock = pygame.time.Clock()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            
            #caso o botao seja apertado, ele soma a velocidade ate parar de apertar 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.jogador.speedx = velocidade_x
                assets["esquerda"] = False #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.jogador.speedx = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.jogador.speedx = -velocidade_x
                assets["esquerda"] = True #Para o tiro
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.jogador.speedx = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.jogador.jump()
            if event.type==pygame.KEYDOWN and event.key == pygame.K_e:
                assets["tiro"] -= 1
                if assets["tiro"] >= 0:
                    Tiro(self.sprites, self.monstros, self.plataforma,self.plataformas_quebraveis,self.gorilas, self.passaro, self.jogador.rect.x, self.jogador.rect.y+25)
            if self.jogador.rect.x > 850 and assets["estrela"] == 2:
                return Tela3(self.window)
            if assets["vidas"] <= 0:
                return GameOver(self.window)

            if event.type==pygame.KEYDOWN: #movimentacao dos monstros 
                Telas.movimenta_monstro(self,self.limita_monstros_x)
            #self.aparece_text_box = False 

            if  50 < self.jogador.rect.x < 400:
                self.aparece_text_box = True  
            if 50 < self.jogador.rect.x > 400:
                self.aparece_text_box = False 

        ultimo_tempo = self.last_updated 
        tempo = pygame.time.get_ticks()
        delta_t = (tempo-ultimo_tempo)/1000
        self.last_updated = tempo
        self.sprites.update(delta_t)

        clock.tick(120)

        return self

    def desenha(self,window):
                
        #pre-sets de desenho de todas as telas
        Telas.desenha(self,window)

        #desenhando a vida do usuario 
        for i in range(assets["vidas"]):
            window.blit(self.img_coracao,(i*20,0))
        
        for i in range(assets["tiro"]):
            if i<10:
                window.blit(self.tiro,(i*14 + 770,0))
            if i < 20 and i >= 10:
                window.blit(self.tiro,(i*14-70+700,13))
            if i < 30 and i>=20:
                window.blit(self.tiro,(i*14-140+630,26))
            if i < 40 and i>=30:
                window.blit(self.tiro,(i*14-210+560,39))
        
        self.contador+=1
        print(self.contador)
        if self.contador == 120:
            print(2)
            self.contador = 0
            if assets["gorila_vivo"]:
                print(1)
                Tiro_monstro(self.sprites, self.plataforma,self.plataformas_quebraveis,700, 290, self.tiro_monstro,"esquerda")

        self.sprites.draw(self.window)

class Jogador(pygame.sprite.Sprite):
    
    def __init__(self,chao,monstros,estrela, coracao, gorilas, pocao, plataformas_quebraveis,passaro,tiro_banana):

        pygame.init() 
        pygame.sprite.Sprite.__init__(self)

        self.coracao = coracao
        self.monstros = monstros
        self.estrela = estrela
        self.gorilas = gorilas
        self.passaro = passaro
        self.pocao = pocao
        self.tiro_banana = tiro_banana

        self.mario = pygame.image.load("estrela.png")
        self.image = pygame.transform.scale(self.mario, (50,50))

        self.rect = self.image.get_rect()

        self.chao = chao
        self.plataformas_quebraveis = plataformas_quebraveis

        self.speedx = 0
        self.speedy = 0

        self.STILL = 0
        self.JUMPING = 1
        self.FALLING = 2
        self.GRAVITY = 1
        self.JUMP_SIZE = 15

        self.WIDTH = 912 
        self.HEIGHT = 512

        self.lista_jogador = []
        imagem = pygame.image.load("pngwing.com (1).png")
        self.lista_jogador = load_spritesheet(imagem,1,8)

        imagem = pygame.image.load("parado.png")
        self.lista_jogador_parado = load_spritesheet(imagem,1,2)

        imagem = pygame.image.load("pulando.png")
        self.lista_jogador_pulando = load_spritesheet(imagem,1,6)

        self.state = "parado"
        self.contador = 0
        self.last_updated = 0
        self.elapsed_ticks = 0

        self.flag = True

    def update(self, delta_t):
        
        self.speedy += self.GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = self.FALLING
        # Atualiza a posição y
        self.rect.y += self.speedy
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.chao, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = self.STILL
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = self.STILL

        # Tenta andar em x
        self.rect.x += self.speedx
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= self.WIDTH:
            self.rect.right = self.WIDTH - 1
        collisions = pygame.sprite.spritecollide(self, self.chao, False)
        for collision in collisions:
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            elif self.speedx < 0:
                self.rect.left = collision.rect.right

        collisions1 = pygame.sprite.spritecollide(self, self.plataformas_quebraveis, False)
        for collision in collisions1:
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            elif self.speedx < 0:
                self.rect.left = collision.rect.right

        collisions = pygame.sprite.spritecollide(self, self.monstros, True)
        for cada_colisao in collisions:
            assets["vidas"]-=1

        collisions = pygame.sprite.spritecollide(self, self.estrela, True)
        for cada_colisao in collisions:
            assets["estrela"] += 1

        collisions = pygame.sprite.spritecollide(self, self.coracao, True)
        for cada_colisao in collisions:
            if assets["vidas"] < 5:
                assets["vidas"] += 1

        collisions = pygame.sprite.spritecollide(self, self.tiro_banana, True)
        for cada_colisao in collisions:
            assets["vidas"] -= 1
        
        
        collisions = pygame.sprite.spritecollide(self, self.passaro, True)
        for cada_colisao in collisions:
            assets["vidas"] -= 1

        collisions = pygame.sprite.spritecollide(self, self.pocao, True)
        for cada_colisao in collisions:
            if assets["tiro"] <= 35:
                assets["tiro"] += 5
            if assets["tiro"]>35 and assets["tiro"]<40:
                assets["tiro"] = 40

        self.elapsed_ticks += delta_t
        if self.speedx != 0:
            if self.elapsed_ticks > 0.1:
                self.contador += 1
                self.elapsed_ticks = 0
            if self.contador >= len(self.lista_jogador):
                self.contador = 0
            imagem = self.lista_jogador[self.contador]
            imagem_virada = pygame.transform.flip(imagem, True, False)
            if self.speedx < 0:
                self.image = pygame.transform.scale(imagem_virada,(65,50))
            else:
                self.image= pygame.transform.scale(imagem,(65,50))
        if self.speedx == 0:
            if self.rect.y>480:
                self.rect.y = 447
            if self.elapsed_ticks > 0.8:
                self.contador += 1
                self.elapsed_ticks = 0
            if self.contador >= len(self.lista_jogador_parado):
                self.contador = 0
            imagem = self.lista_jogador_parado[self.contador]
            self.image = pygame.transform.smoothscale(imagem, (47,39))
        if self.speedy != 0:
            if self.elapsed_ticks > 0.4:
                self.contador += 1
                self.elapsed_ticks = 0
            if self.contador >= len(self.lista_jogador_pulando):
                self.contador = 0
            imagem = self.lista_jogador_pulando[self.contador]
            imagem_virada = pygame.transform.flip(imagem, True, False)
            if self.speedx < 0:
                self.image = pygame.transform.scale(imagem_virada,(65,50))
            else:
                self.image= pygame.transform.scale(imagem,(65,50))
        
        if self.speedx == 0 and self.speedy == 0:
            self.rect.y += 13

    def jump(self):
    # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == self.STILL:
            self.speedy -= self.JUMP_SIZE
            self.state = self.JUMPING

class Jogo:
    
    def __init__(self):
        
        pygame.init()
        self.sprites = pygame.sprite.Group()

        self.window = pygame.display.set_mode((912,512))

        self.tela_atual = TelaInicial(self.window)
        self.last_updated = pygame.time.get_ticks()

    def recebe_eventos(self):
        
        self.tela_atual = self.tela_atual.recebe_eventos()
        # recebe_eventos tela atual
        if self.tela_atual is None:
            return False
        return True

    def game_loop(self):
        
        while self.recebe_eventos():
            self.tela_atual.desenha(self.window)
            pygame.display.update()

    def finaliza(self):
        pygame.quit()

if __name__ == '__main__':
    jogo = Jogo()
    jogo.game_loop()
    jogo.finaliza()


