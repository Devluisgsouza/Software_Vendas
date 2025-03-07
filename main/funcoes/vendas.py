
def vendashist():
    while True:
        print(f"{"\n"}{"\033[1;34mSALES HISTORY SYSTEM".center(49)}\n")
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
            for item in vendas:
                print(f"{"\n"}{"\033[1;36mNAME , PRICE , DATE\033[m\n\033[1;32m"}")
                if resp2 in item.strip().split(","):
                    print(item[0])
        elif resp == "2":
            resp3 = input(f"{"\n"}{"\033[1;36mENTER THE PRODUCT PRICE: ".center(50)}{"\n"}{"\n"}\033[1;32m").replace(",", ".").strip()
            resp3float = float(resp3)
            resp3str = str(resp3float)
            print(f"{"\n"}{"\033[1;36mPRODUCT HISTORY WITH PRICE: ".center(47)}\033[1;32m{resp3float}{"\n"}")           
            for item in vendas:
                if resp3str in item.strip().split(","):
                    print(f"{"\n"}{"\033[1;36mNAME , PRICE , DATE\033[m\n\033[1;32m"}")
                    print(item)
        elif resp == "3":
            resp4 = input(f"{"\n"}{"\033[1;36mENTER THE PRODUCT DATE: ".center(50)}{"\n"}{"\n"}\033[1;32m").replace("-", "/").strip()
            print(f"{"\n"}{"\033[1;36mPRODUCT HISTORY WITH DATE: ".center(47)}\033[1;32m{resp4}{"\n"}")     
            for item in vendas:
                if resp4 in item.strip().split(","):
                    print(f"{"\n"}{"\033[1;36mNAME , PRICE , DATE\033[m\n\033[1;32m"}")
                    print(item)
        elif resp == "4":
            break
        else:
            print(
                f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT! ".center(49)}")


#vendashist()
