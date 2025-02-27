from funcoes.desconto import desconto
from funcoes.transforma import transfstr

# Criação das variáveis
totprod = 0
totdesc = 0
total = 0
totproddesc = 0




print("WELCOME TO SALES SYSTEM")


# Loop para adicionar produtos
name = open("main/banco_de_dados/nome.txt", "x")
price = open("main/banco_de_dados/price.txt", "x")


while True:
    nomeproduto = str(input("Product's name: "))
    name.write(nomeproduto)
    preçoproduto = float(input("Product's price: "))
    price.write(transfstr(preçoproduto))
    totprod += 1
# Verifica se o produto tem desconto, se tiver, aplica o desconto
    if preçoproduto >= 100:
        totdesc += 1
        preçoprodutoproduto = preçoprodutoproduto - desconto(preçoproduto)
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
