import os

from Jogo import Jogo
from Pandas import Pandas


def main():
    '''

    :return:
    '''
    while True:
        jogo = Jogo()
        panda = Pandas()
        while True:
            os.system('cls')
            try:
                print("Escolha: ")
                print("[1] Começar")
                print("[2] Mostrar classificação")
                print("[3] Sair")
                escolha = int(input("Dgitie sua escolha: "))
                if 0 < escolha < 3:
                    break
            except:
                print("só numero lula!")
        if escolha == 1:
            jogo.inicio_jogo()
        elif escolha == 2:
            os.system('cls')
            panda.read()
            input("")
            os.system('cls')
        else:
            print("erro")


if __name__ == "__main__":
    main()
