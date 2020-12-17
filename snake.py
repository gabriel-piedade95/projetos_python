import pygame, random
from componentes import Grid, Snake, Tempo, Pontos, Comida


cor_de_fundo = (100, 100, 100)
azul_claro = (130, 180, 200)
amarelo = (255, 255, 0)
preto = (0, 0, 0)
verde = (20, 110, 20)

largura = 620
altura = 680
grid_tam = (600, 600)
pos_grid = (10, 70)
cel_tam = (15, 15)
info_tam = (200, 50)
pos_tmp =(10, 10)
pos_pnt = (410, 10)
var_comida_x = (10, 600)
var_comida_y = (70, 600)

UP = (0, -15)
DOWN = (0, 15)
LEFT = (-15, 0)
RIGHT = (15, 0) 

def cria_janela(nome, tamanho):
	janela = pygame.display.set_mode(tamanho)
	pygame.display.set_caption(nome)
	janela.fill(cor_de_fundo)
	return(janela)


pygame.init()

tela = cria_janela("Snake", (largura, altura))

pygame.display.flip()
tempo = pygame.time.Clock()
rodar = True
grid = Grid(tela, pos_grid)
tmp = Tempo(tela, pos_tmp)
pontos = Pontos(0, tela, pos_pnt)
cobra = Snake(tela, 310, 370, pontos)
comida = Comida()
while (rodar):
	tela.fill(cor_de_fundo)
	
	for evento in pygame.event.get():
		if (evento.type == pygame.QUIT):
			rodar = False

		press = pygame.key.get_pressed()
		if (press[pygame.K_LEFT]):
			cobra.anda(LEFT)
		if (press[pygame.K_RIGHT]):
			cobra.anda(RIGHT)
		if (press[pygame.K_UP]):
			cobra.anda(UP)
		if (press[pygame.K_DOWN]):
			cobra.anda(DOWN)

	if cobra.comeu(comida):
			comida.renova()

	cobra.anda(cobra.direcao)
	grid.desenhaGrid(comida.pos)
	cobra.apresenta()
	tmp.atualiza()	
	tmp.apresenta()
	pontos.apresenta()
	tempo.tick(10)
	pygame.display.update()	
	

pygame.quit()