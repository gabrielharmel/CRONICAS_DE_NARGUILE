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
        de if e elif."""

        if comando[pygame.K_KP1] or comando[pygame.K_1]:
            """Se cair nesse if, o sistema vai "puxar" o método principal do módulo
            periodo1."""
            periodo1.main()
        
        #este elif é responsável pelos créditos jogo
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            fundo = pygame.image.load('imagens/creditos.png')

        #este elif é responsável pelas opções do jogo
        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            """Para auxiliar na ilustração das opções, foi necessário criar este
            módulo para exibir corretamente as telas."""
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

        """Aqui temos uma parte destinada as condições desse módulo."""

        #este if serve para exibir a tela de como jogar 
        if comando[pygame.K_KP1] or comando[pygame.K_1]:
            como_jogar()
        #este elif serve para exibir a tela dos controles
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            controles()
        # este elif serve para voltar ao módulo main, ou seja, para o principal
        # do módulo jogo
        elif comando[pygame.K_ESCAPE]:
            main()
    
        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()


    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def como_jogar():
    """Aqui está o método chamado de como_jogar. A função é exibir a tela 
    de como jogar."""
    
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

        """Aqui temos uma parte destinada a todas as condições do módulo."""

        # este if serve para voltar a tela de opções
        if comando[pygame.K_ESCAPE]:
           opcoes()
    
        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()


    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def controles():
    """Aqui está o método chamado de opcoes. A sua função é exibir a tela dos
    controles."""
    
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

        """Aqui temos uma parte destinada as condições desse método."""

        #este if serve para voltar no método de opções
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

