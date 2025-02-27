from funcoes.func import desconto

# Cria as variáveis
totprod = 0
totdesc = 0
total = 0
totproddesc = 0

# Loop para adicionar produtos
while True: 
    produto = float(input('Valor do produto: '))
    totprod += 1

# Verifica se o produto tem desconto, se tiver, aplica o desconto
    if produto >= 100:
        totdesc += 1
        produto = produto - desconto(produto)
        total += produto
    else:
        total += produto

# Pergunta se deseja adicionar mais produtos
    decide = int(input("Adicionar mais produtos? [1] Sim [2] Não: "))
    if decide == 2:
        print(f"Total de produtos: {totprod}")
        print(f"Total de produtos com descontos: {totdesc}")
        print(f"Total a pagar: {total}")
        break
