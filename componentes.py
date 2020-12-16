import pygame

cor_de_fundo = (100, 100, 100)
preto = (0, 0, 0)
branco = (255, 255, 255)
cor_texto = (150, 30, 30)
cor_hora = (20, 210, 20)
(largura, altura) = (400, 150)



class Botao(object):

	def __init__(self, nome, pos, janela, cor):

		self.__nome = nome
		self.__pos = pos
		self.__sup = pygame.Surface((50, 50), 0, janela)
		self.__janela = janela
		self.__cor = cor

	@property
	def nome(self):
		return self.__nome
		
		
	def display(self):

		fonte = pygame.font.SysFont('freesansbold.ttf', 30)
		texto = fonte.render(self.__nome, True, preto, self.__cor)
		ret = pygame.Rect((self.__pos), self.__sup.get_size())	
		pygame.draw.rect(self.__janela, self.__cor, ret)
		pygame.draw.rect(self.__janela, preto, ret, 3)
		self.__janela.blit(texto, (ret.center[0] - 7, ret.center[1] - 10))
		

	@property
	def ret(self):
		return((pygame.Rect((self.__pos), self.__sup.get_size())))

class Tela(object):

	def __init__(self, texto, pos, tela):

		self.texto = texto
		self.__pos = pos
		self.__sup = pygame.Surface((250, 70), 0, tela)
		self.__tela = tela

	def display(self):

		fonte = pygame.font.SysFont('freesansbold.ttf', 40)
		texto = fonte.render(self.texto, True, preto, branco)
		ret = pygame.Rect((self.__pos), self.__sup.get_size())	
		pygame.draw.rect(self.__tela, branco, ret)
		pygame.draw.rect(self.__tela, preto, ret, 3)
		self.__tela.blit(texto, (ret.center[0] - 120, ret.center[1] - 10))

class Pilha(object):

	def __init__(self):

		self.topo = -1
		self.pilha = []
		self.__tamanho = 14

	def __repr__(self):
		return(self.apresenta())

	def empilha(self, item):
		if(self.topo < self.__tamanho):
			self.topo += 1
			self.pilha.append(item)

	def desempilha(self):

		if(self.topo == -1):
			return(0)
		
		self.topo -= 1
		item = self.pilha[self.topo]
		return(item)

	def apresenta(self):

		apr = ""
		for item in self.pilha:
			apr = apr + str(item)

		return(apr)

	def limpa(self):

		self.pilha.clear()
		self.topo = -1 








