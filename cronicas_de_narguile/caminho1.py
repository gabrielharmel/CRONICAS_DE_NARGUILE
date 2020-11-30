#bibliotecas & módulos
import pygame
import periodo1
import caminho2 
import jogo
from pygame import mixer

def main():
    """Esse é o método principal do Caminho 1. """
    
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/pergunta.png')

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
            c1f11()
        
       
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            caminho2.main()
        
       
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

        """Aqui temos uma parte destinada a todas as telas do jogo com um conjunto
        enorme de if, elif e else."""

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

def c1f11():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f11.png')

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
            c1f12()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            morrer_c1f11()

        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            caminho2.main()
        
        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
            c1f12()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f11()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f11(): 
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

        """Aqui temos uma parte destinada a todas as telas do jogo com um conjunto
        enorme de if, elif e else."""

        if comando[pygame.K_KP1] or comando[pygame.K_1]:
            c1f11()
        
    
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        
        tamanho_janela.blit(fundo, (0,0))

        
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def morrer_c1f11():
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
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f12():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f12.png')

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
            morrer_c1f11()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            morrer_c1f11()

        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            c1f13()

        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
            morrer_c1f11()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f12()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f12(): 
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
            c1f12()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f13():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f13.png')

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
            c1f20()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            morrer_c1f11()

        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            morrer_c1f11()

        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
            morrer_c1f11()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f13()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f13(): 
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
            c1f13()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f20(): 
#este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f20.png')

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


        if comando[pygame.K_KP_ENTER]:
            c1f21()
        
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f20()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f20(): 
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
            c1f20()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f21():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f21.png')

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
            c1f22()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            morrer_fase2()

        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            morrer_fase2()

        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
            morrer_fase2()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f21()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f21(): 
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
            c1f21()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f22():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f22.png')

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
            morrer_fase2()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            c1f23()

        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            morrer_fase2()

        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
            morrer_fase2()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f22()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f22(): 
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
            c1f22()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f23():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f23.png')

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
            morrer_fase2()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            c1f30()

        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            morrer_fase2()

        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
            morrer_fase2()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f23()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f23(): 
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
            c1f23()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f30():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f30.png')

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


        if comando[pygame.K_KP_ENTER]:
            c1f31()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f30()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f30(): 
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
            c1f30()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f31():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f31.png')

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
            morrer_fase3()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            morrer_fase3()

        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            c1f32()

        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
            morrer_fase3()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f31()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f31(): 
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
            c1f31()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f32():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f32.png')

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
            morrer_fase3()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            morrer_fase3()

        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            morrer_fase3()

        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
            c1f33()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f32()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f32(): 
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
            c1f32()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f33():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f33.png')

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
            morrer_fase3()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            c1f40()

        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            morrer_fase3()

        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
           morrer_fase3()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f33()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f33(): 
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
            c1f33()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f40():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f40.png')

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

        if comando[pygame.K_KP_ENTER]:
            c1f41()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f40()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f40(): 
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
            c1f40()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f41():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f41.png')

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
            c1f42()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            morrer_fase4()

        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
           morrer_fase4()

        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
            morrer_fase4()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f41()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f41(): 
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
            c1f41()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f42():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f42.png')

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
            c1f43()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            c1f43()

        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            c1f43()

        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
            c1f43()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f42()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f42(): 
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
            c1f42()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f43():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f43.png')

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
            c1f44()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            morrer_fase4()

        elif comando[pygame.K_KP3] or comando[pygame.K_3]:
            morrer_fase4()

        elif comando[pygame.K_KP4] or comando[pygame.K_4]:
            morrer_fase4()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f43()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f43(): 
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
            c1f43()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f44():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f44.png')

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


        if comando[pygame.K_KP_ENTER]:
            c1f45()

        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f44()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f44(): 
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
            c1f44()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def c1f45():
    #este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/c1f45.png')

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


        if comando[pygame.K_KP_ENTER]:
            creditos()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao_c1f45()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def opcao_c1f45(): 
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
            c1f45()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def creditos(): 
#este comando é responsável por inicializar os módulos 
    pygame.init()

    #este comando é responsável por inicializar a música 
    mixer.init()

    """Nesta parte temos todos os fundos de tela onde serão armazenados todas as 
    fases do jogo."""
    fundo = pygame.image.load('imagens/creditos.png')

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
        
        if comando[pygame.K_ESCAPE]:
            jogo.main()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def morrer_fase2():
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
            c1f21()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def morrer_fase3():
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
            c1f31()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()

def morrer_fase4():
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
            c1f41()
        
        elif comando[pygame.K_KP2] or comando[pygame.K_2]:
            jogo.main()
        
        #este elif é responsável para voltar ao menu
        elif comando[pygame.K_ESCAPE]:
            opcao()

        #este comando faz a imagem aparecer em todo o espaço disponível
        tamanho_janela.blit(fundo, (0,0))

        #este comando atualiza a tela
        pygame.display.update()

    #este comando é a finalização dos módulos, ou seja, do jogo em si
    pygame.quit()