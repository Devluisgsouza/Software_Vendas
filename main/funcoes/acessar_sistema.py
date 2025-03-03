from funcoes.vender_produto import vender_produto
def acessar_sistema():
    while True:
        print(f"{"\n"}{"\033[1;36m WOULD YOU LIKE TO ACCESS THE SALES SYSTEM? ".center(50)}{"\n"}")
        resp = input(f"{" [1]YES   OR   [2]NO ".center(42)}{"\n"}{"\n"}").replace(" ","").lower()
        if resp == "1":
            vender_produto()
            break
        elif resp == "2":
            print(f"{"\n"}{" SEE YOU SOON! ".center(40)}{"\n"}\033[m")
            break
        else:
            print("\033[1;31mI CAN'T UNDERSTAND WHAT YOU WANT\033[m".center(50))