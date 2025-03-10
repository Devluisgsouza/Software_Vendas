from datetime import datetime
import openpyxl as op

tempo = datetime.now().date()
data = tempo.strftime("%d/%m/%Y")
vendas = []
sair = True

book = op.load_workbook("main\\banco_de_dados\\banco.xlsx")
banco = book["banco_de_dados"]


def vender_prod():
    print(f"{"\n"}{"\033[1;36m WELCOME TO SALES SYSTEM! ".center(50)}{"\n"}")
    print(f"{"\033[1;36m PUT ALL THE PRODUCTS YOU'VE SOLD ".center(50)}{"\n"}")
    print(f"{"\n"}{"\033[1;34m PRODUCTS OVER R$100.00 HAVE A 10% DISCOUNT! ".center(50)}{"\n"}")
    print(f"{"IF YOU WANT TO RETURN TO MENU, TYPE 'EXIT'".center(44)}{"\n"}")

    total = 0
    totprod = 0
    totdesc = 0
    sacola = []
    exit = False

    while True:
        if exit:
                break
        while True:
            name = input(f"\033[1;36m{"\n"}{"Product's name: "}").lower().strip()
            if name == "":
                print(
                    f"{"\n"}{"\033[1;31m ERROR! ENTER A VALID NAME \033[m".center(51)}{"\n"}")
            elif name == "exit".strip().lower():
                return exit
            else:
                break
        while True:
            pricestr = input("\033[1;36mProduct's price: ").replace(",",".").strip().lower()
            if pricestr == "exit".strip().lower():
                return exit
            try:
                price = float(pricestr)
                break
            except:
                print(
                    f"{"\n"}{"\033[1;31m ERROR! ENTER A VALID PRICE \033[m".center(52)}{"\n"}")
        if price < 100:
            total += price
            totprod += 1
            sacola.append((name, price))
            with open("main/banco_de_dados/price.txt", "a") as arquivo:
                arquivo.write(f"\n{price}")
            with open("main/banco_de_dados/name.txt", "a") as arquivo:
                arquivo.write(f"{name}\n")
            with open("main/banco_de_dados/vendas.txt", "a") as arquivo:
                arquivo.write(f"{"\n"}{name},{price},{data}")
            banco.append([name,price,data])
            book.save("main\\banco_de_dados\\banco.xlsx")
        else:
            price = price - (price * 0.1)
            totdesc += 1
            total += price
            totprod += 1
            sacola.append((name, price))
            with open("main/banco_de_dados/price.txt", "a") as arquivo:
                arquivo.write(f"{price}\n")
            with open("main/banco_de_dados/name.txt", "a") as arquivo:
                arquivo.write(f"{name}\n")
            with open("main/banco_de_dados/vendas.txt", "a") as arquivo:
                arquivo.write(f"{"\n"}{name},{price},{data}")
            banco.append([name,price,data])
            book.save("main\\banco_de_dados\\banco.xlsx")
        while True:
            print(f"{"\n"}{"\033[1;36m ADD MORE PRODUCTS? ".center(48)}{"\n"}")
            decide = input(f"{" [1]YES   OR   [2]NO ".center(42)}{"\n"}{"\n"}").replace(
                " ", "").lower()
            if decide == "2":
                print(f"{"\n"}{"\033[1;33m SUMMARY OF YOUR SALE ".center(48)}")
                print(
                    f"{"\n"}{"\033[1;33mTotal products: ".ljust(35)}\033[1;32m{totprod}\033[m")
                print(
                    f"{"\033[1;33mTotal products on sale: ".ljust(35)}\033[1;32m{totdesc}\033[m")
                print(
                    f"{"\033[1;33mTotal to pay: ".ljust(35)}\033[1;32mR${total:.2f}\033[m")
                print(
                    f"{"\n"}{"\033[1;33m ALL PRODUCTS SOLD ".center(47)}{"\n"}")
                for name, price in sacola:
                    print(f"\033[1;33m{name}{"    -    "}\033[1;32mR${price:.2f}")
                print(f"{"\n"}{"\033[m"}")
                break
            elif decide == "1":
                break
            else:
                print(
                    f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT ".center(50)}{"\n"}")
        if decide != "1" and "2":
            break

book.save("main\\banco_de_dados\\banco.xlsx")

#vender_prod()
