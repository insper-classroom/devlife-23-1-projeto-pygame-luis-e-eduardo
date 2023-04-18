from random import randint
import pygame
from assets import *

class TelaInicial:
    def __init__(self, window):
        fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(fonte_padrao, 24)
        self.window = window

    def recebe_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None 
            elif evento.type == pygame.KEYDOWN:
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

        self.jogador = Jogador()
        self.sprites.add(self.jogador)

        self.window = window

    def recebe_eventos(self):
        velocidade = 100
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return Tela2()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.jogador.rect.x+=velocidade
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.jogador.rect.x-=velocidade
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.jogador.rect.y-=velocidade
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.jogador.rect.y+=velocidade
        return self

    def desenha(self, window):
        window.fill(self.verde)
        window.blit(self.fundo,(0,0))
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
        self.image = pygame.transform.scale(mario, (48,48))
        
        self.rect = self.image.get_rect()
        self.rect.x = 1280/2 - self.rect.width/2
        self.rect.y = 480 - self.rect.height

       
    def update(self):
        if self.rect.x + self.rect.width >= 1280:
            self.rect.x = 1280 - self.rect.width
        if self.rect.x  < 0:
            self.rect.x = 0
        if self.rect.y + self.rect.height >= 600:
            self.rect.y = 600 - self.rect.height
        if self.rect.y < 0:
            self.rect.y = 0

       

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