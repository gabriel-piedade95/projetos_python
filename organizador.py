from tkinter import *
from time import strftime
import time
import datetime as dt 


root = Tk()
root.title("Organizador")


def janela_cronometro():

	global ligado
	global contador
	n_janela = Toplevel(root)
	n_janela.title("Cronômetro")
	ligado = False
	contador = 66600



	def label_contador(crono_label):


		def cronometra():
			if ligado:
				global contador

				if contador == 66600:
					novo_tempo = "Iniciando..."

				else:
					tempo = dt.datetime.fromtimestamp(contador)
					t = (contador - 66600)
					milisec = t % 100
					sec = (t // 100) % 60
					minutos = (t // 6000) % 60
					novo_tempo = f'{minutos:02d}:{sec:02d}:{milisec:02d}'
					

				crono_label.config(text = novo_tempo)
				crono_label.after(10, cronometra)
				contador += 1


		cronometra()


	def inicia_crono(crono_label):
		global ligado
		ligado = True
		label_contador(crono_label)
		inicio['state'] = 'disabled'
		pausa['state'] = 'normal'
		zera['state'] = 'normal'


	def pausa_crono():

		global ligado
		inicio['state'] = 'normal'
		pausa['state'] = 'disabled'
		zera['state'] = 'normal'
		ligado = False

	def zera_crono(crono_label):

		global contador
		contador = 66600

		if ligado == False:
			zera['state'] = 'disabled'
			crono_label['text'] = '00:00:00'

		else:
			crono_label['text'] = 'Iniciando...'


	crono_label = Label(n_janela, font = ('calibri', 40, 'bold'), text = '00:00:00', 
	background = 'purple',
	foreground = 'white')

	crono_label.pack()

	Uframe = Frame(n_janela)

	inicio = Button(Uframe, text = "Início", command = lambda: inicia_crono(crono_label))
	pausa = Button(Uframe, text = "Pausa", command = pausa_crono, state = 'disabled')
	zera = Button(Uframe, text = "Zera",
	command = lambda: zera_crono(crono_label), state = 'disabled')
	
	

	Uframe.pack(anchor = 'center')
	inicio.pack(side = 'left')
	pausa.pack(side = 'left')
	zera.pack(side = 'left')
	
	n_janela.mainloop()

def janela_temporizador():

	n_janela = Toplevel(root)
	n_janela.title("Temporizador")
	
	def pega_info():
		global entrada
		info = entrada.get()
		print(info)


	Uframe = Frame(n_janela)
	inicio = Button(Uframe, text = 'Início', command = pega_info)
	entrada = Entry(Uframe)

	Uframe.pack(anchor = 'center')
	entrada.pack(side = 'left')

	inicio.pack(side = 'left')
	

def janela_calendario():

	n_janela = Toplevel(root)
	n_janela.title("Calendário")
	n_janela.geometry("365x83")

def data():

	dt = strftime("%D - %a") 
	data_label.config(text = dt)
	data_label.after(1000, data)

data_label = Label(root, font = ('calibri', 20, 'bold'),
		background = 'green', foreground = 'white')


def horario():
	hora = strftime("%T")
	horas.config(text = hora)
	horas.after(1000, horario)
	

horas = Label(root, font = ('calibri', 40, 'bold'),
	background = 'purple',
    foreground = 'white')

data_label.pack()
horas.pack()

UFRAME = Frame(root)

cronometro = Button(UFRAME, text = "Cronômetro", command = janela_cronometro)
temporizador = Button(UFRAME, text = "Temporizador", command = janela_temporizador)
calendario = Button(UFRAME, text = "Calendário", command = janela_calendario)

UFRAME.pack(anchor = 'center')
cronometro.pack(side = 'left')
temporizador.pack(side = 'left')
calendario.pack(side = 'left')



horario()
data()
root.mainloop()