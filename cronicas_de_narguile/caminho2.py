#bibliotecas & módulos
import pygame
import jogo
import caminho1
import caminho2
from pygame import mixer

def main():
    """Esse é o método principal do Caminho 2. """
    
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c2f11.png')

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

        if comando[pygame.K_KP1] or comando[pygame.K_1]:
            c2f12()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            morrer_c2f12()
        
        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            caminho1.c1f11()
        
        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
            c2f12()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao(): 
#este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/opcao.png')

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


        if comando[pygame.K_KP1] or comando[pygame.K_1]:
            main()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c2f12():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c2f12.png')

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


        if comando[pygame.K_KP1] or comando[pygame.K_1]:
            morrer_c2f12()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            morrer_c2f12()

        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            c2f13()
        
        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
            morrer_c2f12()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c2f12()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c2f12(): 
#este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/opcao.png')

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


        if comando[pygame.K_KP1] or comando[pygame.K_1]:
            c2f12()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def morrer_c2f12():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/morrer.png')

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


        if comando[pygame.K_KP1] or comando[pygame.K_1]:
            main()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()
        
        elif comando[pygame.K_ESCAPE]:
            opcao()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c2f13():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c2f13.png')

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


        if comando[pygame.K_KP1] or comando[pygame.K_1]:
            caminho1.c1f20()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            caminho1.c1f20()

        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            morrer_c2f12()

        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
            morrer_c2f12()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c2f13()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c2f13(): 
#este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/opcao.png')

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


        if comando[pygame.K_KP1] or comando[pygame.K_1]:
            c2f13()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

