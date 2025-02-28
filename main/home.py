from funcoes.desconto import desconto
from funcoes.transforma import transfstr

# Criação das variáveis
totprod = 0
totdesc = 0
total = 0
totproddesc = 0
listname = []
listprice = []
listlogin = []
listpass = []
listaccount = []



login = open("main/banco_de_dados/login.txt", "a")
account = open("main/banco_de_dados/accounts.txt", "a")


print("WELCOME TO THE SALE SYSTEM\n")
print("DO YOU HAVE AN ACCOUNT?")
resp = str(input("[1] YES   or   [2] NO\n"))
if resp != "1":
    print("CREATE YOUR ACCOUNT\n")
    log1 = str(input("Login: "))
    pass1 = str(input("Passwor: "))

    account.write(f"{log1},{pass1}\n")

else:
    account = open("main/banco_de_dados/accounts.txt", "r")
    print("ENTER WITH YOUR ACCOUNT\n")
    log2 = str(input("Login: "))
    pass2 = str(input("Passwor: "))
    login.write(f"{log2},{pass2}\n")
    if login.readline() in account.readlines():
        print("open")
account.close()
login.close()







