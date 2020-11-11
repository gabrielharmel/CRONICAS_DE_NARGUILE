#bibliotecas & módulos
import pygame
import periodo1
from pygame import mixer

def main():
    """Esse é o método principal do jogo. """
    
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/menu.png')

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

        if comando[pygame.K_KP1] or comando[pygame.K_1]:
            """Aqui temos um outro espaço onde estão armazenados todas as telas
            iniciais do jogo, ou seja, causas, consequências e personagens do jogo.
            Chamamos este outro código de periodo1.Ele vai importar todas as informações
            do outro código."""
            periodo1.main()
        
        #este elif é responsável pelos créditos jogo
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            fundo = pygame.image.load('imagens/creditos.png')

        #este elif é responsável pelas opções do jogo
        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            #fundo = pygame.image.load('imagens/opcoes.png')
            opcoes()

        #este elif é responsável por sair do jogo
        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
            janela_aberta = False
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            fundo = pygame.image.load('imagens/menu.png')

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcoes():
    """Aqui está o método chamado de opcoes. Basicamente ele funciona assim:
    Quando pressionada a tecla 3 no menu, será exibida uma tela com duas opções.
    Se o jogador clicar 1, ele será direcionado para uma tela que contém uma 
    explicaçã de como jogar o jogo. Caso o jogador aperte 2, ele será direcionado
    para uma outra tela onde contém todas as informações acerca dos controles."""
    
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/opcoes.png')
    
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

        if comando[pygame.K_KP1] or comando[pygame.K_1]:
            como_jogar()
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            controles()
        elif comando[pygame.K_ESCAPE]:
            main()
    
        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()


    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def como_jogar():
    """Aqui está o método chamado de opcoes. Basicamente ele funciona assim:
    Quando pressionada a tecla 3 no menu, será exibida uma tela com duas opções.
    Se o jogador clicar 1, ele será direcionado para uma tela que contém uma 
    explicaçã de como jogar o jogo. Caso o jogador aperte 2, ele será direcionado
    para uma outra tela onde contém todas as informações acerca dos controles."""
    
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/comojogar.png')
    
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

        if comando[pygame.K_ESCAPE]:
           opcoes()
    
        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()


    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def controles():
    """Aqui está o método chamado de opcoes. Basicamente ele funciona assim:
    Quando pressionada a tecla 3 no menu, será exibida uma tela com duas opções.
    Se o jogador clicar 1, ele será direcionado para uma tela que contém uma 
    explicaçã de como jogar o jogo. Caso o jogador aperte 2, ele será direcionado
    para uma outra tela onde contém todas as informações acerca dos controles."""
    
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/controles.png')
    
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

        if comando[pygame.K_ESCAPE]:
            opcoes()
    
        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()


    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

"""Temos aqui um if responsável para executar o jogo. É o principal if. Se a
condição for verdadeira o jogo será executado."""
if __name__ == "__main__":
    main()

