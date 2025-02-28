from funcoes.desconto import desconto
from funcoes.transforma import transfstr
from funcoes.contas import criar_conta, fazer_login

# Criação das variáveis
totprod = 0
totdesc = 0
total = 0
totproddesc = 0
listname = []
listprice = []


print("WELCOME TO THE SALE SYSTEM\n")
print("DO YOU HAVE AN ACCOUNT?")
resp = str(input("[1] YES   or   [2] NO\n"))
if resp == "1":
    fazer_login()
else:
    criar_conta()


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
