class Dicas:
    setor = "ETS"

    def __init__(self, nome, setor, genero, oculos, cargo, dica1, dica2):
        '''
        Cria o objeto Dicas, no qual busca as caracteristicas ou dicas da pessoa criada.
        :param nome: nome da pessoa, str
        :param setor: setor da pessoa, str
        :param genero: genero da pessoa, str
        :param oculos: se a pessoa usa óculos, str
        :param cargo: cargo da pessoa, str
        :param dica1: dica génerica 1 da pessoa, str
        :param dica2: dica génerica 2 da pessoa, str
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
        Um método estático que obtem a variável "setor" da classe Dicas.
        :return: variável setor
        '''
        return Dicas.setor

    @classmethod
    def criar_pessoa(cls, nome_c, genero_c, oculos_c, cargo_c, dica1_c, dica2_c):
        '''
        O classmethod verifica se as caracteristicas da pessoa estão vazias ou não. Se sim ele não cria o objeto dicas, caso não ele cria.
        :param nome_c: nome da pessoa, str
        :param genero_c: genero da pessoa, str
        :param oculos_c: se a pessoa usa óculos, str
        :param cargo_c: cargo da pessoa, str
        :param dica1_c: dica génerica 1 da pessoa, str
        :param dica2_c: dica génerica 2 da pessoa, str
        :return: retorna o objeto pessoa com dicas.
        '''
        nome_c = nome_c.title()
        if nome_c == '' or nome_c == '' or oculos_c == '' or cargo_c == '' or dica1_c == '' or dica2_c == '':
            print("foi nao")
        else:
            return cls(nome=nome_c, setor=cls.obter_setor(), genero=genero_c, oculos=oculos_c,
                       cargo=cargo_c, dica1=dica1_c, dica2=dica2_c)

