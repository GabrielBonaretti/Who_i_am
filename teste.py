import pandas as pd

def read():
    df = pd.read_excel('teste.xlsx')
    print(df)

def write():
    df = pd.DataFrame([["bona", 123123], ["felps", 123], ["mandy", 2]],
                  index=[1, 2, 3], columns=['nick name', 'pontos']).to_excel('teste.xlsx', sheet_name="Planilha1")
    print(df)

write()
read()
