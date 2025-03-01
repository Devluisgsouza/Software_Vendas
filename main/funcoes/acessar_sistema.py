from funcoes.vender_produto import vender_produto
def acessar_sistema():
    while True:
        print("\nWOULD YOU LIKE TO ACCESS THE SALES SYSTEM?")
        resp = input("[1] YES   OR   [2] CLOSE SYSTEM: \n").replace(" ","").lower()
        if resp == "1":
            vender_produto()
            break
        elif resp == "2":
            print("\nSEE YOU SOON!")
            break
        else:
            print("I CAN'T UNDERSTAND WHAT YOU WANT")