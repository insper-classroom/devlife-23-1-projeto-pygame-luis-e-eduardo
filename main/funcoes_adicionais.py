import pygame 
from classes_adicionais import *

def gera_plataforma(self,quantidade_blocos,eixo,inicio,outro_eixo):
    """
    Gera uma plataforma horizontal ou vertical com a quantidade de blocos especificada.
    
    Args:
    - quantidade_blocos: int, quantidade de blocos que a plataforma terá.
    - eixo: str, eixo em que a plataforma será gerada (horizontal ou vertical).
    - inicio: int, posição inicial no eixo especificado.
    - outro_eixo: int, posição no outro eixo (posição fixa).
    """
    if eixo == 'x':   
        x = 0
        for i in range(quantidade_blocos):
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,inicio + x, outro_eixo, 'bloco')
            x += 24 
    if eixo == 'y':
        x = 0
        for i in range(quantidade_blocos):
            Plataform(self.sprites,self.plataforma,self.plataformas_quebraveis,outro_eixo, inicio - x, 'bloco')
            x += 24 

def load_spritesheet(spritesheet, rows, columns): #funcao feita pelo professor Toshi 
    """
    Cria uma lista de sprites a partir de uma imagem spritesheet, que contém várias imagens menores organizadas em linhas e 
    colunas.

    Args:
    spritesheet (Surface): a imagem spritesheet contendo todas as imagens menores.
    rows (int): a quantidade de linhas na spritesheet.
    columns (int): a quantidade de colunas na spritesheet.

    Returns:
    list: uma lista contendo as imagens menores como elementos.
    """
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    sprites = []
    for row in range(rows):
        for column in range(columns):
            x = column * sprite_width
            y = row * sprite_height
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)
            image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
    return sprites

def musica(musica):
    """
    Carrega uma música e a toca em loop.

    Parâmetros:
    -----------
    musica : str 
    """
    pygame.mixer.music.load(musica)
    pygame.mixer.music.set_endevent(pygame.USEREVENT) #para reniciar a musica caso acabar
    pygame.mixer.music.play() 