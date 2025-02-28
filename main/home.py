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
result = []


login = open("main/banco_de_dados/login.txt", "a")
account = open("main/banco_de_dados/accounts.txt", "a")


print("WELCOME TO THE SALE SYSTEM\n")
print("DO YOU HAVE AN ACCOUNT?")
resp = str(input("[1] YES   or   [2] NO\n"))
if resp != "1":
    print("CREATE YOUR ACCOUNT\n")
    log1 = str(input("Login: "))
    pass1 = str(input("Passwor: "))
    listlogin.append(str(log1))
    listlogin.append(str(pass1))
    listaccount.append(str(listlogin))
    account.write(str(listaccount)) and account.write("\n")
    print(listlogin)
    print(listaccount)
else:
    account = open("main/banco_de_dados/accounts.txt", "r")
    print("ENTER WITH YOUR ACCOUNT\n")
    log2 = str(input("Login: "))
    pass2 = str(input("Passwor: "))
    result.append(str(log2))
    result.append(str(pass2))
    list = account.readlines()
    print(list)
    print(result)
    if result in list:
        print("open")
account.close()
login.close()







# Loop para adicionar produtos e preços
while True:
    name = open("main/banco_de_dados/name.txt", "a")
    nomeproduto = str(input("Product's name: "))
    name.write(nomeproduto) and name.write("\n")
    listname.append(nomeproduto)
    price = open("main/banco_de_dados/price.txt", "a")
    preçoproduto = float(input("Product's price: "))
    price.write(transfstr(preçoproduto)) and price.write("\n")
    listprice.append(preçoproduto)
    totprod += 1


# Verifica se o produto tem desconto, se tiver, aplica o desconto
    if preçoproduto >= 100:
        totdesc += 1
        preçoproduto = preçoproduto - desconto(preçoproduto)
        total += preçoproduto
    else:
        total += preçoproduto
    name.close()
    price.close()


# Pergunta se deseja adicionar mais produtos
    decide = int(input("Add more products? [1] Yes [2] No: "))
    if decide == 2:
        print(f"Total products: {totprod}")
        print(f"Total products on sale: {totdesc}")
        print(f"Total to pay: {total}")
        break
