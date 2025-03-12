
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
    print(f"{"\n"}{"\033[1;31m WRONG INFORMATIONS! \033[m".center(55)}")
    print(f"\033[1;31mTHIS ACCOUNT DOESN'T EXIST IN THE SYSTEM".center(52))
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
            print(f"{"\033[1;31mCHOOSE THE OPTION USING THE NUMBERS [1,2]".center(53)}{"\n"}")

#fazer_login()


from datetime import datetime
import openpyxl as op
from copy import copy

tempo = datetime.now().date()
data = tempo.strftime("%d/%m/%Y")

exit = False

def vender_prod():
    print(f"{"\n"}{"\033[1;36m WELCOME TO SALES SYSTEM! ".center(50)}{"\n"}")
    print(f"{"\033[1;36m PUT ALL THE PRODUCTS YOU'VE SOLD ".center(50)}{"\n"}")
    print(f"{"\n"}{"\033[1;34m PRODUCTS OVER R$100.00 HAVE A 10% DISCOUNT! ".center(50)}{"\n"}")
    print(f"{"IF YOU WANT TO RETURN TO MENU, TYPE 'EXIT'".center(44)}{"\n"}")

    arquivo_bancodd = op.load_workbook("main\\banco_de_dados\\banco.xlsx")
    banco = arquivo_bancodd["banco_de_dados"]
    ultima_linha = banco.max_row
    destino = ultima_linha + 1

    total = 0
    totprod = 0
    totdesc = 0
    sacola = []

    while True:
        if exit:
                break
        while True:
            name = input(f"\033[1;36m{"\n"}{"Product's name: "}").lower().strip()
            if name == "":
                print(f"{"\n"}{"\033[1;31m ERROR! ENTER A VALID NAME \033[m".center(51)}{"\n"}")
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
                print(f"{"\n"}{"\033[1;31m ERROR! ENTER A VALID PRICE \033[m".center(52)}{"\n"}")
        if price < 100:
            total += price
            totprod += 1
            sacola.append((name, price))
            banco.append([name,price,data])

            arquivo_bancodd.save("main\\banco_de_dados\\banco.xlsx")
        else:
            price = price - (price * 0.1)
            totdesc += 1
            total += price
            totprod += 1
            sacola.append((name, price))
            banco.append([name,price,data])
            arquivo_bancodd.save("main\\banco_de_dados\\banco.xlsx")
        while True:
            print(f"{"\n"}{"\033[1;36m ADD MORE PRODUCTS? ".center(48)}{"\n"}")
            decide = input(f"{" [1]YES   OR   [2]NO ".center(42)}{"\n"}{"\n"}").strip().lower()
            if decide == "2":
                print(f"{"\n"}{"\033[1;33m SUMMARY OF YOUR SALE ".center(48)}")
                print(
                    f"{"\n"}{"\033[1;33mTotal products: ".ljust(35)}\033[1;32m{totprod:.1f}\033[m")
                print(
                    f"{"\033[1;33mTotal products on sale: ".ljust(35)}\033[1;32m{totdesc:.1f}\033[m")
                print(
                    f"{"\033[1;33mTotal to pay: ".ljust(35)}\033[1;32mR${total:.2f}\033[m")
                print(f"{"\n"}{"\033[1;33m ALL PRODUCTS SOLD ".center(47)}{"\n"}")
                for name, price in sacola:
                    print(f"\033[1;33m{name}{"    -    "}\033[1;32mR${price:.2f}")
                print(f"{"\n"}{"\033[m"}")
                break
            elif decide == "1":
                break
            else:
                print(
                    f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT ".center(50)}")
                print(f"{"\033[1;31mCHOOSE THE OPTION USING THE NUMBERS [1,2]".center(52)}{"\n"}")
        if decide != "1" and "2":
            break



#vender_prod()




def vendashist():
    while True:
        print(f"{"\n"}{"\033[1;34mSALES HISTORY".center(42)}\n")
        print(f"{"DO YOU WANT TO SEARCH BY:  ".center(49)}{"\n"}")
        print("[1] PRODUCT NAME ".center(39))
        print("[2] PRODUCT PRICE ".center(39))
        print("[3] DATE OF SALE ".center(39))
        print("[4] RETURN TO MENU ".center(41))
        resp = input("\n")
        with open("main/banco_de_dados/vendas.txt", "r") as arquivo:
            vendas = arquivo.readlines()
        while True:
            if resp == "1":
                resp2 = input(f"{"\n"}{"\033[1;36mENTER THE PRODUCT NAME: ".center(50)}{"\n"}{"\n"}\033[1;32m").strip().lower()
                if resp2 != "":
                    print(f"{"\n"}{"\033[1;36mPRODUCT HISTORY WITH NAME: ".center(47)}\033[1;32m{resp2}{"\n"}")
                    print(f"{"\n"}{"\033[1;36mNAME , PRICE , DATE\033[m\n\033[1;32m"}")
                    for item in vendas:
                        if resp2 in item.strip().split(","):
                            if resp2 in item.strip().split(","):
                                print(item)
                    break
                else:
                    print(f"{"\n"}{"\033[1;31m ERROR! ENTER A VALID NAME \033[m".center(51)}{"\n"}")

            elif resp == "2":
                resp3 = input(f"{"\n"}{"\033[1;36mENTER THE PRODUCT PRICE: ".center(50)}{"\n"}{"\n"}\033[1;32m").replace(",", ".").strip()
                try:
                    resp3float = float(resp3)
                    resp3str = str(resp3float)
                    print(f"{"\n"}{"\033[1;36mPRODUCT HISTORY WITH PRICE: ".center(47)}\033[1;32m{resp3float}{"\n"}")    
                    print(f"{"\n"}{"\033[1;36mNAME , PRICE , DATE\033[m\n\033[1;32m"}")       
                    for item in vendas:
                        if resp3str in item.strip().split(","):
                            print(item)
                    break
                except ValueError:
                    print(f"{"\n"}{"\033[1;31m ERROR! ENTER A VALID PRICE \033[m".center(52)}{"\n"}")
                

            elif resp == "3":
                print(f"{"\n"}{"\033[1;36mENTER THE PRODUCT DATE: ".center(50)}{"\n"}\033[1;32m")
                resp4 = input("\033[1;36mFOR EXAMPLE: DD/MM/YYYY (DAY/MONTH/YEAR)\n\n".center(53)).replace("-", "/").replace(" ","/").replace(".","/").strip()
                print(f"{"\n"}{"\033[1;36mPRODUCT HISTORY WITH DATE: ".center(47)}\033[1;32m{resp4}{"\n"}")   
                print(f"{"\n"}{"\033[1;36mNAME , PRICE , DATE\033[m\n\033[1;32m"}")  
                for item in vendas:
                    if resp4 in item.strip().split(","):
                        print(item)
                break
            elif resp == "4":
                break
            else:
                print(f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT! ".center(49)}")
                print(f"\033[1;31mCHOOSE THE OPTION USING THE NUMBERS [1,2,3,4]".center(47))


#vendashist()



from funcoes.contas import criar_conta, fazer_login
from funcoes.vender_produto import vender_prod
from funcoes.vendas import vendashist
from funcoes.menu import menusystem, menusystem2


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
                    print(f"\033[1;31mCHOOSE THE OPTION USING THE NUMBERS [1,2,3,4]".center(47))
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
    else:
        print(f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT \033[m".center(56)}")
        print(f"{"\033[1;31mCHOOSE THE OPTION USING THE NUMBERS [1,2]".center(54)}{"\n"}")
while True:
    menusystem2()
    resp4 = input("").strip().lower()
    if resp4 == "1":
        vender_prod()
    elif resp4 == "2":
        fazer_login()
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
                    print(f"\033[1;31mCHOOSE THE OPTION USING THE NUMBERS [1,2,3,4]".center(47))
        vender_prod()
    elif resp4 == "4":
        print(f"{"\n"}{"\033[1;32m SEE YOU SOON! \033[m".center(48)}{"\n"}")
        exit()   
    else:
        print(f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT \033[m".center(54)}{"\n"}")
        print(f"\033[1;31mCHOOSE THE OPTION USING THE NUMBERS [1,2,3,4]".center(47))
