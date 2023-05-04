class Dicas:
    setor = "ETS"

    def __init__(self, nome, setor, genero, oculos, cargo, dica1, dica2):
        '''

        :param nome:
        :param setor:
        :param genero:
        :param oculos:
        :param cargo:
        :param dica1:
        :param dica2:
        '''
        self.nome = nome
        self.setor = setor
        self.genero = genero
        self.oculos = oculos
        self.cargo = cargo
        self.dica1 = dica1
        self.dica2 = dica2

    @staticmethod
    def obter_setor():
        '''

        :return:
        '''
        return Dicas.setor

    @classmethod
    def criar_pessoa(cls, nome_c, genero_c, oculos_c, cargo_c, dica1_c, dica2_c):
        '''

        :param nome_c:
        :param genero_c:
        :param oculos_c:
        :param cargo_c:
        :param dica1_c:
        :param dica2_c:
        :return:
        '''
        nome_c = nome_c.title()
        if nome_c == '' or nome_c == '' or oculos_c == '' or cargo_c == '' or dica1_c == '' or dica2_c == '':
            print("foi nao")
        else:
            return cls(nome=nome_c, setor=cls.obter_setor(), genero=genero_c, oculos=oculos_c,
                       cargo=cargo_c, dica1=dica1_c, dica2=dica2_c)

