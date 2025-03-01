from funcoes.contas import criar_conta, fazer_login
from funcoes.vender_produto import vender_produto
from funcoes.acessar_sistema import acessar_sistema


print("--- WELCOME TO THE SALE SYSTEM --- \n")
while True:
    print("--- DO YOU HAVE AN ACCOUNT? ---")
    resp = str(input("[1] YES   or   [2] NO\n").replace(" ","").lower())
    if resp == "1":
        fazer_login()
        acessar_sistema()
        break
    elif resp == "2":
        criar_conta()
        acessar_sistema()
        break
    else:
        print("--- I CAN'T UNDERSTAND WHAT YOU WANT ---")
        