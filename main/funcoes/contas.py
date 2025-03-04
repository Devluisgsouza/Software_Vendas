

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