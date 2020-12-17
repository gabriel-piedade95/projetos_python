import random, pygame

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


class Comida(object):

	def __init__(self):

		self._x = random.randint(10, 600)
		self._y = random.randint(70, 600)

	@property
	def pos(self):
		return(self._x, self._y)

	def renova(self):

		self._x = random.randint(10, 600)
		self._y = random.randint(70, 600)


class Snake(object):
	
	def __init__(self, tela, x_inicio, y_inicio, pontos):
		self.x = x_inicio
		self.y = y_inicio
		self.pnt = pontos
		self.__tela = tela
		self.direcao = random.choice([UP, DOWN, LEFT, RIGHT])
		self.posicoes = [(x_inicio, y_inicio)]
		self.tam = 1

	@property
	def pos(self):
		if len(self.posicoes) > 0:
			return(self.posicoes[0][0], self.posicoes[0][1])
		else: 
			return(self.x, self.y)

	def posicao_invalida(self, grid_tam, pos_grid):
		return(self.posicoes[0][0] < pos_grid[0] or self.posicoes[0][0] > grid_tam[0] or
		self.posicoes[0][1] < pos_grid[1] or self.posicoes[0][1] > grid_tam[1] + pos_grid[1] -1)
	
	def direciona(self, comando):
		if len(self.posicoes) > 1 and (comando[0] * -1, comando[1] * -1) == self.direcao:
			return
		else:
			self.direcao = comando

	def reset(self):
		self.direcao = random.choice([UP, DOWN, LEFT, RIGHT])
		self.posicoes = [(self.x, self.y)]
		self.tam = 1
		self.pnt.zera()

	def anda(self, comando):
		
		self.direciona(comando)
		atual = self.posicoes[0]
		prox = (atual[0] + comando[0], atual[1] + comando[1])
		if (self.tam  > 1 and prox in self.posicoes[2:]) or self.posicao_invalida(grid_tam, pos_grid):
			print("Game Over")
			self.reset()
			
		else:
			self.posicoes.insert(0, prox)
			if len(self.posicoes) > self.tam:
				self.posicoes.pop()

	def apresenta(self):
		for pos in self.posicoes:
			cel = pygame.Rect((pos,  cel_tam))
			pygame.draw.rect(self.__tela, verde, cel)

	def comeu(self, comida):
		cel = pygame.Rect(((self.pos),  cel_tam))
		if (cel.collidepoint(comida.pos)):
			self.tam += 1
			self.pnt.aumenta()
			return(1)


class Grid(object):

	def __init__(self, tela, pos):

		self.__tela = tela
		self.__pos = pos

	def desenhaGrid(self, comida):
		pygame.draw.rect(self.__tela, preto, (self.__pos,  grid_tam), 5)
		pygame.draw.rect(self.__tela, azul_claro, (self.__pos,  grid_tam))
		for lg in range(10, grid_tam[0] + 10, cel_tam[0]):
			for alt in range(70, grid_tam[1] + 70, cel_tam[0]):
				cel = pygame.Rect(((lg, alt),  cel_tam))
				if cel.collidepoint(comida):
					pygame.draw.rect(self.__tela, amarelo, cel)	
				pygame.draw.rect(self.__tela, preto, cel, 1)
		

class Tempo(object):

	def __init__(self, tela, pos):
	
		self.sec = 0
		self.__min = 0
		self.__hora = 0
		self.__tela = tela
		self.__pos = pos

	def apresenta(self):
		fonte = pygame.font.SysFont('freesansbold.ttf', 40)
		tmp = f"{self.__hora:02d}:{self.__min:02d}:{self.__sec:02d}"
		texto = fonte.render(tmp, True, preto, azul_claro)
		ret = pygame.Rect((self.__pos), info_tam)
		pygame.draw.rect(self.__tela, preto, (self.__pos,  info_tam), 5)
		pygame.draw.rect(self.__tela, azul_claro, (self.__pos,  info_tam))
		self.__tela.blit(texto, (ret.center[0] - 90, ret.center[1] - 10))

	@property
	def tmp(self):
		return self.__tempo

	def atualiza(self):
		self.__sec = (int(pygame.time.get_ticks())//1000)%60
		self.__min = (int(pygame.time.get_ticks())//60000)%60
		self.__hora = (int(pygame.time.get_ticks())//36000000)%60
		

class Pontos(object):

	def __init__(self, pontos, tela, pos):
		self.__pontos = pontos
		self.__tela = tela
		self.__pos = pos

	def apresenta(self):
		fonte = pygame.font.SysFont('freesansbold.ttf', 40)
		texto = fonte.render(str(self.__pontos), True, preto, azul_claro)
		ret = pygame.Rect((self.__pos), info_tam)
		pygame.draw.rect(self.__tela, preto, (self.__pos,  info_tam), 5)
		pygame.draw.rect(self.__tela, azul_claro, (self.__pos,  info_tam))
		self.__tela.blit(texto, (ret.center[0] - 90, ret.center[1] - 10))

	def aumenta(self):
		self.__pontos += 100

	def zera(self):
		self.__pontos = 0