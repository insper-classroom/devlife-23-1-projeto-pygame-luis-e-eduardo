import pygame 
from telas import *

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
