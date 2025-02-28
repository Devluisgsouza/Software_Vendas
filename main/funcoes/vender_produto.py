def vendaer_produto():
    total = 0
    totprod = 0
    totdesc = 0
    while True:
        name = input("Product's name: ")
        price = int(input("Product's price: "))
        totprod += 1
        if price >= 100:
            price = price - (price * 0.1)
            totdesc += 1
            total += price

        else:
            total += price

        decide = int(input("Add more products? [1] Yes [2] No: "))
        if decide == 2:
            print(f"Total products: {totprod}")
            print(f"Total products on sale: {totdesc}")
            print(f"Total to pay: {total}")
            break
        with open("main/banco_de_dados/price.txt", "a") as arquivo:
            arquivo.write(f"\n{price}")
        with open("main/banco_de_dados/name.txt", "a") as arquivo:
            arquivo.write(f"\n{name}")
