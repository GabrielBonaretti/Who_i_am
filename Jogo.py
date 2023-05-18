import os
from time import time
from random import choice

from Pessoas import Pessoas
from Pandas import Pandas


class Jogo:
    def __init__(self):
        '''
        Construtor da classe Jogo
        '''
        self.dicas = []
        self.dicas_reserva = []
        self.pts = 2500
        self.time_init = 0
        self.pessoa_sorteada = ''

    def adicionando_lista(self):
        '''
        Sorteia uma das pessoas e busca a dica das mesmas. Adicionando-as na lista self.dicas
        :return:
        '''
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

    def inicio_jogo(self):
        '''
        Lógica do jogo, com a apresentação das dicas da pessoa sorteada. Juntamente com a declaração do nome do user,
        tambem pergunta se a pessoa quer registrar sua jogada com a biblioteca panda.
        '''
        os.system('cls')
        nome_usuario = input("Digite o nome do usuario: ")
        os.system('cls')

        self.adicionando_lista()
        self.pessoa_sorteada = self.dicas[0]
        self.dicas.remove(self.pessoa_sorteada)

        for i in range(6):
            self.time_init = time()
            chute = self.dica()
            if chute == self.pessoa_sorteada:
                self.acertou()
                break
            elif chute == "Senai@Mange":
                self.senha()
                break
            else:
                print("Não é esse não")

            self.pts -= 500
            if i == 5:
                self.pts = 0
                print("Você errou, a pessoa era {}, você ganhou {} pontos.".format(self.pessoa_sorteada, round(self.pts)))
                break

            os.system('cls')

        while True:
            panda = Pandas()
            escolha = input("Deseja registrar sua resposta [S/N]? ").upper()
            if escolha == "S":
                panda.write(pts=self.pts, nome_usuario=nome_usuario)
                os.system('cls')
                break

            if escolha == "N":
                os.system('cls')
                break

    def dica(self):
        '''
        Mostra a dica sorteada e o tanto de dicas restantes.
        :return: Retorna o chute do usuario da pessoa sorteada
        '''
        print("Você tem {} dicas".format(len(self.dicas)))
        dica = choice(self.dicas)
        print(dica)
        self.dicas.remove(dica)
        self.dicas_reserva.append(dica)
        chute = input("Chute a pessoa que voce acha que é: ").title()
        return chute

    def acertou(self):
        '''
        Se a pessoa acertou, logica de conclusao do jogo, junto com os pontos e também arruma a lista de dicas.
        '''
        time_acertou = self.time_init - time()
        pts_perdido = time_acertou * 25
        if pts_perdido > 250:
            pts_perdido = 250
        self.pts -= abs(pts_perdido)
        print("Parabéns você acertou, é o {}, você ganhou {} pontos.".format(self.pessoa_sorteada, round(self.pts)))
        for i in self.dicas_reserva:
            self.dicas.append(i)
        self.dicas_reserva.clear()

    def senha(self):
        '''
        Se a pessoa souber a senha, lógica de conclusão de jogo. Arrumando a lista de dicas alem de lista de dicas reservas.
        :return:
        '''
        self.pts = 8000
        print("Parabéns você acertou, é o {}, você ganhou {} pontos.".format(self.pessoa_sorteada, round(self.pts)))
        for i in self.dicas_reserva:
            self.dicas.append(i)
        self.dicas_reserva.clear()
        print("chegou")