from funcoes.contas import criar_conta, fazer_login
from funcoes.acessar_sistema import acessar_sistema


print(
    f"{"\n"}{"\033[1;32m WELCOME TO THE SALES SYSTEM \033[m".center(54)}{"\n"}")
while True:
    print(f"{"\n"}{"\033[1;36m DO YOU HAVE AN ACCOUNT? ".center(52)}\n")
    resp = str(input(f"{" [1]YES   or   [2]NO ".center(45)}{"\n"}{"\n"}").replace(" ", "").lower())
    if resp == "1":
        fazer_login()
        acessar_sistema()
        break
    elif resp == "2":
        criar_conta()
        acessar_sistema()
        break
    else:
        print(f"{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT \033[m".center(55)}{"\n"}")


