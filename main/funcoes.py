from random import randint
import pygame
from assets import *

import time

def escreve(texto, window,y):
    delay = 10 # tempo de atraso em milissegundos
    x = 0 # posição inicial da letra na tela
    y = y
    fonte = pygame.font.get_default_font()
    fonte = pygame.font.Font(fonte, 12)
    clock = pygame.time.Clock()

    for letra in texto:
        img_mensagem = fonte.render(letra, True, (255, 255, 255))
        imagem_letra = pygame.transform.smoothscale(img_mensagem, (10, 12))
        
        window.blit(imagem_letra, (x, y))
        pygame.display.update() # atualiza a tela
        pygame.time.wait(delay) # atraso entre as letras
        x += imagem_letra.get_width() # atualiza a posição da letra

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

class Plataform(pygame.sprite.Sprite):
    def __init__(self,sprites,plataforma,x,y):
        self.plataforma = plataforma
        pygame.sprite.Sprite.__init__(self)
        img_plataforma = pygame.image.load("grass.png")
        self.image = pygame.transform.scale(img_plataforma, (50,15))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.plataforma.add(self)

class Moeda(pygame.sprite.Sprite):
    def __init__(self,sprites,moeda,x,y):
        self.moeda = moeda
        pygame.sprite.Sprite.__init__(self)
        img_moeda = pygame.image.load("moeda-removebg-preview.png")
        self.image = pygame.transform.scale(img_moeda, (40,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.moeda.add(self)

class Monstro(pygame.sprite.Sprite):      
    def __init__(self,sprites,monstros,x,y):
        self.monstros = monstros
        pygame.sprite.Sprite.__init__(self)
        img_monstro = pygame.image.load(assets["monstro_img"])
        self.image = pygame.transform.scale(img_monstro, (40,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.monstros.add(self)

class Tiro(pygame.sprite.Sprite):
    def __init__(self, sprites,monstros, x, y):
        pygame.sprite.Sprite.__init__(self)

        img_laser = pygame.image.load('machado.png')
        self.image = pygame.transform.scale(img_laser,(20,20))
        
        self.rect = self.image.get_rect()
        self.vel_y_laser = 0

        self.rect.x = x
        self.rect.y = y
        if assets["esquerda"]:
            self.vel_x_laser = -500
        else:
            self.vel_x_laser = +500

        self.flag_tiro = False
        self.monstros = monstros
        sprites.add(self) 
        self.sprites = sprites 
    
    def update(self, delta_t):
        
        self.rect.x = (self.rect.x + self.vel_x_laser*delta_t)
        lista = pygame.sprite.spritecollide(self, self.monstros,True)
        for tiro in lista:
            self.sprites.remove(self)
        if self.rect.x > 912 or self.rect.x < 0:
            self.kill()

class TelaInicial:
    def __init__(self, window):
        fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(fonte_padrao, 24)
        self.window = window
        imagem = pygame.image.load("tela_inicial.jpg")
        self.image = pygame.transform.scale(imagem,(912,512))

        # imagem = pygame.image.load("pap-removebg-preview.png")
        # self.lista_load = load_spritesheet(imagem,3,4)
        
        # self.contador = 0
        # self.last_updated = 0
        # self.elapsed_ticks = 0


    def recebe_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None 
            elif evento.type == pygame.KEYDOWN: #nao pode apertar as teclas de andar nao sei pq kkkk
                return Tela1(self.window)
        return self

    def desenha(self, window):
        window.fill((0, 0, 0))
        largura = 200
        altura = 70
        diferenca_largura = (912 - largura)/2
        window.blit(self.image,(0,0))
        pygame.draw.polygon(window,(235,180,51),[(diferenca_largura,400),(912 - diferenca_largura,400),(912 - diferenca_largura,470),(diferenca_largura,470)])
        pygame.draw.circle(window,(235,180,51),(diferenca_largura, 435), 35)
        pygame.draw.circle(window,(235,180,51),(912-diferenca_largura, 435), 35)
        img_mensagem = self.fonte.render("Jogar", True,(255,255,255))
        mensagem = pygame.transform.scale(img_mensagem, (150,60))
        window.blit(mensagem,(diferenca_largura+20, 400))

class Tela1:
    def __init__(self, window):
        self.window = window
        #self.width = pygame.get_width(window)
        self.sprites = pygame.sprite.Group()
        self.plataform = pygame.sprite.Group()
        fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(fonte_padrao, 24)
        self.azul = (0,0,255)
        self.vermelho = (255, 0, 0)
        self.verde = (0,255,0)
        
        self.vidas = 3
        coracao = pygame.image.load("coracao.png")
        self.coracao = pygame.transform.scale(coracao, (15,15))

        self.last_updated = 0

        fundo = pygame.image.load(assets["fundo1"]) #imagem gerdada pela AI "https://www.scenario.com/""
        self.fundo = pygame.transform.scale(fundo, (912,512))

        setas = pygame.image.load("setas.png")
        self.setas = pygame.transform.scale(setas,(200,120))
        
        #criando o chao 
        chao = pygame.image.load("terra.png")
        self.chao = pygame.transform.scale(chao,(250,90))
        self.plataforma = pygame.sprite.Group()
        self.monstros = pygame.sprite.Group()
        self.moeda = pygame.sprite.Group()
        self.jogador = Jogador(self.plataforma,self.monstros,self.moeda)
        self.sprites.add(self.jogador)
        self.scroll = 0 
        luffy = pygame.image.load("Meu projeto.png")
        self.luffy = pygame.transform.smoothscale(luffy,(70,80))
        
        self.window = window

        for i in range(30):
            x = 32*i
            Plataform(self.sprites,self.plataforma,x, 480)

        Moeda(self.sprites,self.moeda, 200, 440)

        assets["texto"] = True
        
        self.lista_de_monstros = []
        for i in range(3):
            x = randint(0,912)
            self.monstro = Monstro(self.sprites,self.monstros, x, 450) 
            self.lista_de_monstros.append(self.monstro) 
    
    def movimenta_monstro(self):
        for monstro in self.lista_de_monstros:    
            num_aleatorio1 = randint(0,1)
            if 10 < monstro.rect.x < 900:
                if num_aleatorio1 > 0.5:
                    monstro.rect.x += 10 #direita 
                else:
                    monstro.rect.x -= 10 #esquerda
            elif monstro.rect.x >= 900:
                monstro.rect.x -= 10 #esquerda
            elif monstro.rect.x <= 10:
                monstro.rect.x += 10 #direita 
 
    def recebe_eventos(self):
        
        velocidade_x = 3

        clock = pygame.time.Clock()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            
            #caso o botao seja apertado, ele soma a velocidade ate parar de apertar 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.jogador.speedx += velocidade_x
                assets["esquerda"] = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.jogador.speedx -= velocidade_x
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.jogador.speedx -= velocidade_x
                assets["esquerda"] = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.jogador.speedx += velocidade_x
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.jogador.jump()
            if event.type==pygame.KEYDOWN and event.key == pygame.K_e:
                Tiro(self.sprites, self.monstros, self.jogador.rect.x, self.jogador.rect.y+25)
            if self.jogador.rect.x > 850 and assets["moeda"] == 1:
                return Tela2(self.window)
        
            #movimentacao dos monstros 
            if event.type==pygame.KEYDOWN:
                Tela1.movimenta_monstro(self)
        
        ultimo_tempo = self.last_updated 
        tempo = pygame.time.get_ticks()
        delta_t = (tempo-ultimo_tempo)/1000
        self.last_updated = tempo
        self.sprites.update(delta_t)

        clock.tick(120)

        return self

    def desenha(self, window):

        #window.fill(self.verde)
        window.blit(self.fundo,(0,0)) #colocando o fundo do jogo
        #pygame.draw.rect(window,(150,75,0),self.chao) #desenhando o chao 
        for i in range(assets["vidas"]):
            window.blit(self.coracao,(i*15,0))
        window.blit(self.chao,(0,490))
        window.blit(self.chao,(200,490))
        window.blit(self.chao,(400,490))
        window.blit(self.chao,(600,490))
        window.blit(self.chao,(800,490))
        
        #desenhando o luffy npc
        window.blit(self.luffy,(100,380))

        if assets["texto"]:
            escreve("utilize as setas para se mover", self.window,20)
            escreve("e a barra de espaço para pular", self.window,40)
            assets["texto"] = False

        texto = "utilize as setas para se mover"
        texto2 = "e a barra de espaço para pular"
        img_mensagem = self.fonte.render(texto, True,(255,255,255))
        mensagem = pygame.transform.scale(img_mensagem, (20*len(texto),25))
        window.blit(mensagem,(0, 20))

        img_mensagem = self.fonte.render(texto2, True,(255,255,255))
        mensagem = pygame.transform.scale(img_mensagem, (20*len(texto),25))
        window.blit(mensagem,(0, 40))
        
        window.blit(self.setas,(0,100))
        self.sprites.draw(self.window)
        
class Tela2:
    
    def __init__(self, window):
        
        self.sprites = pygame.sprite.Group()
        self.plataform = pygame.sprite.Group()
        fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(fonte_padrao, 24)
        self.azul = (0,0,255)
        self.vermelho = (255, 0, 0)
        self.verde = (0,255,0)
        
        self.vidas = 3

        self.plataforma = pygame.sprite.Group()
        self.monstros = pygame.sprite.Group()
        self.moeda = pygame.sprite.Group()
        self.jogador = Jogador(self.plataforma,self.monstros,self.moeda)
        self.sprites.add(self.jogador)

        self.window = window

        self.gera_mapa() 

        self.contador = 60
        self.contagem = 0
        
    def recebe_eventos(self):
        
        velocidade_x = 3

        clock = pygame.time.Clock()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            
            #caso o botao seja apertado, ele soma a velocidade ate parar de apertar 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.jogador.speedx += velocidade_x
                assets["esquerda"] = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.jogador.speedx -= velocidade_x
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.jogador.speedx -= velocidade_x
                assets["esquerda"] = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.jogador.speedx += velocidade_x
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.jogador.jump()
            if event.type==pygame.KEYDOWN and event.key == pygame.K_e:
                Tiro(self.sprites, self.monstros, self.jogador.rect.x, self.jogador.rect.y+25)
            if self.jogador.rect.x>=850 and assets["moeda"] == 5:
                return Tela1(self.window)
        
            #movimentacao dos monstros 
            if event.type==pygame.KEYDOWN:
                Tela1.movimenta_monstro(self)
        
        ultimo_tempo = self.last_updated 
        tempo = pygame.time.get_ticks()
        delta_t = (tempo-ultimo_tempo)/1000
        self.last_updated = tempo
        self.sprites.update(delta_t)
        clock.tick(120)

        return self

    def desenha(self, window):
        window.blit(self.fundo2,(0,0)) #colocando o fundo do jogo
        for i in range(assets["vidas"]):
            window.blit(self.coracao,(i*15,0))
        window.blit(self.chao,(0,490))
        window.blit(self.chao,(200,490))
        window.blit(self.chao,(400,490))
        window.blit(self.chao,(600,490))
        window.blit(self.chao,(800,490))

        numero = str(self.contador)
        img_mensagem = self.fonte.render(numero, True,(255,255,255))
        mensagem = pygame.transform.scale(img_mensagem, (30,30))
        window.blit(mensagem,(850,3))
        self.contagem+=1
        if self.contagem == 120:
            self.contador-=1
            self.contagem = 0

        img_mensagem = self.fonte.render("Tempo restante:", True,(255,255,255))
        mensagem = pygame.transform.scale(img_mensagem, (280,25))
        window.blit(mensagem,(850-295, 5))
    
        self.sprites.draw(self.window)
    
    def gera_mapa(self):
        coracao = pygame.image.load("coracao.png")
        self.coracao = pygame.transform.scale(coracao, (15,15))

        self.last_updated = 0

        fundo = pygame.image.load("fundo2.png") #imagem gerdada pela AI "https://www.scenario.com/""
        self.fundo2 = pygame.transform.scale(fundo, (1200,512))

        chao = pygame.image.load("terra.png")
        self.chao = pygame.transform.scale(chao,(200,130))
        
        Plataform(self.sprites,self.plataforma,350,335)
        Plataform(self.sprites,self.plataforma,200,400)
        Plataform(self.sprites,self.plataforma,500,280)
        Plataform(self.sprites,self.plataforma,680,210)
        
        Plataform(self.sprites,self.plataforma,650,210)
        Plataform(self.sprites,self.plataforma,700,210)
        Plataform(self.sprites,self.plataforma,730,210)
        Plataform(self.sprites,self.plataforma,750,210)

        Plataform(self.sprites,self.plataforma,650,300)
        Plataform(self.sprites,self.plataforma,700,300)

        for i in range(30):
            x = 32*i
            Plataform(self.sprites,self.plataforma,x, 480)

        Moeda(self.sprites,self.moeda, 350, 290)
        Moeda(self.sprites,self.moeda, 500, 240)
        Moeda(self.sprites,self.moeda, 680, 260)
        Moeda(self.sprites,self.moeda, 780, 140)
        
        self.lista_de_monstros = []
        for i in range(3):
            x = randint(0,912)
            self.monstro = Monstro(self.sprites,self.monstros, x, 450) 
            self.lista_de_monstros.append(self.monstro)

class Jogador(pygame.sprite.Sprite):
    
    def __init__(self,chao,monstros,moeda):

        pygame.init() 
        pygame.sprite.Sprite.__init__(self)


        self.monstros = monstros
        self.moeda = moeda

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

        collisions = pygame.sprite.spritecollide(self, self.moeda, True)
        for cada_colisao in collisions:
            assets["moeda"] +=1

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
            if self.elapsed_ticks > 0.8:
                self.contador += 1
                self.elapsed_ticks = 0
            if self.contador >= len(self.lista_jogador_parado):
                self.contador = 0
            imagem = self.lista_jogador_parado[self.contador]
            self.image = pygame.transform.scale(imagem, (49,52))
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