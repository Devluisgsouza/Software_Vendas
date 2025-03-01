def vender_produto():
    print("WELCOME TO SALES SYSTEM!")
    print("\nPRODUCTS OVER R$100.00 HAVE A 10% DISCOUNT!\n")
    total = 0
    totprod = 0
    totdesc = 0
    sacola = []
    while True:
        name = input("Product's name: ")
        price = float(input(f"Product's price: ").replace(",","."))
        sacola.append((name,price))
        with open("main/banco_de_dados/price.txt", "a") as arquivo:
            arquivo.write(f"\n{price}")
        with open("main/banco_de_dados/name.txt", "a") as arquivo:
            arquivo.write(f"\n{name}")
        if price < 100:
            total += price
            totprod += 1
        else:
            price = price - (price * 0.1)
            totdesc += 1
            total += price
            totprod += 1
        decide = int(input("Add more products? [1] Yes [2] No: "))
        if decide == 2:
            print(f"\nTotal products: {totprod}")
            print(f"Total products on sale: {totdesc}")
            print(f"Total to pay: {total}")
            print("\nYOUR BAG: ")
            for name, price in sacola:
                print(f"{name}  -  R${price}")
            break
