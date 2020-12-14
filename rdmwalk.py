import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#random walk 2d e duas analises
def random_walk(n):
	x = 0
	y = 0
	
	for i in range(n):
		dx, dy = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])
		x += dx
		y+= dy
		
	return((x, y))

# A analise busca a porcentagem de caminhos que teminaram 
# a uma determinada distancia do inicio
def monte_carlo(valor,  tam_teste, n_testes):

	for n_passos in range(1, tam_teste + 1):
		longe = 0
		for i in range(n_testes):
			(x, y) = random_walk(n_passos)
			res =  abs(x) + abs(y)
			if res > valor:
				longe += 1
		distancias = float(longe)/n_testes
		print(f"distancia: {n_passos} - porc. de caminhos maiores que {valor}: {distancias * 100}%")

# A analise busca qual o maior numero de passos que na media 
# ainda te deixa a um certa distancia do inicio
def maior_caminhada_segura(valor, tam_teste, n_testes):

	for passos in range(valor, tam_teste + 1):
		perto = 0
		for j in range(n_testes):

			caminho = random_walk(passos)
			res =  abs(caminho[0]) + abs(caminho[1])
			if res <= valor:
				perto += 1
		media = float(perto)/n_testes
		print(f"passos: {passos} - porc. dos caminhos que terminam a {valor} do inicio: {media * 100}%")


#desenho de random walk 1d

def random_walk_linear(n):

	x = 0
	passos = [x]
	for i in range(n):
		dx = random.choice([1, 0, -1])
		x += dx
		passos.append(x)
	return(passos)

def desenha_random_walk1d(passos, n = 1):

	for i in range(n):
		lista_pas = random_walk_linear(passos)
		y = [i + 1 for i in range(0, len(lista_pas))]
		plt.plot(y, lista_pas)

	plt.show()


#desenho random walk 2d

def random_walk_bidimensional(n):
	x, y = 0, 0
	x_passos = [x]
	y_passos = [y]

	for i in range(n):
		(dx, dy) = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
		x += dx
		y += dy
		x_passos.append(x)
		y_passos.append(y)

	return((x_passos, y_passos))

def desenha_random_walk2d(passos, n = 1):
	
	for i in range(n):
		x, y = random_walk_bidimensional(passos)
		plt.plot(y, x)

	plt.show()


# desenho random walk 3d

def random_walk_tridimensional(n):
	
	x, y, z = 0, 0, 0
	x_passos = [x]
	y_passos = [y]
	z_passos = [z]

	for i in range(n):
		dx, dy, dz = random.choice([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)])
		x += dx
		y += dy
		z += dz
		x_passos.append(x)
		y_passos.append(y)
		z_passos.append(z)

	return((x_passos, y_passos, z_passos))

def desenha_random_walk3d(passos, n = 1):

	fig = plt.figure()
	ax = Axes3D(fig)
	for i in range(n):
		x, y, z = random_walk_tridimensional(passos)
		
		ax.plot(x, y, z)

	plt.show()


