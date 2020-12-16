import pygame
from componentes import Botao, Tela, Pilha

cor_de_fundo = (100, 100, 100)
cor1 = (150, 150, 150)
preto = (0, 0, 0)
cor_texto = (150, 30, 30)
cor_hora = (20, 210, 20)
(largura, altura) = (300, 300)

def prioridade(op1, op2):

	prd = {"X" : 3, "/" : 3, "+": 2, "-": 2, "(": 1}

	if(prd[op1] <= prd[op2]):
		return(0)

	else:
		return(1)


def posfixa(expressao):

	pos_f = []
	expr = list(expressao)
	aux = []
	num = "0"
	i = 0
	operadores = ["X", "/", "+", "-"]
	while i < len(expr):
		
		if expr[i].isdigit():
			num += expr[i]
		else:
			if(num != "0"):
				aux.append(int(num))
				num = "0"

			if expr[i] in operadores:
				if len(pos_f) == 0:
					pos_f.append(expr[i])
				else:	
					topo = len(pos_f) - 1
					while (topo >= 0 and prioridade(pos_f[topo], expr[i])):
						
						x = pos_f.pop(topo)
						aux.append(x)
						topo -= 1
					pos_f.append(expr[i])

			elif expr[i] == "(":
				pos_f.append(expr[i])

			elif expr[i] == ")":
				topo = len(pos_f) - 1
				while (pos_f[topo] != "(" and topo >= 0):
					
					x = pos_f.pop(topo)
					aux.append(x)
					topo -= 1
				pos_f.pop(topo)
		i += 1
	if num != "0":
		aux.append(int(num))
	topo = len(pos_f) - 1
	while (topo >= 0):
		x = pos_f.pop(topo)
		aux.append(x)
		topo -= 1

	return(aux)


def resolve_posfixa(lista):

	pilha = []
	k = -1
	for i in range(0, len(lista)):
		
		
		if type(lista[i]) == int:
			pilha.append(lista[i])
			k += 1

		if lista[i] == "X":
			pilha[k - 1] = pilha[k -1] * pilha.pop(k)
			k -= 1

		if lista[i] == "/":
			pilha[k - 1] = pilha[k -1] / pilha.pop(k)
			k -= 1

		if lista[i] == "+":
			pilha[k - 1] = pilha[k -1] + pilha.pop(k)
			k -= 1

		if lista[i] == "-":
			pilha[k - 1] = pilha[k -1] - pilha.pop(k)
			k -= 1

	return(pilha[0])

pygame.font.init()
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Calculadora")
janela.fill(cor_de_fundo)
pygame.display.flip()

botoes_n = []
num = 1
for i in range(0, 4):
	altura = 50 * (i + 1)
	for j in range(0, 3):
		botoes_n.append(Botao(f"{num}", ((20 + j * 50), 40 + altura), janela, cor1))
		if(num == 0):
			break
		else:
			num = (num + 1)%10

botoes_c = []
num = 0
lista_botoes_c = ["+", "-", "X", "/", "(", ")", "=", "c"]
for i in range(0, 4):
	altura = 50 * (i + 1)
	for j in range(0, 2):
		botoes_c.append(Botao(f"{lista_botoes_c[num]}", ((190 + j * 50), 40 + altura), janela, cor1))
		if(num == len(lista_botoes_c) - 1):
			break
		else:
			num += 1


tela = Tela("", (25, 10), janela)
pilha = Pilha()
rodar = True
while(rodar):

	tela.texto = pilha.apresenta()
	tela.display()

	for botao_n in botoes_n:
		botao_n.display()

	for botao_c in botoes_c:
		botao_c.display()

	for evento in pygame.event.get():
		if (evento.type == pygame.QUIT):
			rodar = False

		if (evento.type == pygame.MOUSEBUTTONDOWN):
			mouse = evento.pos

			for botao_n in botoes_n:

				if botao_n.ret.collidepoint(mouse):
					pilha.empilha(botao_n.nome)

			for i in range(0, 6):

				if botoes_c[i].ret.collidepoint(mouse):
					pilha.empilha(botoes_c[i].nome)


			if botoes_c[6].ret.collidepoint(mouse):
				expr = posfixa(pilha.apresenta())
				res = resolve_posfixa(expr)
				pilha.limpa()
				pilha.empilha(str(int(res)))

			if botoes_c[7].ret.collidepoint(mouse):
				pilha.limpa()

	pygame.display.update()	

pygame.quit()