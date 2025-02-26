from funcoes.func import desconto

totprod = 0
totdesc = 0
total = 0
totproddesc = 0
while True:
    produto = float(input('Valor do produto: '))
    totprod += 1
    if produto >= 100:
        totdesc += 1
        produto = produto - desconto(produto)
        total += produto
    else:
        total += produto
    decide = int(input("Adicionar mais produtos? [1] Sim [2] Não: "))
    if decide == 2:
        print(f"Total de produtos: {totprod}")
        print(f"Total de produtos com descontos: {totdesc}")
        print(f"Total a pagar: {total}")
        break
