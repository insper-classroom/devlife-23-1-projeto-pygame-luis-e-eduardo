import pygame 
from assets import *
from random import randint

class Plataform(pygame.sprite.Sprite):
    def __init__(self,sprites,plataforma,plataformas_quebraveis,x,y,tipo):
        self.plataforma = plataforma
        self.tipo = tipo 
        self.plataformas_quebraveis = plataformas_quebraveis
        pygame.sprite.Sprite.__init__(self)
        if self.tipo == 'grass':
            img_plataforma = pygame.image.load("grass.png")
            self.image = pygame.transform.scale(img_plataforma, (50,15))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            sprites.add(self)
            self.plataforma.add(self)
        if self.tipo == 'bloco':
            img_plataforma = pygame.image.load("bloco1.png")
            self.image = pygame.transform.scale(img_plataforma, (50,30))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            sprites.add(self)
            self.plataforma.add(self)
        if self.tipo == 'sand':
            img_plataforma = pygame.image.load("sand.png")
            self.image = pygame.transform.scale(img_plataforma, (25,25))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            sprites.add(self)
            self.plataformas_quebraveis.add(self)

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
        img_coracao = pygame.image.load("coracao1.png")
        self.image = pygame.transform.scale(img_coracao, (45,45))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.coracao.add(self)

class Pocao(pygame.sprite.Sprite):
    def __init__(self,sprites,pocao,x,y):
        self.pocao = pocao
        pygame.sprite.Sprite.__init__(self)
        img_pocao = pygame.image.load("berry.png")
        self.image = pygame.transform.scale(img_pocao, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.pocao.add(self)

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

class Gorila(pygame.sprite.Sprite):      
    def __init__(self,sprites,gorila,x,y,lado):
        self.gorila = gorila
        pygame.sprite.Sprite.__init__(self)
        if lado == 'direita':
            img_gorila = pygame.image.load(assets["gorila_img"])
        if lado == 'esquerda':  
            img_gorila_esquerda = pygame.image.load(assets["gorila_img"])
            img_gorila = pygame.transform.flip(img_gorila_esquerda, True, False )
        self.image = pygame.transform.scale(img_gorila, (120,150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.gorila.add(self)

class Passaro(pygame.sprite.Sprite):      
    def __init__(self,sprites,passaro,x,y,jogador,lista_passaros):
        self.passaro = passaro
        pygame.sprite.Sprite.__init__(self)
        img_passaro = pygame.image.load("passaro.png")  
        self.image = pygame.transform.scale(img_passaro, (100,60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.passaro.add(self)
        self.jogador = jogador 
        self.lista_passaros = lista_passaros
        self.vel_x = 1
        self.vel_y = 1

    def update(self,delta_t):
        if self.rect.x <= 0:
            self.vel_x = 4
        if self.rect.x >= 700:
            self.vel_x = -4
        self.rect.x = (self.rect.x + self.vel_x)

        if self.rect.y < 20:
            self.vel_y = 2
        if self.rect.y > 150:
            self.vel_y = -2
        self.rect.y = (self.rect.y + self.vel_y)

class Tiro(pygame.sprite.Sprite):
    def __init__(self, sprites,monstros,plataforma,plataformas_quebraveis, x, y):
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
        self.plataformas_quebraveis = plataformas_quebraveis
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
            lista_plataformas_quebraveis = pygame.sprite.spritecollide(self, self.plataformas_quebraveis,True)
            for tiro in lista_plataformas_quebraveis:
                self.kill()

class Tiro_monstro(pygame.sprite.Sprite):
    def __init__(self, sprites,plataforma,plataformas_quebraveis, x, y, tiro_monstro):
        pygame.sprite.Sprite.__init__(self)

        img_laser = pygame.image.load('banana.png')
        self.image = pygame.transform.scale(img_laser,(30,30))
        
        self.tiro_monstro = tiro_monstro
        self.rect = self.image.get_rect()
        self.vel_y_laser = 0
        self.rect.x = x
        self.rect.y = y - 10
        sorteio = randint(1,2)
        if sorteio == 1:
            self.vel_x_laser = -200
        else:
            self.vel_x_laser = +200

        self.flag_tiro = False
        self.plataforma = plataforma
        self.plataformas_quebraveis = plataformas_quebraveis

        sprites.add(self) 
        self.tiro_monstro.add(self)
        self.sprites = sprites 
    
    def update(self, delta_t):
        
            self.rect.x = (self.rect.x + self.vel_x_laser*delta_t)
            if self.rect.x > 912 or self.rect.x < 0:
                self.kill()
            lista_plataformas = pygame.sprite.spritecollide(self, self.plataforma,False)
            for tiro in lista_plataformas:   
                self.kill()
            lista_plataformas_quebraveis = pygame.sprite.spritecollide(self, self.plataformas_quebraveis,False)
            for tiro in lista_plataformas_quebraveis:
                self.kill()