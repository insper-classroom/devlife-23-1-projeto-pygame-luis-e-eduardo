import pygame 
from telas import *
class Jogo:
    """
    Classe responsável por gerenciar o jogo e suas telas.

    Atributos:
    -----------
    sprites : pygame.sprite.Group
        Grupo de sprites do jogo.
    window : pygame.Surface
        Tela principal do jogo.
    tela_atual : Tela
        Tela atual do jogo.
    last_updated : int
        Timestamp do último update do jogo.

    Métodos:
    --------
    __init__()
        Inicializa a classe Jogo.
    recebe_eventos()
        Recebe e trata eventos do jogo.
    game_loop()
        Loop principal do jogo.
    finaliza()
        Finaliza o jogo e a biblioteca pygame.
    """
    def __init__(self):
        """
        Inicializa a classe jogo
        """
        pygame.init()
        self.sprites = pygame.sprite.Group()

        self.window = pygame.display.set_mode((912,512))

        self.tela_atual = TelaInicial(self.window)
        self.last_updated = pygame.time.get_ticks()

    def recebe_eventos(self):
        """
        Recebe todos os eventos de todas as telas do jogo 
        """
        self.tela_atual = self.tela_atual.recebe_eventos()
        # recebe_eventos tela atual
        if self.tela_atual is None:
            return False
        return True

    def game_loop(self):
        """
        Loop principal do jogo
        """
        while self.recebe_eventos():
            self.tela_atual.desenha(self.window)
            pygame.display.update()

    def finaliza(self):
        """
        Finaliza o jogo 
        """
        pygame.quit()

if __name__ == '__main__':
    jogo = Jogo()
    jogo.game_loop()
    jogo.finaliza()
