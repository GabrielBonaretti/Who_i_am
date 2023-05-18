import pandas as pd
from prettytable import PrettyTable

class Pandas:
    def __init__(self) -> None:
        '''
        Cria classe pandas
        '''
        self.file_name = 'teste.xlsx'
        self.sheet_name = "Planilha1"
        self.placar = {}

    def write(self, pts, nome_usuario):
        '''
        Escreve a nova tabela com os novos pontos da pessoa
        :param pts: entrada de pontos da nova jogada, double
        :param nome_usuario: entrada de nick da nova jogada, str
        '''
        df = pd.read_excel(self.file_name)
        
        nick_names = list(df['nick name'])
        pontos = list(df['pontos'])

        for i in range(len(pontos)):
           self.placar[nick_names[i]] = pontos[i]

        self.placar[nome_usuario] = pts

        lista = []
        index = []

        sorted_dict = sorted(self.placar.items(), key=lambda x:x[1], reverse=1)
        
        myTable = PrettyTable(["Classificação", "Nick name", "Pontos"])
        for i in range(len(sorted_dict)):
            myTable.add_row(["{}º".format(i + 1), "{}".format(sorted_dict[i][0]), "{}".format(round(sorted_dict[i][1]))])
            lista.append(["{}º".format(i + 1), "{}".format(sorted_dict[i][0]), "{}".format(round(sorted_dict[i][1]))])
            index.append(i+1)

        df = pd.DataFrame(lista,index=index, columns=['classificacao','nick name', 'pontos']).to_excel('teste.xlsx', sheet_name="Planilha1")

        self.placar.clear()
        lista.clear()
        index.clear()

    def read(self):
        '''
        Ler a tabela do excel e printa no terminal com o pretty table
        '''
        df = pd.read_excel(self.file_name)
        
        nick_names = list(df['nick name'])
        pontos = list(df['pontos'])
        
        for i in range(len(pontos)):
           self.placar[nick_names[i]] = pontos[i]
           
        sorted_dict = sorted(self.placar.items(), key=lambda x:x[1], reverse=1)
        
        myTable = PrettyTable(["Classificação", "Nick name", "Pontos"])
        for i in range(len(sorted_dict)):
            myTable.add_row(["{}º".format(i + 1), "{}".format(sorted_dict[i][0]), "{}".format(round(sorted_dict[i][1]))])
        
        print(myTable)
        self.placar.clear()