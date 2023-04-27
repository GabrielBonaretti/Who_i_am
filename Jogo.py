import os
from time import time
from random import choice

from prettytable import PrettyTable

from Pessoas import Pessoas
from Pandas import Pandas



class Jogo:
    def __init__(self):
        self.dicas = []
        self.dicas_reserva = []

    def adicionando_lista(self):
        pessoas = Pessoas()
        pessoa_sorteada = pessoas.sortear()

        for i in range(7):
            if i == 0:
                self.dicas.append(pessoa_sorteada.nome)
            elif i == 1:
                self.dicas.append(pessoa_sorteada.setor)
            elif i == 2:
                self.dicas.append(pessoa_sorteada.genero)
            elif i == 3:
                self.dicas.append(pessoa_sorteada.oculos)
            elif i == 4:
                self.dicas.append(pessoa_sorteada.cargo)
            elif i == 5:
                self.dicas.append(pessoa_sorteada.dica1)
            elif i == 6:
                self.dicas.append(pessoa_sorteada.dica2)

    def inicio_jogo(self, placar):
        pts = 2500
        os.system('cls')
        nome_usuario = input("Digite o nome do usuario: ")
        os.system('cls')
        self.adicionando_lista()
        pessoa_sorteada = self.dicas[0]
        self.dicas.remove(pessoa_sorteada)
        for i in range(5):
            time_init = time()
            print("Você tem {} dicas".format(len(self.dicas)))
            dica = choice(self.dicas)
            print(dica)
            self.dicas.remove(dica)
            self.dicas_reserva.append(dica)
            chute = input("Chute a pessoa que voce acha que é: ").title()
            if chute == pessoa_sorteada:
                time_acertou = time_init - time()
                pts_perdido = time_acertou * 25
                if pts_perdido > 250:
                    pts_perdido = 250
                pts -= abs(pts_perdido)
                print("Parabéns você acertou, é o {}, você ganhou {} pontos.".format(pessoa_sorteada, round(pts)))
                for i in self.dicas_reserva:
                    self.dicas.append(i)
                self.dicas_reserva.clear()
                break
            elif chute == "Senai@Mange":
                pts = 8000
                print("Parabéns você acertou, é o {}, você ganhou {} pontos.".format(pessoa_sorteada, round(pts)))
                for i in self.dicas_reserva:
                    self.dicas.append(i)
                self.dicas_reserva.clear()
                print("chegou")
                break
            else:
                print("Não é esse não")
            pts -= 500
            if i == 4:
                pts = 0
                print("Você errou, a pessoa era {}, você ganhou {} pontos.".format(pessoa_sorteada, round(pts)))
                break
            os.system('cls')
        while True:
            panda = Pandas()
            escolha = input("Deseja registrar sua resposta [S/N]? ").upper()
            if escolha == "S":
                panda.write(pts=pts, nome_usuario=nome_usuario)
                os.system('cls')
                break

            if escolha == "N":
                os.system('cls')
                break