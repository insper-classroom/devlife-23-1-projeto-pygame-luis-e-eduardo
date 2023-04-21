from random import randint
import pygame
from assets import *

class Plataform(pygame.sprite.Sprite):
    
    def __init__(self,sprites,plataforma,x,y):
        self.plataforma = plataforma
        pygame.sprite.Sprite.__init__(self)
        img_plataforma = pygame.image.load("ground.png")
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
        fonte_padrao = pygame.font.get_default_font()
        self.font = pygame.font.Font(fonte_padrao, 24)
        self.azul = (0,0,255)
        self.vermelho = (255, 0, 0)
        self.verde = (0,255,0)
        
        fundo = pygame.image.load(assets["fundo1"]) #imagem gerdada pela AI "https://www.scenario.com/""
        self.fundo = pygame.transform.scale(fundo, (912,512))
        
        self.chao = pygame.Rect(0,450,912,112) #chao provisório, coords certas 

        self.plataforma = pygame.sprite.Group()
        self.jogador = Jogador(self.plataforma)
        self.sprites.add(self.jogador)

        self.window = window

        for i in range(30):
            x = 32*i
            Plataform(self.sprites,self.plataforma,x,445)
        for i in range(5):
            x = 200+32*i
            Plataform(self.sprites,self.plataforma,x,380)
        for i in range(5):
            x = 350+32*i
            Plataform(self.sprites,self.plataforma,x,315)

    def recebe_eventos(self):
        
        velocidade_x = 1
        velocidade_y = 3

        clock = pygame.time.Clock()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return Tela2()
            
            #caso o botao seja apertado, ele soma a velocidade ate parar de apertar 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                state["velocidade_jogador"][0] += velocidade_x
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                state["velocidade_jogador"][0] -= velocidade_x
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                state["velocidade_jogador"][0] -= velocidade_x
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                state["velocidade_jogador"][0] += velocidade_x
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                #implementar condicao do jagor piular quando estiver no chao ou quando houver colisao
                state["velocidade_jogador"][1] -= velocidade_y
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                state["velocidade_jogador"][1] += velocidade_y
            if event.type==pygame.KEYDOWN and event.key == pygame.K_e:
                Tiro(self.sprites, self.plataforma, self.jogador.rect.x, self.jogador.rect.y+25)
        

        self.sprites.update()
        clock.tick(120)

        return self

    def desenha(self, window):

        #window.fill(self.verde)
        window.blit(self.fundo,(0,0)) #colocando o fundo do jogo
        pygame.draw.rect(window,(150,75,0),self.chao) #desenhando o chao 

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
    
    def __init__(self,chao):

        pygame.init() 
        pygame.sprite.Sprite.__init__(self)

        mario = pygame.image.load("personagem_principal.png")
        self.image = pygame.transform.scale(mario, (50,50))

        self.rect = self.image.get_rect()

        self.chao = chao

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
            anterior = self.rect.y
            self.rect.y = abs(self.rect.y + state["velocidade_jogador"][1]) + (state["aceleracao_gravidade"])
            lista = pygame.sprite.spritecollide(self, self.chao, False)
            if len(lista)>0:
                self.rect.y = anterior
            lista = []
        else:
            print(2)
            self.rect.y = 400
    
        if self.rect.y > 0:
            anterior = self.rect.y
            self.rect.y = abs(self.rect.y + state["velocidade_jogador"][1]) + (state["aceleracao_gravidade"])
            lista = pygame.sprite.spritecollide(self, self.chao, False)
            if len(lista)>0:
                self.rect.y = anterior
            lista = []
        else: 
            print(4)
            self.rect.y = 0

class Tiro(pygame.sprite.Sprite):
    def __init__(self, sprites,meteoros, x, y):
        pygame.sprite.Sprite.__init__(self)

        img_laser = pygame.image.load('assets/img/laserRed16.png')
        self.image = pygame.transform.scale(img_laser,(16,12))
        
        self.rect = self.image.get_rect()
        self.vel_y_laser = 0

        self.rect.x = x
        self.rect.y = y
        self.vel_y_laser = -500

        self.flag_tiro = False
        self.meteoros = meteoros
        sprites.add(self) 
        self.sprites = sprites 
    def update(self, delta_t):

        self.rect.y = (self.rect.y + self.vel_y_laser*delta_t)
        lista = pygame.sprite.spritecollide(self, self.meteoros,True)
        for tiro in lista:
            self.sprites.remove(self)
        

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