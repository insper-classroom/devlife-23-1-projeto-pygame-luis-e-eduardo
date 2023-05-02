import pygame 
from classes_adicionais import *

def gera_plataforma(self,quantidade_blocos,eixo,inicio,outro_eixo):
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