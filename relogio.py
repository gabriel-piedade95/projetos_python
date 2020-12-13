import datetime, pygame

def dia_da_semana(hoje):

	dias_s = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

	return(dias_s[hoje])


def mes_nome(hoje):

	meses = ["Janerio", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
	 "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

	return(meses[hoje - 1])


pygame.font.init()

cor_de_fundo = (100, 100, 100)
preto = (0, 0, 0)
cor_texto = (150, 30, 30)
cor_hora = (20, 210, 20)
(largura, altura) = (400, 150)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Relógio")
fonte1 = pygame.font.SysFont('freesansbold.ttf', 60)
fonte2 = pygame.font.SysFont('gubbi.ttf', 30)
tela.fill(cor_de_fundo)
pygame.display.flip()

rodar = True
while (rodar):

	horario = datetime.datetime.today()
	mes = horario.month
	mes_n = mes_nome(mes)
	dia = horario.day
	ano = horario.year
	dia_semana = dia_da_semana(datetime.datetime.today().weekday())
	hora = horario.hour
	minuto = horario.minute
	segundo = horario.second


	hora_atual = fonte1.render(f"{hora:02d}:{minuto:02d}:{segundo:02d}", True, cor_hora, preto)
	dia_atual = fonte2.render(f"{dia}/{mes_n}/{ano} - {dia_semana}", True, cor_texto, preto)


	tela.blit(dia_atual, (20//2, 10//2))
	tela.blit(hora_atual, (220//2, 130//2))

	
	for evento in pygame.event.get():
		if (evento.type == pygame.QUIT):
			rodar = False


	pygame.display.update()	