from tkinter import *
from tkinter import ttk
import time
import random as rand



root = Tk()

velocidade = StringVar()
vel_lista = ['Rápido', 'Médio', 'Lento']

ordenacoes = StringVar()
ord_lista = ['Merge Sort', 'Bubble Sort', 'Insertion Sort', 'Quick Sort',
'Heap Sort', 'Selection Sort']

def numeros_aleatorios():
	
	global lista
	lista = [rand.randint(250, 800) for i in range(100)]
	cria_retangulos(lista, ['red' for x in range(0, len(lista))])
	

def cria_retangulos(lista, cor):

	tela_can.delete("all")
	dist = 3
	for i in range(0, len(lista)):
		tela_can.create_rectangle(dist, 800 - lista[i], 5 + dist , 800, fill = cor[i])
		dist += 8
	
	root.update_idletasks()



def bubble_sort(lista, velocidade):

	for j in range(0, len(lista)):
		for i in range(0, len(lista) - j - 1):

			if lista[i] > lista[i + 1]:

				aux = lista[i]
				lista[i] = lista[i + 1]
				lista[i + 1] =  aux
				cria_retangulos(lista, ['green' if x == j + 1 else 'red' for x in range(0, len(lista))])
				time.sleep(velocidade)
			
		cria_retangulos(lista, ['green' for x in range(0, len(lista))])
		

def merge_sort(lista, aux, inicio, fim, velocidade):

	if inicio < fim:

		metade = int((inicio + fim) / 2)

		merge_sort(lista, aux, inicio, metade, velocidade)
		merge_sort(lista, aux, metade + 1, fim, velocidade)

		merge(lista, aux, inicio, metade, fim, velocidade)

		cria_retangulos(lista, ['green' if x == metade else 'red' for x in range(0, len(lista))])
		time.sleep(velocidade)
			
	cria_retangulos(lista, ['green' for x in range(0, len(lista))])

def merge(lista, aux, inicio, metade, fim, velocidade):

	
	for i in range(inicio, fim + 1):

		aux[i] = lista[i]

	p =  inicio
	q = metade + 1

	for j in range(inicio, fim + 1):
		
		if p > metade:
			lista[j] = aux[q]
			q += 1

		elif q > fim:
			lista[j] = aux[p]
			p += 1

		elif aux[p] < aux[q]:
			lista[j] = aux[p]
			p += 1

		else:
			lista[j] = aux[q]
			q += 1

def insertion_sort(lista, velocidade):

	for i in range(1, len(lista)):

		pivo = lista[i]
		j = i - 1

		while pivo < lista[j] and j >= 0:
			lista[j + 1] = lista[j]
			j -= 1
			cria_retangulos(lista, ['green' if x == pivo else 'red' for x in range(0, len(lista))])
			time.sleep(velocidade)

		lista[j + 1] = pivo

	cria_retangulos(lista, ['green' for x in range(0, len(lista))])

def particao(inicio, fim, lista):
	
	index_pivo = inicio
	pivo = lista[index_pivo]

	while inicio < fim:

		while inicio < len(lista) and lista[inicio] <= pivo:

			inicio += 1

		while lista[fim] > pivo:
			fim -= 1

		if inicio < fim:
			aux = lista[inicio]
			lista[inicio] = lista[fim]
			lista[fim] = aux
		
		
	
	aux = lista[fim]
	lista[fim] = lista[index_pivo]
	lista[index_pivo] = aux

	return fim

def quick_sort(inicio, fim, lista, velocidade):

	if inicio < fim:

		p = particao(inicio, fim, lista)
		quick_sort(inicio, p - 1, lista, velocidade)
		quick_sort(p + 1, fim, lista, velocidade)
		cria_retangulos(lista, ['green' if x == p else 'red' for x in range(0, len(lista))])
		time.sleep(velocidade)

	cria_retangulos(lista, ['green' for x in range(0, len(lista))])


def selectionSort(lista, velocidade):

	tam = len(lista)
	for i in range(0, tam -1):
		menor = i

		j = i + 1

		while j < tam:

			if lista[j] < lista[menor]:
				menor = j

			j += 1

		if i != menor:
			aux = lista[i]
			lista[i] = lista[menor]
			lista[menor] = aux
		
		cria_retangulos(lista, ['green' if x == menor else 'red' for x in range(0, len(lista))])
		time.sleep(velocidade)
	cria_retangulos(lista, ['green' for x in range(0, len(lista))])


def heapifica(lista, n, i):

	maior = i

	esq = (2 * i) + 1
	drt = (2 * i) + 2

	if esq < n  and lista[maior] < lista[esq]:
		maior = esq

	if drt < n and lista[maior] < lista[drt]:
		maior = drt

	if maior != i:

		aux = lista[maior]
		lista[maior] = lista[i]
		lista[i] = aux

		heapifica(lista, n, maior)



def heapSort(lista, velocidade):

	n = len(lista)

	for i in range(n//2 - 1, -1, -1):
		heapifica(lista, n, i)
		cria_retangulos(lista, ['green' if x == i else 'red' for x in range(0, len(lista))])
		time.sleep(velocidade)

	for j in range(n - 1, 0, -1):
		aux = lista[j]
		lista[j] = lista[0]
		lista[0] = aux
		heapifica(lista, j, 0)
		cria_retangulos(lista, ['green' if x == j else 'red' for x in range(0, len(lista))])
		time.sleep(velocidade)

	cria_retangulos(lista, ['green' for x in range(0, len(lista))])

def escolhe_velocidade():

	if vel_selecao.get() == 'Rápido':
		return 0.001

	elif vel_selecao.get() == 'Médio':
		return  0.01

	else:
		return 0.1



def roda_orednacao():
	global lista
	velocidade = escolhe_velocidade()

	if ord_selecao.get() == 'Bubble Sort':
		bubble_sort(lista, velocidade)

	elif ord_selecao.get() == 'Merge Sort':
		aux = [0] * len(lista)
		merge_sort(lista, aux, 0, len(lista) - 1, velocidade)

	elif ord_selecao.get() == 'Insertion Sort':
		insertion_sort(lista, velocidade)

	elif ord_selecao.get() == 'Quick Sort':
		quick_sort(0, len(lista) - 1, lista, velocidade)

	elif ord_selecao.get() == 'Selection Sort':
		selectionSort(lista, velocidade)

	elif ord_selecao.get() == 'Heap Sort':
		heapSort(lista, velocidade)


U_Frame = Frame(root, width = 800, height = 250)
U_Frame.grid(row = 0, column = 0)

inicio = Button(U_Frame, text = 'Inicia', command = roda_orednacao)
inicio.grid(row = 0, column = 0)

gera_lista = Button(U_Frame, text = 'Gera Lista', command = numeros_aleatorios)
gera_lista.grid(row = 0, column = 1)

vel = Label(U_Frame, text = 'Velociade', background = 'lightgray')
vel.grid(row = 1, column = 0, padx = 10, pady = 10)

vel_selecao = ttk.Combobox(U_Frame, textvariable = velocidade, values = vel_lista)
vel_selecao.grid(row = 2, column = 0, padx = 5, pady = 5)
vel_selecao.current(0)

ord_algo = Label(U_Frame, text = 'Algoritmo de Ordenação', background = 'lightgray') 
ord_algo.grid(row = 1, column = 1, padx = 10, pady = 10)

ord_selecao = ttk.Combobox(U_Frame, textvariable = ordenacoes, values = ord_lista)
ord_selecao.grid(row = 2, column = 1, padx = 5, pady = 5)
ord_selecao.current(0)

tela_can = Canvas(root, width = 800, height = 800, background = 'lightblue')
tela_can.grid(row = 1, column = 0)

root.mainloop()

