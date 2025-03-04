
def vendashist():
    while True:
        print(f"{"\n"}{"SYSTEM SALES HISTORY"}\n")
        print("DO YOU WANT TO SEARCH BY:  ")
        print("[1] PRODUCT NAME ")
        print("[2] PRODUCT PRICE ")
        print("[3] DATE OF SALE ")
        print("[4] RETURN TO MENU ")
        resp = input("\n")
        with open("main/banco_de_dados/vendas.txt", "r") as arquivo:
            vendas = arquivo.readlines()
        if resp == "1":
            resp2 = input("ENTER THE PRODUCT NAME: ")
            for item in vendas:
                total = item.strip().split(",")
                if resp2 in item:
                    print(item)

        elif resp == "2":
            resp3 = input(f"{"ENTER THE PRODUCT PRICE: "}").replace(",",".")
            resp3float = float(resp3)
            resp3str = str(resp3float)
            for item in vendas:
                total = item.strip().split(",")
                if resp3str in item:
                    print(item)
     
        elif resp == "3":
            resp4 = input(f"{"ENTER THE PRODUCT'S DATE OF SALE : "}").replace("-","/")
            print(resp4)
            for item in vendas:
                total = item.strip().split(",")
                if resp4 in item:
                    print(item)
            else:
                print("data nao encontrada")     
        elif resp == "4":
            break      

            
            
            
                     
            

#vendashist()