from tkinter import *
from time import strftime
import time

root = Tk()
root.title("Organizador")


def janela_cronometro():

	n_janela = Toplevel(root)
	n_janela.title("Cronômetro")
	n_janela.geometry("365x83")

	def cronometra():

		zero = time.time()
		novo_tempo = str(time.time() - zero)
		crono_label.config(text = novo_tempo)
		crono_label.after(1000, cronometra)

	inicio = Button(n_janela, text = "Início")
	crono_label = Label(n_janela, font = ('calibri', 40, 'bold'),
	background = 'purple',
	foreground = 'white')
	crono_label.pack()
	inicio.pack()
	cronometra()
	n_janela.mainloop()

def janela_temporizador():

	n_janela = Toplevel(root)
	n_janela.title("Temporizador")
	n_janela.geometry("365x83")

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
	hora = strftime("%T %p")
	horas.config(text = hora)
	horas.after(1000, horario)
	

horas = Label(root, font = ('calibri', 40, 'bold'),
	background = 'purple',
    foreground = 'white')

horas.pack()
data_label.pack()

cronometro = Button(root, text = "Cronômetro", command = janela_cronometro)
cronometro.pack()

temporizador = Button(root, text = "Temporizador", command = janela_temporizador)
temporizador.pack()

calendario = Button(root, text = "Calendário", command = janela_calendario)
calendario.pack()



horario()
data()
root.mainloop()