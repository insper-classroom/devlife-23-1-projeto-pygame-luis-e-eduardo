from random import randint
import pygame
from assets import *
#Comentários
#A função load_spritesheet server para "recortar um png com os frames do movimento do jogador e nós pegamos essa função do snippets do github"
#Para fazer o pulo do jogador, nos tambem nos baseamos no algoritimo do snippets

def gera_plataforma(self,quantidade_blocos,eixo,inicio,outro_eixo):
        if eixo == 'x':   
            x = 0
            for i in range(quantidade_blocos):
                Plataform(self.sprites,self.plataforma,inicio + x, outro_eixo, 'bloco')
                x += 24 
        if eixo == 'y':
            x = 0
            for i in range(quantidade_blocos):
                Plataform(self.sprites,self.plataforma,outro_eixo, inicio - x, 'bloco')
                x += 24 

def load_spritesheet(spritesheet, rows, columns):
    # Calcula a largura e altura de cada sprite.
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    
    # Percorre todos os sprites adicionando em uma lista.
    sprites = []
    for row in range(rows):
        for column in range(columns):
            # Calcula posição do sprite atual
            x = column * sprite_width
            y = row * sprite_height
            # Define o retângulo que contém o sprite atual
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)

            # Cria uma imagem vazia do tamanho do sprite
            image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            # Copia o sprite atual (do spritesheet) na imagem
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
    return sprites

def musica(musica):
    pygame.mixer.music.load(musica)
    pygame.mixer.music.set_endevent(pygame.USEREVENT) #para reniciar a musica caso acabar
    pygame.mixer.music.play() 

class Plataform(pygame.sprite.Sprite):
    def __init__(self,sprites,plataforma,x,y,tipo):
        self.plataforma = plataforma
        self.tipo = tipo 
        pygame.sprite.Sprite.__init__(self)
        if self.tipo == 'grass':
            img_plataforma = pygame.image.load("grass.png")
            self.image = pygame.transform.scale(img_plataforma, (50,15))
        if self.tipo == 'bloco':
            img_plataforma = pygame.image.load("bloco1.png")
            self.image = pygame.transform.scale(img_plataforma, (50,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.plataforma.add(self)

class Estrela(pygame.sprite.Sprite):
    def __init__(self,sprites,estrela,x,y):
        self.estrela = estrela
        pygame.sprite.Sprite.__init__(self)
        img_estrela = pygame.image.load("estrela.png")
        self.image = pygame.transform.scale(img_estrela, (35,35))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.estrela.add(self)

class Coracao(pygame.sprite.Sprite):
    def __init__(self,sprites,coracao,x,y):
        self.coracao = coracao
        pygame.sprite.Sprite.__init__(self)
        img_coracao = pygame.image.load("coracao.png")
        self.image = pygame.transform.scale(img_coracao, (25,25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.coracao.add(self)

class Monstro(pygame.sprite.Sprite):      
    def __init__(self,sprites,monstros,x,y):
        self.monstros = monstros
        pygame.sprite.Sprite.__init__(self)
        if assets["posicao_monstro"] == 'esquerda':
            img_monstro = pygame.image.load(assets["monstro_img"])  
        elif assets["posicao_monstro"] == 'direita':
            img_monstro1 = pygame.image.load(assets["monstro_img"])
            img_monstro = pygame.transform.flip(img_monstro1, True, False)
        self.image = pygame.transform.scale(img_monstro, (40,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.monstros.add(self)

class Planta(pygame.sprite.Sprite):      
    def __init__(self,sprites,monstros,x,y):
        self.monstros = monstros
        pygame.sprite.Sprite.__init__(self)
        if assets["posicao_monstro"] == 'esquerda':
            img_monstro = pygame.image.load(assets["monstro_img"])  
        elif assets["posicao_monstro"] == 'direita':
            img_monstro1 = pygame.image.load(assets["monstro_img"])
            img_monstro = pygame.transform.flip(img_monstro1, True, False)
        self.image = pygame.transform.scale(img_monstro, (40,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.monstros.add(self)

class Tiro(pygame.sprite.Sprite):
    def __init__(self, sprites,monstros,plataforma, x, y):
        pygame.sprite.Sprite.__init__(self)

        img_laser = pygame.image.load('bola.png')
        self.image = pygame.transform.scale(img_laser,(15,15))
        
        self.rect = self.image.get_rect()
        self.vel_y_laser = 0
        self.rect.x = x
        self.rect.y = y - 10
        if assets["esquerda"]:
            self.vel_x_laser = -500
        else:
            self.vel_x_laser = +500

        self.flag_tiro = False
        self.monstros = monstros
        self.plataforma = plataforma
        sprites.add(self) 
        self.sprites = sprites 
    
    def update(self, delta_t):
        
            self.rect.x = (self.rect.x + self.vel_x_laser*delta_t)
            lista = pygame.sprite.spritecollide(self, self.monstros,True)
            for tiro in lista:
                self.sprites.remove(self)
            if self.rect.x > 912 or self.rect.x < 0:
                self.kill()
            lista_plataformas = pygame.sprite.spritecollide(self, self.plataforma,False)
            for tiro in lista_plataformas:   
                self.kill()
            
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
                        return Tela2_1(self.window)
                        
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
        fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(fonte_padrao, 24)
        
        self.vidas = 5
        img_coracao = pygame.image.load("coracao.png")
        self.img_coracao = pygame.transform.scale(img_coracao, (25,25))

        self.last_updated = 0

        setas = pygame.image.load("setas.png")
        self.setas = pygame.transform.scale(setas,(200,120))
        
        chao = pygame.image.load("grass.png")
        self.chao = pygame.transform.scale(chao,(50,15))
        self.plataforma = pygame.sprite.Group()
        self.monstros = pygame.sprite.Group()
        self.estrela = pygame.sprite.Group()
        self.coracao = pygame.sprite.Group()
        self.jogador = Jogador(self.plataforma,self.monstros,self.estrela, self.coracao)
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
            Plataform(self.sprites,self.plataforma,x, 480, 'grass')

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
            Plataform(self.sprites,self.plataforma,x, 480, 'grass')

        x = 0
        for i in range(4):
            x += 24
            Plataform(self.sprites,self.plataforma,250 + x, 430, 'bloco')

        x = 0
        for i in range(4):
            x += 24
            Plataform(self.sprites,self.plataforma,390 + x, 400, 'bloco')

        x = 0
        for i in range(4):
            x += 24
            Plataform(self.sprites,self.plataforma,530 + x, 430, 'bloco')

        x = 0
        for i in range(4):
            Plataform(self.sprites,self.plataforma,750, 452 - x, 'bloco')
            x += 25
        
        Plataform(self.sprites,self.plataforma,726, 377, 'bloco')
        Plataform(self.sprites,self.plataforma,774, 377, 'bloco')

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
        
class Tela1_2:
    
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
            Plataform(self.sprites,self.plataforma,x, 480, 'grass')

        diferenca_entre_blocos_y = 25
        #colocar bloco no chao, y = 452
        
        #criando as plataformas 
        Plataform(self.sprites,self.plataforma,300, 452, 'bloco')
        Plataform(self.sprites,self.plataforma,300, 452 - diferenca_entre_blocos_y, 'bloco')

        Plataform(self.sprites,self.plataforma,800, 452, 'bloco')
        Plataform(self.sprites,self.plataforma,800, 452 - diferenca_entre_blocos_y, 'bloco')

        x = 0
        for i in range(10):
            x += 24
            Plataform(self.sprites,self.plataforma,410 + x, 390, 'bloco')

        x = 0
        for i in range(6):
            Plataform(self.sprites,self.plataforma,600 + x, 300, 'bloco')
            x += 24
        
        x = 0
        for i in range(6):
            Plataform(self.sprites,self.plataforma,400 + x, 210, 'bloco')
            x += 24

        x = 0
        for i in range(6):
            Plataform(self.sprites,self.plataforma,180 + x, 260, 'bloco')
            x += 24
        
        x = 0
        for i in range(3):
            Plataform(self.sprites,self.plataforma,50 + x, 180, 'bloco')
            x += 24

        Estrela(self.sprites,self.estrela, 84, 140)
        Coracao(self.sprites, self.coracao, 410, 140)
        Coracao(self.sprites, self.coracao, 700, 200)


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
                    Tiro(self.sprites, self.monstros, self.jogador.rect.x, self.jogador.rect.y+25)

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
    
    def gera_mapa(self):
        
        #criando o chao
        for i in range(30):
            x = 32*i
            Plataform(self.sprites,self.plataforma,x, 480, 'grass')

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
                    Tiro(self.sprites, self.monstros,self.plataforma, self.jogador.rect.x, self.jogador.rect.y+25)
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
            self.monstro = Monstro(self.sprites,self.monstros, x, 412) 
            self.lista_de_monstros.append(self.monstro)
    
    def gera_mapa(self):
        
        #criando o chao
        for i in range(30):
            x = 32*i
            Plataform(self.sprites,self.plataforma,x, 480, 'grass')

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
                    Tiro(self.sprites, self.monstros, self.plataforma,self.jogador.rect.x, self.jogador.rect.y+25)
            if self.jogador.rect.x > 850 and assets["estrela"] == 3:
                return Tela3(self.window)
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

        self.sprites.draw(self.window)

class Jogador(pygame.sprite.Sprite):
    
    def __init__(self,chao,monstros,estrela, coracao):

        pygame.init() 
        pygame.sprite.Sprite.__init__(self)

        self.coracao = coracao
        self.monstros = monstros
        self.estrela = estrela

        self.mario = pygame.image.load("personagem_principal.png")
        self.image = pygame.transform.scale(self.mario, (50,50))

        self.rect = self.image.get_rect()

        self.chao = chao

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
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.chao, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            # Estava indo para a esquerda
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