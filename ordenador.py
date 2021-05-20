from tkinter import *
import time
import random as rand


root = Tk()


def numeros_aleatorios():
	
	global lista
	lista = [rand.randint(180, 800) for i in range(100)]
	cria_retangulos(lista, ['red' for x in range(0, len(lista))])
	

def cria_retangulos(lista, cor):

	tela_can.delete("all")
	dist = 3
	for i in range(0, len(lista)):
		tela_can.create_rectangle(dist, 800 - lista[i], 5 + dist , 800, fill = cor[i])
		dist += 8
	
	root.update_idletasks()

def bubble_sort(lista):

	for j in range(0, len(lista)):
		for i in range(0, len(lista) - j - 1):

			if lista[i] > lista[i + 1]:

				aux = lista[i]
				lista[i] = lista[i + 1]
				lista[i + 1] =  aux
				cria_retangulos(lista, ['green' if x == j + 1 else 'red' for x in range(0, len(lista))])
				time.sleep(0.002)
			
		cria_retangulos(lista, ['green' for x in range(0, len(lista))])


def roda_orednacao():
	global lista
	bubble_sort(lista)



inicio = Button(root, text = 'Inicia', command = roda_orednacao)
inicio.grid(row = 0, column = 0)
gera_lista = Button(root, text = 'Novo', command = numeros_aleatorios)
gera_lista.grid(row = 1, column = 0)
tela_can = Canvas(root, width = 800, height = 800, background = 'lightblue')
tela_can.grid(row = 2, column = 0)

root.mainloop()

