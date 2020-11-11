#bibliotecas & módulos
import pygame
import jogo
import caminho1
from pygame import mixer

def main():
    """Este é o método principal do jogo. Nele está tudo."""
    
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/causas.png')
    
    """Este comando é responsável por definir o tamanho da janela recebendo como
    parâmetros a largura e a altura em pixel."""
    tamanho_janela = pygame.display.set_mode((1280,1000))
    
    #este comando é responsável pelo nome que aparecerá na tela 
    pygame.display.set_caption("CRÔNICAS DE NARGUILÉ")
    
    #esta variável vai armazenar um valor booleano 
    janela_aberta = True
    
    #aqui temos um loop que significa quando a janela_aberta ser True faça isso
    while janela_aberta:
    #este comando atualiza a tela em 60 segundos 
        pygame.time.delay(60)

    #este loop serve para fechar o jogo no X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        #esta variável armazenará o comando de entrada no teclado
        comando = pygame.key.get_pressed()

        """Aqui temos uma parte destinada a todas as telas do jogo com um conjunto
        enorme de if, elif e else."""

        if comando[pygame.K_KP_ENTER]:
            consequencias()
        
        if comando[pygame.K_ESCAPE]:
            jogo.main()
            
        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()


    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()
        
def consequencias(): 
    """Aqui está o método chamado de consequências. Basicamente ele funciona assim:
    Quando pressionada a tecla enter o jogo irá avançar e quando a tecla esc for 
    pressionada o jogo irá voltar. A sua principal função é exibir a tela
    consequências"""
    
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/consequencias.png')
    
    """Este comando é responsável por definir o tamanho da janela recebendo como
    parâmetros a largura e a altura em pixel."""
    tamanho_janela = pygame.display.set_mode((1280,1000))
    
    #este comando é responsável pelo nome que aparecerá na tela 
    pygame.display.set_caption("CRÔNICAS DE NARGUILÉ")
    
    #esta variável vai armazenar um valor booleano 
    janela_aberta = True
    
    #aqui temos um loop que significa quando a janela_aberta ser True faça isso
    while janela_aberta:
    #este comando atualiza a tela em 60 segundos 
        pygame.time.delay(60)

    #este loop serve para fechar o jogo no X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        #esta variável armazenará o comando de entrada no teclado
        comando = pygame.key.get_pressed()

        """Aqui temos uma parte destinada a todas as telas do jogo com um conjunto
        enorme de if, elif e else."""

        if comando[pygame.K_KP_ENTER]:
            jamaicaman()
        
        if comando[pygame.K_ESCAPE]:
            main()
        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()


    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def jamaicaman():
    """Aqui está o método chamado de jamaicaman. Basicamente ele funciona assim:
    Quando pressionada a tecla enter o jogo irá avançar e quando a tecla esc for 
    pressionada o jogo irá voltar. A sua principal função é exibir a tela do 
    jamaica man."""
    
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/jamaicaman.png')
    
    """Este comando é responsável por definir o tamanho da janela recebendo como
    parâmetros a largura e a altura em pixel."""
    tamanho_janela = pygame.display.set_mode((1280,1000))
    
    #este comando é responsável pelo nome que aparecerá na tela 
    pygame.display.set_caption("CRÔNICAS DE NARGUILÉ")
    
    #esta variável vai armazenar um valor booleano 
    janela_aberta = True
    
    #aqui temos um loop que significa quando a janela_aberta ser True faça isso
    while janela_aberta:
    #este comando atualiza a tela em 60 segundos 
        pygame.time.delay(60)

    #este loop serve para fechar o jogo no X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        #esta variável armazenará o comando de entrada no teclado
        comando = pygame.key.get_pressed()

        """Aqui temos uma parte destinada a todas as telas do jogo com um conjunto
        enorme de if, elif e else."""

        if comando[pygame.K_KP_ENTER]:
            cubasurfer()
        
        if comando[pygame.K_ESCAPE]:
            consequencias()
    
        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()


    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()
        
def cubasurfer():
    """Aqui está o método chamado de cubasurfer. Basicamente ele funciona assim:
    Quando pressionada a tecla enter o jogo irá avançar e quando a tecla esc for 
    pressionada o jogo irá voltar. A sua principal função é exibir a tela do 
    cuba surfer."""
    
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/cubasurfer.png')
    
    """Este comando é responsável por definir o tamanho da janela recebendo como
    parâmetros a largura e a altura em pixel."""
    tamanho_janela = pygame.display.set_mode((1280,1000))
    
    #este comando é responsável pelo nome que aparecerá na tela 
    pygame.display.set_caption("CRÔNICAS DE NARGUILÉ")
    
    #esta variável vai armazenar um valor booleano 
    janela_aberta = True
    
    #aqui temos um loop que significa quando a janela_aberta ser True faça isso
    while janela_aberta:
    #este comando atualiza a tela em 60 segundos 
        pygame.time.delay(60)

    #este loop serve para fechar o jogo no X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        #esta variável armazenará o comando de entrada no teclado
        comando = pygame.key.get_pressed()

        """Aqui temos uma parte destinada a todas as telas do jogo com um conjunto
        enorme de if, elif e else."""

        if comando[pygame.K_KP_ENTER]:
            floridaman()

        if comando[pygame.K_ESCAPE]:
            jamaicaman()
        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()


    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def floridaman():
    """Aqui está o método chamado de floridaman. Basicamente ele funciona assim:
    Quando pressionada a tecla enter o jogo irá avançar e quando a tecla esc for 
    pressionada o jogo irá voltar. A sua principal função é exibir a tela do 
    florida man."""
    
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/floridaman.png')
    
    """Este comando é responsável por definir o tamanho da janela recebendo como
    parâmetros a largura e a altura em pixel."""
    tamanho_janela = pygame.display.set_mode((1280,1000))
    
    #este comando é responsável pelo nome que aparecerá na tela 
    pygame.display.set_caption("CRÔNICAS DE NARGUILÉ")
    
    #esta variável vai armazenar um valor booleano 
    janela_aberta = True
    
    #aqui temos um loop que significa quando a janela_aberta ser True faça isso
    while janela_aberta:
    #este comando atualiza a tela em 60 segundos 
        pygame.time.delay(60)

    #este loop serve para fechar o jogo no X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        #esta variável armazenará o comando de entrada no teclado
        comando = pygame.key.get_pressed()

        """Aqui temos uma parte destinada a todas as telas do jogo com um conjunto
        enorme de if, elif e else."""

        if comando[pygame.K_KP_ENTER]:
            caminho1.main()

        if comando[pygame.K_ESCAPE]:
            cubasurfer()
        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()


    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()
        

        
       
    