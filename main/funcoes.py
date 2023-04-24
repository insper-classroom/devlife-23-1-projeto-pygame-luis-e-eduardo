from random import randint
import pygame
from assets import *

def esta_no_chao(obj1,obj2):
    if obj1.colliderect(obj2):
        return True 
    else:
        return False 

class Plataform(pygame.sprite.Sprite):
    
    def __init__(self,sprites,x,y):
        pygame.sprite.Sprite.__init__(self)

        #img_plataforma = pygame.image.load("main/grass.png")
        #self.image = pygame.transform.scale(img_plataforma, assets["bloco"])
        #self.rect = self.image.get_rect()
        
        #self.rect.x = x
        #self.rect.y = y
        #sprites.add(self)

        self.plataforma = pygame.sprite.Group()
        img_plataforma = pygame.image.load("main/assets/imagens/ground.png")
        self.image = pygame.transform.scale(img_plataforma, assets["bloco"])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.plataforma.add(self)

class TelaInicial:
    def __init__(self, window):
        fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(fonte_padrao, 24)
        self.window = window

    def recebe_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None 
            elif evento.type == pygame.KEYDOWN: #nao pode apertar as teclas de andar nao sei pq kkkk
                return Tela1(self.window)
        return self

    def desenha(self, window):
        window.fill((0, 0, 0))
        img_mensagem = self.fonte.render("Aperte uma tecla para continuar", True,(255,255,255))
        mensagem = pygame.transform.scale(img_mensagem, (400,90))
        window.blit(mensagem,(150, 216))
        

class Tela1:
    def __init__(self, window):
        
        self.sprites = pygame.sprite.Group()
        self.plataform = pygame.sprite.Group()
        fonte_padrao = pygame.font.get_default_font()
        self.font = pygame.font.Font(fonte_padrao, 24)
        self.azul = (0,0,255)
        self.vermelho = (255, 0, 0)
        self.verde = (0,255,0)
        
        fundo = pygame.image.load("main/assets/imagens/fundo1.png") #imagem gerdada pela AI "https://www.scenario.com/""
        self.fundo = pygame.transform.scale(fundo, (912,512))
        
        #criando o chao 
        chao = pygame.image.load("main/assets/imagens/grass_agora.png")
        self.chao = pygame.transform.scale(chao,(200,130))
        #self.chao = pygame.Rect(0,450,912,112) #chao provisório, coords certas 

        self.jogador = Jogador()
        self.sprites.add(self.jogador)

        #for i in range(30):
            #x = 32*i
            #y = assets["altura_tela"] - 71
            #Plataform(self.sprites,x,y)
        for i in range(6):
            x = 300 + 32*i
            y = assets["altura_tela"] - 6*assets["bloco"][1] 
            Plataform(self.sprites,x,y)
        for i in range(4):
            x = 600 + 32*i
            y = assets["altura_tela"] - 5*assets["bloco"][1]
            Plataform(self.sprites,x,y)
            

        self.window = window


   
    def recebe_eventos(self):
        
        velocidade_x = 1
        velocidade_y = 8

        clock = pygame.time.Clock()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return Tela2()
            
            #caso o botao seja apertado, ele soma a velocidade ate parar de apertar 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.jogador.vel_x += velocidade_x
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.jogador.vel_x -= velocidade_x
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.jogador.vel_x -= velocidade_x
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.jogador.vel_x += velocidade_x
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if self.jogador.vel_y == 0:
                    self.jogador.vel_y -= velocidade_y
                else:
                    self.jogador.vel_y == 0
                    
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                self.jogador.vel_y += velocidade_y



        self.sprites.update()
        
        clock.tick(60) #definindo um fps max para todos os usuarios

        self.sprites.update()
        clock.tick(120)

        return self

    def desenha(self, window):

        #window.fill(self.verde)
        window.blit(self.fundo,(0,0)) #colocando o fundo do jogo
        #pygame.draw.rect(window,(150,75,0),self.chao) #desenhando o chao 
        window.blit(self.chao,(0,390))
        window.blit(self.chao,(200,390))
        window.blit(self.chao,(400,390))
        window.blit(self.chao,(600,390))
        window.blit(self.chao,(800,390))

        self.sprites.draw(self.window)
        
class Tela2:
    
    def __init__(self):
        default_font_name = pygame.font.get_default_font()
        self.font = pygame.font.Font(default_font_name, 24)
        self.cor = (0, 0, 255)
        
    def recebe_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return Tela1()
        return self

    def desenha(self, window):
        window.fill(self.cor)
       
class Jogador(pygame.sprite.Sprite):
    
    def __init__(self):

        pygame.init() 
        pygame.sprite.Sprite.__init__(self)

        mario = pygame.image.load("main/assets/imagens/personagem_principal.png")
        self.image = pygame.transform.scale(mario, (50,50))

        self.rect = self.image.get_rect()

        #posicao do jogador 

        self.rect.x = 0
        self.rect.y = 400 

        self.vel_x = 0
        self.vel_y = 0

        # self.rect.x = float(state["posicao_jogador"][0])
        # self.rect.y = float(state["posicao_jogador"][1]) 

        #velocidade jogador 

    def update(self):

        
        if self.rect.x < 862:
            self.rect.x = abs(self.rect.x + state["velocidade_jogador"][0])
        else:
            self.rect.x = 862
    
        if self.rect.x > 0:
            self.rect.x = abs(self.rect.x + state["velocidade_jogador"][0])
        else:
            self.rect.x = 0
    
        if self.rect.y < 400:
            self.rect.y = abs(self.rect.y + state["velocidade_jogador"][1]) + (state["aceleracao_gravidade"])
        else:
            self.rect.y = 400
    
        if self.rect.y > 0:
            self.rect.y = abs(self.rect.y + state["velocidade_jogador"][1]) + (state["aceleracao_gravidade"])
        else:
            self.rect.y = 0
        
        if self.rect.x < 862:
            self.rect.x = abs(self.rect.x + self.vel_x)
        else:
            self.rect.x = 862
        
        if self.rect.x > 0:
            self.rect.x = abs(self.rect.x + self.vel_x)
        else:
            self.rect.x = 0
        
        if self.rect.y < 400:
            self.rect.y = abs(self.rect.y + self.vel_y) + (state["aceleracao_gravidade"])
        else:
            self.rect.y = 400
    
        if self.rect.y > 0:
            self.rect.y = abs(self.rect.y + self.vel_y) + (state["aceleracao_gravidade"])
        else:
            self.rect.y = 0  

            #spritecolliderect retorn true ou false e entao se for true o vel_y vira 0

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