import contas
import vender_produto


def menu():
    while True:
        print("SYSTEM MENU")
        print("[1] ACCESS THE SYSTEM")
        print("[2] CHANGE ACCOUNT")
        print("[3] SALES HISTORY")
        print("[4] CLOSE SYSTEM")
        resp = input("WHAT YOU WANT TO DO?")
        match resp:
            case "1":
                vender_produto.vender_produto()
                break
            case "2":
                contas.fazer_login()
                break
            case "3":
                break
            case "4":
                break
            case _:
                print("I CAN'T UNDERSTAND WHAT YOU WANT!")

menu()