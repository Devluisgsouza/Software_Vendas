from funcoes.contas import criar_conta, fazer_login
from funcoes.vender_produto import vender_prod
from funcoes.vendas import vendashist


print(f"{"\n"}{"\033[1;32m WELCOME TO THE SALES SYSTEM \033[m".center(54)}{"\n"}")
while True:
    print(f"{"\n"}{"\033[1;36m DO YOU HAVE AN ACCOUNT? ".center(52)}\n")
    resp = str(input(f"{" [1]YES   or   [2]NO ".center(45)}{"\n"}{"\n"}").replace(" ", "").lower())
    if resp == "1":
        fazer_login()
        while True:
            print(f"{"\n"}{"\033[1;36m SYSTEM MENU" .center(50)}{"\n"}")
            print(" [1] ACCESS THE SYSTEM ".center(41))
            print(" [2] CHANGE ACCOUNT ".center(38))
            print(" [3] SALES HISTORY ".center(38))
            print(f"{" [4] CLOSE SYSTEM ".center(36)}{"\n"}")
            resp = input(f"{" WHAT YOU WANT TO DO? ".center(42)}{"\n"}{"\n"}")
            match resp:
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
    elif resp == "2":
        criar_conta()
        while True:
            print(f"{"\n"}{"\033[1;36m SYSTEM MENU" .center(50)}{"\n"}")
            print(" [1] ACCESS THE SYSTEM ".center(41))
            print(" [2] CHANGE ACCOUNT ".center(38))
            print(" [3] SALES HISTORY ".center(38))
            print(f"{" [4] CLOSE SYSTEM ".center(36)}{"\n"}")
            resp = input(f"{" WHAT YOU WANT TO DO? ".center(42)}{"\n"}{"\n"}")
            match resp:
                case "1":
                    break
                case "2":
                    fazer_login()
                case "3":
                    break
                case "4":
                    print(f"{"\n"}{"\033[1;32m SEE YOU SOON! \033[m".center(52)}{"\n"}")
                    exit()
                case _:
                    print("\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT! ".center(47))
        vender_prod()
        break
    else:
        print(f"{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT \033[m".center(54)}{"\n"}")
while True:
    print("\033[1;36m WOULD YOU LIKE TO MAKE A NEW SALE OR CHANGE ACCOUNT? ".center(49))
    resp = str(input(f"{"\n"}{" [1]NEW SALE     [2]CHANGE ACCOUNT     [3]LOGOUT ".center(49)}{"\n"}{"\n"}").replace(" ", "").lower())
    if resp == "1":
        vender_prod()
    elif resp == "2":
        fazer_login()
        vender_prod()
    elif resp == "3":
        print(f"{"\n"}{"\033[1;32m SEE YOU SOON! \033[m".center(48)}{"\n"}")
        break
    else:
        print(f"{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT \033[m".center(54)}{"\n"}")