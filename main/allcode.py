
def criar_conta():
    print(f"{"\n"}{"\033[1;36m CREATE YOUR ACCOUNT ".center(52)}{"\n"}")
    while True:
        login = input("\033[1;32mEmail: ").replace("@","").replace(".","")
        password = input("\033[1;32mPassword: ")
        with open("main/banco_de_dados/logins.txt","r") as arquivo:
            conteudo = arquivo.readlines()
            for line in conteudo:
                if login in line.strip().split("\n"):
                    print(f"{"\n"}{"\033[1;31m THIS ACCOUNT ALREADY EXISTS IN THE SYSTEM \033[m".center(52, "=")}{"\n"}")
                    break
            else:
                with open("main/banco_de_dados/logins.txt","a") as arquivo:
                    arquivo.write(f"{login}\n")
                with open("main/banco_de_dados/passwords.txt","a") as arquivo:
                    arquivo.write(f"{password}\n")
                print(f"{"\n"}{"\033[1;32m ACCOUNT CREATED SUCCESSFULY! \033[m".center(54)}")
                with open("main/banco_de_dados/accounts.txt", "a") as arquivo:
                    arquivo.write(f"{login},{password}\n")
                    break
    

def fazer_login():
    print(f"{"\n"}{"\033[1;36m ENTER WITH YOUR ACCOUNT: ".center(52)}{"\n"}")
    login = input("\033[1;32mEmail: ")
    password = input("Password: ")
    with open("main/banco_de_dados/accounts.txt", "r") as arquivo:
        contas = arquivo.readlines()
    for conta in contas:
        login_salvo, senha_salva = conta.strip().split(",")
        if login == login_salvo and password == senha_salva:
            print(f"{"\n"}{"\033[1;32m SUCCESSFULLY LOGIN \033[m".center(51)}")
            return
    print(f"{"\n"}{"\033[1;31m WRONG INFORMATIONS! \033[m".center(54)}")
    while True:
        print(f"{"\n"}{"\033[1;36m WOULD YOU LIKE TO CREATE A NEW ACCOUNT? ".center(53)}{"\n"}")
        resp = input(f"{" [1]YES   OR   [2]NO ".center(44)}{"\n"}{"\n"}").replace(" ","").lower()
        if resp == "1":
            criar_conta()
            break
        elif resp == "2":
            fazer_login()
            break
        else:
            print(f"{"\n"}{"\033[1;31mI CAN'T UNDERSTAND WHAT YOU WANT\033[m".center(53)}")

from datetime import datetime

tempo = datetime.now().date()
data = tempo.strftime("%d/%m/%Y")
hora = datetime.now().time()
vendas = []

def vender_prod():
    print(f"{"\n"}{"\033[1;36m WELCOME TO SALES SYSTEM! ".center(50)}")
    print(
        f"{"\n"}{"\033[1;34m PRODUCTS OVER R$100.00 HAVE A 10% DISCOUNT! ".center(50)}{"\n"}")
    print(f"{"\033[1;36m PUT ALL THE PRODUCTS YOU'VE SOLD ".center(50)}{"\n"}")
    total = 0
    totprod = 0
    totdesc = 0
    sacola = []
    while True:
        name = input("\033[1;36mProduct's name: ").lower().strip()
        while True:
            pricestr = input("\033[1;36mProduct's price: ").replace(",", ".").replace(" ", "")
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
                arquivo.write(f"{price}\n")
            with open("main/banco_de_dados/name.txt", "a") as arquivo:
                arquivo.write(f"{name}\n")
            with open("main/banco_de_dados/vendas.txt", "a") as arquivo:
                arquivo.write(f"{"\n"}{name},{price},{data}")
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
        while True:
            print(f"{"\n"}{"\033[1;36m ADD MORE PRODUCTS? ".center(48)}{"\n"}")
            decide = input(f"{" [1]YES   OR   [2]NO ".center(42)}{"\n"}{"\n"}").replace(
                " ", "").lower()
            if decide == "2":
                print(f"{"\n"}{"\033[1;33m SUMMARY OF YOUR SALE ".center(48)}")
                print(
                    f"{"\n"}{"\033[1;33mTotal products: "}\033[1;32m{totprod}\033[m")
                print(
                    f"{"\033[1;33mTotal products on sale: "}\033[1;32m{totdesc}\033[m")
                print(
                    f"{"\033[1;33mTotal to pay: "}\033[1;32mR${total:.2f}\033[m")
                print(
                    f"{"\n"}{"\033[1;33m ALL PRODUCTS SOLD ".center(47)}{"\n"}")
                for name, price in sacola:
                    print(f"\033[1;33m{name}  -  \033[1;32mR${price:.2f}")
                print(f"{"\n"}{"\033[m"}")
                break
            elif decide == "1":
                break
            else:
                print(
                    f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT ".center(50)}{"\n"}")
        if decide != "1" and "2":
            break



def vendashist():
    while True:
        print(f"{"\n"}{"\033[1;34mSYSTEM SALES HISTORY".center(49)}\n")
        print(f"{"DO YOU WANT TO SEARCH BY:  ".center(49)}{"\n"}")
        print("[1] PRODUCT NAME ".center(39))
        print("[2] PRODUCT PRICE ".center(39))
        print("[3] DATE OF SALE ".center(39))
        print("[4] RETURN TO MENU ".center(41))
        resp = input("\n")
        with open("main/banco_de_dados/vendas.txt", "r") as arquivo:
            vendas = arquivo.readlines()
        if resp == "1":
            resp2 = input(f"{"\n"}{"\033[1;36mENTER THE PRODUCT NAME: ".center(50)}{"\n"}{"\n"}\033[1;32m").strip().lower()
            print(f"{"\n"}{"\033[1;36mPRODUCT HISTORY WITH NAME: ".center(47)}\033[1;32m{resp2}{"\n"}")
            print(f"{"\n"}{"\033[1;36mNAME , PRICE , DATE\033[m\n\033[1;32m"}")
            for item in vendas:
                if resp2 in item:
                    print(item)


        elif resp == "2":
            resp3 = input(f"{"\n"}{"\033[1;36mENTER THE PRODUCT PRICE: ".center(50)}{"\n"}{"\n"}\033[1;32m").replace(",", ".").strip()
            resp3float = float(resp3)
            resp3str = str(resp3float)            
            print(f"{"\n"}{"\033[1;36mPRODUCT HISTORY WITH PRICE: ".center(47)}\033[1;32m{resp3float}{"\n"}")
            print(f"{"\n"}{"\033[1;36mNAME , PRICE , DATE\033[m\n\033[1;32m"}")
            for item in vendas:
                if resp3str in item.strip().split(","):
                    print(item)
                

        elif resp == "3":
            resp4 = input(f"{"\n"}{"\033[1;36mENTER THE PRODUCT DATE: ".center(50)}{"\n"}{"\n"}\033[1;32m").replace("-", "/").strip()
            print(f"{"\n"}{"\033[1;36mPRODUCT HISTORY WITH DATE: ".center(47)}\033[1;32m{resp4}{"\n"}")
            print(f"{"\n"}{"\033[1;36mNAME , PRICE , DATE\033[m\n\033[1;32m"}")
            for item in vendas:
                if resp4 in item.strip().split(","):
                    print(item)

        elif resp == "4":
            break
        else:
            print(f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT! ".center(49)}")

            
def menusystem():
    print(f"{"\n"}{"\033[1;36m SYSTEM MENU" .center(40)}{"\n"}")
    print(" [1] ACCESS THE SYSTEM ".center(43))
    print(" [2] CHANGE ACCOUNT ".center(39))
    print(" [3] SALES HISTORY ".center(39))
    print(f"{" [4] CLOSE SYSTEM ".center(37)}{"\n"}")


def menusystem2():
    print("\033[1;36m WHAT YOU WANT TO DO? ".center(49))
    print(f"{"\n"}{"[1] NEW SALE".center(33)}")
    print(f"{"[2] CHANGE ACCOUNT".center(40)}")
    print(f"{"[3] RETURN TO MENU".center(40)}")
    print(f"{"[4] LOGOUT".center(31)}{"\n"}")

from funcoes.contas import criar_conta, fazer_login
from funcoes.vender_produto import vender_prod
from funcoes.vendas import vendashist
from main.funcoes.menu import menusystem, menusystem2


print(f"{"\n"}{"\033[1;32m WELCOME TO THE SALES SYSTEM \033[m".center(54)}{"\n"}")
while True:
    print(f"{"\033[1;36m DO YOU HAVE AN ACCOUNT? ".center(52)}\n")
    resp = str(input(f"{" [1]YES   or   [2]NO ".center(45)}{"\n"}{"\n"}").replace(" ", "").lower())
    if resp == "1":
        fazer_login()
        while True:
            menusystem()
            resp2 = input(f"{" WHAT YOU WANT TO DO? ".center(42)}{"\n"}{"\n"}")
            match resp2:
                case "1":
                    break
                case "2":
                    fazer_login()
                case "3":
                    vendashist()
                case "4":
                    print(f"{"\n"}{"\033[1;32m SEE YOU SOON! \033[m".center(52)}{"\n"}")
                    exit()
                case _:
                    print(f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT! ".center(47)}")
        vender_prod()
        break
    elif resp == "2":
        criar_conta()
        while True:
            menusystem()
            resp3 = input(f"{" WHAT YOU WANT TO DO? ".center(42)}{"\n"}{"\n"}")
            match resp3:
                case "1":
                    break
                case "2":
                    fazer_login()
                case "3":
                    vendashist()
                case "4":
                    print(f"{"\n"}{"\033[1;32m SEE YOU SOON! \033[m".center(52)}{"\n"}")
                    exit()
                case _:
                    print("\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT! ".center(47))
        vender_prod()
        break
    else:
        print(f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT \033[m".center(54)}{"\n"}")
while True:
    menusystem2()
    resp4 = input("").replace(" ", "").lower()
    if resp4 == "1":
        vender_prod()
    elif resp4 == "2":
        fazer_login()
        while True:
            menusystem()
            resp5 = input(f"{" WHAT YOU WANT TO DO? ".center(42)}{"\n"}{"\n"}")
            match resp5:
                case "1":
                    break
                case "2":
                    fazer_login()
                case "3":
                    vendashist()
                case "4":
                    print(f"{"\n"}{"\033[1;32m SEE YOU SOON! \033[m".center(52)}{"\n"}")
                    exit()
                case _:
                    print("\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT! ".center(47))
        vender_prod()
        break
    elif resp4 == "3":
        while True:
            menusystem()
            resp6 = input(f"{" WHAT YOU WANT TO DO? ".center(42)}{"\n"}{"\n"}")
            match resp6:
                case "1":
                    break
                case "2":
                    fazer_login()
                case "3":
                    vendashist()
                case "4":
                    print(f"{"\n"}{"\033[1;32m SEE YOU SOON! \033[m".center(52)}{"\n"}")
                    exit()
                case _:
                    print("\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT! ".center(47))
        vender_prod()
        break
    elif resp4 == "4":
        print(f"{"\n"}{"\033[1;32m SEE YOU SOON! \033[m".center(48)}{"\n"}")
        exit()   
    else:
        print(f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT \033[m".center(54)}{"\n"}")
