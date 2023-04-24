from random import randint
import pygame
from assets import *

class Plataform(pygame.sprite.Sprite):
    def __init__(self,sprites,plataforma,x,y):
        self.plataforma = plataforma
        pygame.sprite.Sprite.__init__(self)
        img_plataforma = pygame.image.load("esse_chao.png")
        self.image = pygame.transform.scale(img_plataforma, (100,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.plataforma.add(self)
class Portal(pygame.sprite.Sprite):
    def __init__(self,sprites,portal,x,y):
        self.portal = portal
        pygame.sprite.Sprite.__init__(self)
        img_portal = pygame.image.load("portal.png")
        self.image = pygame.transform.scale(img_portal, (80,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.portal.add(self)
class Monstro(pygame.sprite.Sprite):      
    def __init__(self,sprites,monstros,x,y):
        self.monstros = monstros
        pygame.sprite.Sprite.__init__(self)
        img_monstro = pygame.image.load("monstro.png")
        self.image = pygame.transform.scale(img_monstro, (60,70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.monstros.add(self)

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
        
        self.vidas = 3
        coracao = pygame.image.load("coracao.png")
        self.coracao = pygame.transform.scale(coracao, (15,15))

        self.last_updated = 0

        fundo = pygame.image.load(assets["fundo1"]) #imagem gerdada pela AI "https://www.scenario.com/""
        self.fundo = pygame.transform.scale(fundo, (912,512))
        
        self.chao = pygame.Rect(0,450,912,112) #chao provisório, coords certas 

        self.plataforma = pygame.sprite.Group()
        self.monstros = pygame.sprite.Group()
        self.portal = pygame.sprite.Group()
        self.jogador = Jogador(self.plataforma,self.monstros,self.portal)
        self.sprites.add(self.jogador)

        

        self.window = window

        for i in range(30):
            x = 32*i
            Plataform(self.sprites,self.plataforma,x, 480)

        Plataform(self.sprites,self.plataforma,350,335)
        Plataform(self.sprites,self.plataforma,200,400)
        Plataform(self.sprites,self.plataforma,500,280)
        Plataform(self.sprites,self.plataforma,680,210)
        Plataform(self.sprites,self.plataforma,700,210)
        Plataform(self.sprites,self.plataforma,730,210)
        Plataform(self.sprites,self.plataforma,750,210)

        Portal(self.sprites,self.portal, 780, 140)
        
        for i in range(3):
            x = randint(0,912)
            Monstro(self.sprites,self.monstros, x, 480-50)
        Monstro(self.sprites, self.monstros, randint(750,900), 210-50)
        
        

        
            

    def recebe_eventos(self):
        
        velocidade_x = 3
        velocidade_y = 3

        clock = pygame.time.Clock()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            
            #caso o botao seja apertado, ele soma a velocidade ate parar de apertar 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.jogador.speedx += velocidade_x
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.jogador.speedx -= velocidade_x
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.jogador.speedx -= velocidade_x
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.jogador.speedx += velocidade_x
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.jogador.jump()
            #     #implementar condicao do jagor piular quando estiver no chao ou quando houver colisao
            #     self.jogador.speedx[1] -= velocidade_y
            # elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            #     self.jogador.speedx[1] += velocidade_y
            if event.type==pygame.KEYDOWN and event.key == pygame.K_e:
                Tiro(self.sprites, self.monstros, self.jogador.rect.x, self.jogador.rect.y+25)

            if assets["portal"]:
                return Tela2()
        
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
    
    def __init__(self,chao,monstros,portal):

        pygame.init() 
        pygame.sprite.Sprite.__init__(self)

        self.monstros = monstros
        self.portal = portal

        mario = pygame.image.load("personagem_principal.png")
        self.image = pygame.transform.scale(mario, (50,50))

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
            print(1)
            assets["vidas"]-=1

        collisions = pygame.sprite.spritecollide(self, self.portal, True)
        for cada_colisao in collisions:
            assets["portal"] = True

        
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == self.STILL:
            self.speedy -= self.JUMP_SIZE
            self.state = self.JUMPING

class Tiro(pygame.sprite.Sprite):
    def __init__(self, sprites, monstros, x, y):
        pygame.sprite.Sprite.__init__(self)

        img_laser = pygame.image.load('tiro.png')
        self.image = pygame.transform.scale(img_laser,(16,6))
        
        self.rect = self.image.get_rect()
        self.vel_y_laser = 0

        self.rect.x = x
        self.rect.y = y
        self.vel_x_laser = 500

        self.flag_tiro = False
        self.monstros = monstros
        sprites.add(self) 
        self.sprites = sprites 

    def update(self, delta_t):
        self.rect.x = (self.rect.x + self.vel_x_laser*delta_t)
        lista = pygame.sprite.spritecollide(self, self.monstros,True)
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