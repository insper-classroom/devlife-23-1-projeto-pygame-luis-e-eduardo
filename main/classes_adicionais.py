import pygame 
from assets import *
from random import randint

class Plataform(pygame.sprite.Sprite):
    """
    Inicializa um onjeto plataforma 

    Parametros:
        sprites (pygame.sprite.Group): grupo sprites da plataforma 
        plataforma (pygame.sprite.Group): grupo de plataformas 
        plataformas_quebraveis (pygame.sprite.Group): grupo da plataformas quebraveis 
        x (int): cordenada x da plataforma
        y (int): cordenada y da plataforma
        tipo (str): tipo de plataforma 

    Returns:
        None.
    """
    def __init__(self,sprites,plataforma,plataformas_quebraveis,x,y,tipo):
        self.plataforma = plataforma
        self.tipo = tipo 
        self.plataformas_quebraveis = plataformas_quebraveis
        pygame.sprite.Sprite.__init__(self)
        if self.tipo == 'grass':
            img_plataforma = pygame.image.load(assets["grass"])
            self.image = pygame.transform.scale(img_plataforma, (50,15))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            sprites.add(self)
            self.plataforma.add(self)
        if self.tipo == 'bloco':
            img_plataforma = pygame.image.load(assets["img_bloco1"])
            self.image = pygame.transform.scale(img_plataforma, (50,30))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            sprites.add(self)
            self.plataforma.add(self)
        if self.tipo == 'sand':
            img_plataforma = pygame.image.load(assets["sand"])
            self.image = pygame.transform.scale(img_plataforma, (25,25))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            sprites.add(self)
            self.plataformas_quebraveis.add(self)

class Estrela(pygame.sprite.Sprite):
    """
    Cria uma nova instância de Estrela.

    Args:
        sprites (pygame.sprite.Group): Grupo de sprites ao qual a instância deve ser adicionada.
        estrela (pygame.sprite.Group): Grupo de estrelas ao qual a instância deve ser adicionada.
        x (int): Posição x da estrela.
        y (int): Posição y da estrela.
    """
    def __init__(self,sprites,estrela,x,y):
        self.estrela = estrela
        pygame.sprite.Sprite.__init__(self)
        img_estrela = pygame.image.load(assets["img_estrela"])
        self.image = pygame.transform.scale(img_estrela, (35,35))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.estrela.add(self)

class Coracao(pygame.sprite.Sprite):
    """
    Cria uma nova instância de Coracao.

    Args:
        sprites (pygame.sprite.Group): Grupo de sprites ao qual a instância deve ser adicionada.
        coracao (pygame.sprite.Group): Grupo de coracoes ao qual a instância deve ser adicionada.
        x (int): Posição x do coracao.
        y (int): Posição y do coracao.
    """
    def __init__(self,sprites,coracao,x,y):
        self.coracao = coracao
        pygame.sprite.Sprite.__init__(self)
        img_coracao = pygame.image.load(assets["img_coracao1"])
        self.image = pygame.transform.scale(img_coracao, (45,45))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.coracao.add(self)

class Carne(pygame.sprite.Sprite):
    """
    Cria uma nova instância de Carne.

    Args:
        sprites (pygame.sprite.Group): Grupo de sprites ao qual a instância deve ser adicionada.
        carne (pygame.sprite.Group): Grupo de carnes ao qual a instância deve ser adicionada.
        x (int): Posição x da carne.
        y (int): Posição y da carne.
    """
    def __init__(self,sprites,carne,x,y):
        self.carne = carne
        pygame.sprite.Sprite.__init__(self)
        img_coracao = pygame.image.load(assets["img_carne"])
        self.image = pygame.transform.scale(img_coracao, (45,45))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.carne.add(self)

class Pocao(pygame.sprite.Sprite):
    """
    Cria uma nova instância de Pocao.

    Args:
        sprites (pygame.sprite.Group): Grupo de sprites ao qual a instância deve ser adicionada.
        pocao (pygame.sprite.Group): Grupo de pocoes ao qual a instância deve ser adicionada.
        x (int): Posição x da pocao.
        y (int): Posição y da pocao.
    """
    def __init__(self,sprites,pocao,x,y):
        self.pocao = pocao
        pygame.sprite.Sprite.__init__(self)
        img_pocao = pygame.image.load(assets["img_berry"])
        self.image = pygame.transform.scale(img_pocao, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        sprites.add(self)
        self.pocao.add(self)

class Monstro(pygame.sprite.Sprite):      
    """
        Inicializa um objeto Monstro.

        Args:
            sprites: grupo de sprites ao qual o monstro será adicionado.
            monstros: grupo de monstros ao qual o monstro será adicionado.
            x: coordenada x inicial do monstro na tela.
            y: coordenada y inicial do monstro na tela.
        """
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
    """
        Inicializa um objeto Gorila.

        Args:
            sprites: grupo de sprites ao qual o gorila será adicionado.
            gorila: grupo de gorila ao qual o gorila será adicionado.
            x: coordenada x inicial do gorila na tela.
            y: coordenada y inicial do gorila na tela.
        """
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
    """
    Classe para criar um objeto passaro.

    Args:
        sprites (pygame.sprite.Group): Grupo que contém todos os sprites.
        passaro (pygame.sprite.Group): Grupo que contém apenas os passaros.
        x (int): Posição horizontal inicial do passaro.
        y (int): Posição vertical inicial do passaro.
        jogador (Jogador): Instância da classe Jogador.
        lista_passaros (list): Lista com todos os passaros criados.

    Attributes:
        passaro (pygame.sprite.Group): Grupo que contém apenas os passaros.
        jogador (Jogador): Instância da classe Jogador.
        lista_passaros (list): Lista com todos os passaros criados.
        vel_x (int): Velocidade horizontal do passaro.
        vel_y (int): Velocidade vertical do passaro.

    Methods:
        update(delta_t): Atualiza a posição do passaro no tempo delta_t.

    """
    def __init__(self,sprites,passaro,x,y,jogador,lista_passaros):
        self.passaro = passaro
        pygame.sprite.Sprite.__init__(self)
        img_passaro = pygame.image.load("passaro.png")  
        self.image = pygame.transform.scale(img_passaro, (90,55))
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
            self.vel_x = 5
        if self.rect.x >= 850:
            self.vel_x = -4
        self.rect.x = (self.rect.x + self.vel_x)

        if self.rect.y < 30:
            self.vel_y = 1
        if self.rect.y > 80:
            self.vel_y = -1
        self.rect.y = (self.rect.y + self.vel_y)

class Tiro(pygame.sprite.Sprite):
    """"
    Classe representa os tiros do jogador dentro do jogo 
    """
    def __init__(self, sprites,monstros,plataforma,plataformas_quebraveis,gorilas,passaro, x, y):
        """
        Inicializa a classe Tiro com as coordenadas do tiro e adiciona-o ao grupo de sprites.

        Parâmetros:
        - sprites: grupo de sprites que o tiro será adicionado
        - monstros: grupo de sprites dos monstros que podem ser atingidos pelo tiro
        - plataforma: grupo de sprites das plataformas
        - plataformas_quebraveis: grupo de sprites das plataformas quebráveis
        - gorilas: grupo de sprites dos gorilas que podem ser atingidos pelo tiro
        - passaro: grupo de sprites dos passaros que podem ser atingidos pelo tiro
        - x: coordenada x do tiro
        - y: coordenada y do tiro
        """
        pygame.sprite.Sprite.__init__(self)

        img_laser = pygame.image.load(assets["img_bola"])
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
        self.gorilas = gorilas
        self.passaro = passaro
        sprites.add(self) 
        self.sprites = sprites 

        musica_tiro = pygame.mixer.Sound("som_tiro.mp3")
        musica_tiro.set_volume(1)
        musica_tiro.play()
        
    
    def update(self, delta_t):
        """
        Atualiza a posição do tiro e verifica se atingiu algum alvo (monstros, plataformas, gorilas, passaros).

        Parâmetros:
        - delta_t: valor de tempo para atualização da posição do tiro
        """
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

        lista_plataformas_quebraveis = pygame.sprite.spritecollide(self, self.gorilas,True)
        for tiro in lista_plataformas_quebraveis:
            self.kill()
            lista_plataformas_quebraveis = []
            assets["gorila_vivo"] = False
            musica_estrela = pygame.mixer.Sound("gorila_morreu.mp3")
            musica_estrela.set_volume(0.9)
            musica_estrela.play()

        lista_plataformas_quebraveis = pygame.sprite.spritecollide(self, self.passaro,True)
        for tiro in lista_plataformas_quebraveis:
            self.kill()

class Tiro_monstro(pygame.sprite.Sprite):
    """"
    Classe para representar o tiro dos gorilas 
    """
    def __init__(self, sprites,plataforma,plataformas_quebraveis, x, y, tiro_monstro, direcao):
        """
        Inicializa a classe Tiro_monstro.

        Parâmetros
        ----------
        sprites : pygame.sprite.Group
            grupo de sprites do jogo
        plataforma : pygame.sprite.Group
            grupo de plataformas do jogo
        plataformas_quebraveis : pygame.sprite.Group
            grupo de plataformas quebráveis do jogo
        x : int
            posição x inicial do tiro
        y : int
            posição y inicial do tiro
        tiro_monstro : pygame.sprite.Group
            grupo de tiros do monstro
        direcao : str
            direção do tiro (esquerda ou direita)
        """
        pygame.sprite.Sprite.__init__(self)

        img_laser = pygame.image.load(assets["img_banana"])
        self.image = pygame.transform.scale(img_laser,(30,30))
        
        self.tiro_monstro = tiro_monstro
        self.rect = self.image.get_rect()
        self.vel_y_laser = 0
        self.rect.x = x
        self.rect.y = y - 10
        
        if direcao == "direita":
            self.vel_x_laser = +200
            if assets["vel_nana"]:
                self.vel_x_laser = 100
        else:
            self.vel_x_laser = -200
            if assets["vel_nana"]:
                self.vel_x_laser = -100

        self.flag_tiro = False
        self.plataforma = plataforma
        self.plataformas_quebraveis = plataformas_quebraveis

        sprites.add(self) 
        self.tiro_monstro.add(self)
        self.sprites = sprites 
    
    def update(self, delta_t):
        """
        Atualiza a posição do tiro e verifica se colidiu com alguma plataforma.

        Parâmetros
        ----------
        delta_t : float
            tempo transcorrido desde a última atualização
        """
        self.rect.x = (self.rect.x + self.vel_x_laser*delta_t)
        if self.rect.x > 912 or self.rect.x < 0:
            self.kill()
        lista_plataformas = pygame.sprite.spritecollide(self, self.plataforma,False)
        for tiro in lista_plataformas:   
            self.kill()
        lista_plataformas_quebraveis = pygame.sprite.spritecollide(self, self.plataformas_quebraveis,False)
        for tiro in lista_plataformas_quebraveis:
            self.kill()