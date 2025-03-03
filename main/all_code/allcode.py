def vender_produto():
    print(f"{"\033[1;36m WELCOME TO SALES SYSTEM! ".center(50)}")
    print(f"{"\n"}{"\033[1;34m PRODUCTS OVER R$100.00 HAVE A 10% DISCOUNT! ".center(50)}{"\n"}")
    total = 0
    totprod = 0
    totdesc = 0
    sacola = []
    while True:
        name = input("\033[1;36mProduct's name: ")
        while True:
            pricestr = input("Product's price: ").replace(",", ".").replace(" ","")
            try:
                price = float(pricestr)
                break
            except:
                print("erro")
        with open("main/banco_de_dados/price.txt", "a") as arquivo:
            arquivo.write(f"{price}\n")
        with open("main/banco_de_dados/name.txt", "a") as arquivo:
            arquivo.write(f"{name}\n")
        if price < 100:
            total += price
            totprod += 1
            sacola.append((name, price))
        else:
            price = price - (price * 0.1)
            totdesc += 1
            total += price
            totprod += 1
            sacola.append((name, price))
        while True:
            print(f"{"\n"}{"\033[1;36m ADD MORE PRODUCTS? ".center(48)}{"\n"}")
            decide = input(f"{" [1]YES   OR   [2]NO ".center(42)}{"\n"}{"\n"}").replace(" ", "").lower()
            if decide == "2":
                print(f"{"\n"}{"\033[1;33m SUMMARY OF YOUR SALE ".center(48)}")
                print(f"{"\n"}{"\033[1;33mTotal products: "}\033[1;32m{totprod}\033[m")
                print(f"{"\033[1;33mTotal products on sale: "}\033[1;32m{totdesc}\033[m")
                print(f"{"\033[1;33mTotal to pay: "}\033[1;32m{total}\033[m")
                print(f"{"\n"}{"\033[1;33m ALL PRODUCTS SOLD ".center(47)}{"\n"}")
                for name, price in sacola:
                    print(f"\033[1;33m{name}  -  \033[1;32mR${price}")
                print(f"{"\n"}{"\033[m"}")
                break
            elif decide == "1":
                break
            else:
                print(
                    f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT ".center(50)}{"\n"}")
        if decide != "1" and "2":
            break












def vender_produto():
    print(f"{"\033[1;36m WELCOME TO SALES SYSTEM! ".center(50)}")
    print(f"{"\n"}{"\033[1;34m PRODUCTS OVER R$100.00 HAVE A 10% DISCOUNT! ".center(50)}{"\n"}")
    total = 0
    totprod = 0
    totdesc = 0
    sacola = []
    while True:
        name = input("\033[1;36mProduct's name: ")
        price = float(input("Product's price: ").replace(",", ".").replace(" ",""))
        with open("main/banco_de_dados/price.txt", "a") as arquivo:
            arquivo.write(f"{price}\n")
        with open("main/banco_de_dados/name.txt", "a") as arquivo:
            arquivo.write(f"{name}\n")
        if price < 100:
            total += price
            totprod += 1
            sacola.append((name, price))
        else:
            price = price - (price * 0.1)
            totdesc += 1
            total += price
            totprod += 1
            sacola.append((name, price))
        while True:
            print(f"{"\n"}{"\033[1;36m ADD MORE PRODUCTS? ".center(48)}{"\n"}")
            decide = input(f"{" [1]YES   OR   [2]NO ".center(42)}{"\n"}{"\n"}").replace(" ", "").lower()
            if decide == "2":
                print(f"{"\n"}{"\033[1;33m SUMMARY OF YOUR SALE ".center(48)}")
                print(f"{"\n"}{"\033[1;33mTotal products: "}\033[1;32m{totprod}\033[m")
                print(f"{"\033[1;33mTotal products on sale: "}\033[1;32m{totdesc}\033[m")
                print(f"{"\033[1;33mTotal to pay: "}\033[1;32m{total}\033[m")
                print(f"{"\n"}{"\033[1;33m ALL PRODUCTS SOLD ".center(47)}{"\n"}")
                for name, price in sacola:
                    print(f"\033[1;33m{name}  -  \033[1;32mR${price}")
                print(f"{"\n"}{"\033[m"}")
                break
            elif decide == "1":
                break
            else:
                print(
                    f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT ".center(50)}{"\n"}")
        if decide != "1" and "2":
            break