from random import choice

from Dicas import Dicas


class Pessoas:
    def __init__(self) -> None:
        self.__pessoas = ["clebinho", "bona", "esther", "dona", "vanessa"]

    def sortear(self):
        pessoa_sorteada = choice(self.__pessoas)
        if pessoa_sorteada == "clebinho":
            lista_clebinho = ["clebinho",
                              "Homem",
                              "Usa óculos",
                              "Instrutor",
                              "Da aula de python",
                              "O aluno mais fraco é o einsten"]
            clebinho = Clebinho(lista=lista_clebinho)
            pessoa_clebinho = clebinho.criar_pessoa()
            return pessoa_clebinho
        elif pessoa_sorteada == "bona":
            lista_bona = ["bona",
                          "Homem",
                          "Não usa óculos",
                          "Aluno",
                          "O mais lindo de campinas e região",
                          "Provavelmente a reencarnação de einsten"]
            bonaretti = Bona(lista=lista_bona)
            pessoa_bona = bonaretti.criar_pessoa()
            return pessoa_bona
        elif pessoa_sorteada == "esther":
            lista_esther = ["esther",
                            "Mulher",
                            "Não usa óculos",
                            "Aluno",
                            "Gosta de carro",
                            "Fala em hebraico"]
            esther = Esther(lista=lista_esther)
            pessoa_esther = esther.criar_pessoa()
            return pessoa_esther
        elif pessoa_sorteada == "dona":
            lista_dona = ["dona",
                          "Homem",
                          "Usa óculos",
                          "Chefe",
                          "Parecido com um protagonista de um filme",
                          "Pode te dar um aumento"]
            dona = Dona(lista=lista_dona)
            pessoa_dona = dona.criar_pessoa()
            return pessoa_dona
        elif pessoa_sorteada == "vanessa":
            lista_vanessa = ["vanessa",
                             "Mulher",
                             "Usa óculos",
                             "Instrutor",
                             "Da aula de englis",
                             "Sumida nas aulas para DS6"]
            vanessa = Vanessa(lista=lista_vanessa)
            pessoa_vanessa = vanessa.criar_pessoa()
            return pessoa_vanessa


class Pessoa:
    def __init__(self, lista):
        self.nome_c = lista[0]
        self.genero_c = lista[1]
        self.oculos_c = lista[2]
        self.cargo_c = lista[3]
        self.dica1_c = lista[4]
        self.dica2_c = lista[5]

    def criar_pessoa(self):
        pessoa_objeto = Dicas.criar_pessoa(nome_c=self.nome_c,
                                           genero_c=self.genero_c,
                                           oculos_c=self.oculos_c,
                                           cargo_c=self.cargo_c,
                                           dica1_c=self.dica1_c,
                                           dica2_c=self.dica2_c)
        return pessoa_objeto

    def printpessoa(self):
        print("A pessoa é {}")


class Clebinho(Pessoa):
    def __init__(self, lista):
        super().__init__(lista)

    def printpessoa(self):
        print("A pessoa é o clebinho")


class Bona(Pessoa):
    def __init__(self, lista):
        super().__init__(lista)

    def printpessoa(self):
        print("A pessoa é o bona")


class Esther(Pessoa):
    def __init__(self, lista):
        super().__init__(lista)

    def printpessoa(self):
        print("A pessoa é a esther")


class Dona(Pessoa):
    def __init__(self, lista):
        super().__init__(lista)

    def printpessoa(self):
        print("A pessoa é o doná")


class Vanessa(Pessoa):
    def __init__(self, lista):
        super().__init__(lista)

    def printpessoa(self):
        print("A pessoa é a vanessa")
