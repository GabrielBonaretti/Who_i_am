import pandas as pd
from prettytable import PrettyTable

class Pandas:
    def __init__(self) -> None:
        self.file_name = 'teste.xlsx'
        self.sheet_name = "Planilha1"
        self.placar = {}

    def write(self, pts, nome_usuario):
        self.placar[pts] = nome_usuario

        df = pd.read_excel(self.file_name)
        
        nick_names = list(df['nick name'])
        pontos = list(df['pontos'])

        for i in range(len(pontos)):
            self.placar[pontos[i]] = nick_names[i]

        lista = []
        index = []
        myKeys = list(self.placar.keys())
        myKeys.sort(reverse=1)
        sorted_dict = {i:  self.placar[i] for i in myKeys}
        myTable = PrettyTable(["Classificação", "Nick name", "Pontos"])
        for i in range(len(sorted_dict)):
            myTable.add_row(["{}º".format(i + 1), "{}".format(list(sorted_dict.values())[i]), "{}".format(round(list(sorted_dict.keys())[i]))])
            lista.append(["{}º".format(i + 1), "{}".format(list(sorted_dict.values())[i]), "{}".format(round(list(sorted_dict.keys())[i]))])
            index.append(i+1)

        df = pd.DataFrame(lista,index=index, columns=['classificacao','nick name', 'pontos']).to_excel('teste.xlsx', sheet_name="Planilha1")

        self.placar.clear()
        lista.clear()
        index.clear()

    def read(self):
        df = pd.read_excel(self.file_name)
        
        nick_names = list(df['nick name'])
        pontos = list(df['pontos'])

        for i in range(len(pontos)):
            self.placar[pontos[i]] = nick_names[i]

        myKeys = list(self.placar.keys())
        myKeys.sort(reverse=1)
        sorted_dict = {i:  self.placar[i] for i in myKeys}
        myTable = PrettyTable(["Classificação", "Nick name", "Pontos"])
        for i in range(len(sorted_dict)):
            myTable.add_row(["{}º".format(i + 1), "{}".format(list(sorted_dict.values())[i]), "{}".format(round(list(sorted_dict.keys())[i]))])
        
        print(myTable)
        self.placar.clear()