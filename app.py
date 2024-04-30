import pygame  # Importa o módulo Pygame
import sys  # Importa o módulo sys para sair do jogo
import time  # Importa o módulo time para controlar o tempo
import random  # Importa o módulo random para gerar números aleatórios

pygame.init()  # Inicializa o Pygame

white = (255, 255, 255)  # Define a cor branca
black = (0, 0, 0)  # Define a cor preta
red = (213, 50, 80)  # Define a cor vermelha
green = (0, 255, 0)  # Define a cor verde

dis_width = 800  # Define a largura da tela
dis_height = 600  # Define a altura da tela

dis = pygame.display.set_mode((dis_width, dis_height))  # Define a tela do jogo
pygame.display.set_caption('Snake Game')  # Define o título do jogo na janela

clock = pygame.time.Clock()  # Define o clock do jogo

snake_block = 10  # Define o tamanho do bloco da serpente

font_style = pygame.font.SysFont(None, 50)  # Define o estilo da fonte para a pontuação

# Função para desenhar a serpente na tela
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Função para exibir a tela de game over com a pontuação do jogador
def game_over_screen(score):
    dis.fill(black)  # Preenche a tela com a cor preta
    game_over_font = pygame.font.SysFont(None, 75)  # Define o estilo da fonte para a mensagem de game over
    game_over_Surf = game_over_font.render('Sua pontuação é :' + str(score), True, white)  # Cria a superfície de texto
    game_over_Rect = game_over_Surf.get_rect()  # Obtém o retângulo da superfície de texto
    game_over_Rect.midtop = (dis_width / 2, dis_height / 4)  # Define a posição do retângulo
    dis.blit(game_over_Surf, game_over_Rect)  # Desenha o texto na tela
    pygame.display.flip()  # Atualiza a tela
    pygame.time.wait(1500)  # Espera 1.5 segundos antes de fechar a tela

# Função principal do jogo
def gameLoop():
    game_over = False  # Inicializa a flag de game over
    x1, y1 = dis_width / 2, dis_height / 2  # Define a posição inicial da cabeça da serpente
    x1_change, y1_change = 0, 0  # Define a velocidade inicial da serpente
    snake_List = []  # Inicializa a lista que armazenará as posições da serpente
    snake_speed = 15  # Define a velocidade inicial da serpente
    length_of_snake = 1  # Define o comprimento inicial da serpente
    foodx, foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10, round(random.randrange(0, dis_height - snake_block) / 10.0) * 10  # Define a posição inicial da comida

    while not game_over:  # Loop principal do jogo
        for event in pygame.event.get():  # Obtém os eventos do jogo
            if event.type == pygame.QUIT:  # Se o jogador fechar a janela
                game_over = True  # Define a flag de game over como True
            elif event.type == pygame.KEYDOWN:  # Se o jogador pressionar uma tecla
                if event.key == pygame.K_LEFT:  # Se a tecla pressionada for a seta para a esquerda
                    x1_change, y1_change = -snake_block, 0  # Define a mudança de posição da serpente
                elif event.key == pygame.K_RIGHT:  # Se a tecla pressionada for a seta para a direita
                    x1_change, y1_change = snake_block, 0  # Define a mudança de posição da serpente
                elif event.key == pygame.K_UP:  # Se a tecla pressionada for a seta para cima
                    x1_change, y1_change = 0, -snake_block  # Define a mudança de posição da serpente
                elif event.key == pygame.K_DOWN:  # Se a tecla pressionada for a seta para baixo
                    x1_change, y1_change = 0, snake_block  # Define a mudança de posição da serpente

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:  # Se a serpente colidir com as bordas da tela
            game_over = True  # Define a flag de game over como True

        x1 += x1_change  # Atualiza a posição x da cabeça da serpente
        y1 += y1_change  # Atualiza a posição y da cabeça da serpente
        dis.fill(black)  # Preenche a tela com a cor preta
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])  # Desenha a comida na tela
        snake_head = [x1, y1]  # Define a posição da cabeça da serpente
        snake_List.append(snake_head)  # Adiciona a posição da cabeça da serpente à lista

        if len(snake_List) > length_of_snake:  # Se o comprimento da serpente for maior que o tamanho especificado
            del snake_List[0]  # Remove o último bloco da serpente da lista

        for x in snake_List[:-1]:  # Para cada bloco da serpente, exceto a cabeça
            if x == snake_head:  # Se a cabeça da serpente colidir com algum bloco do corpo
                game_over = True  # Define a flag de game over como True

        our_snake(snake_block, snake_List)  # Desenha a serpente na tela
        pygame.display.update()  # Atualiza a tela

        if x1 == foodx and y1 == foody:  # Se a serpente comer a comida
            foodx, foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10, round(random.randrange(0, dis_height - snake_block) / 10.0) * 10  # Define a nova posição da comida
            length_of_snake += 1  # Aumenta o comprimento da serpente
            snake_speed += 1  # Aumenta a velocidade da serpente

        clock.tick(snake_speed)  # Define a velocidade do jogo

    game_over_screen(length_of_snake - 1)  # Exibe a tela de game over com a pontuação
    pygame.quit()  # Sai do Pygame
    sys.exit()  # Sai do programa

gameLoop()  # Chama a função principal do jogo
