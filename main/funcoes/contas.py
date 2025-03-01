def criar_conta():
    print("--- CREAT YOUR ACCOUNT: ---\n")
    login = input("Login: ")
    password = input("Password: ")
    with open("main/banco_de_dados/accounts.txt", "a") as arquivo:
        arquivo.write(f"{login},{password}\n")
    print("\n--- ACCOUNT CREATED SUCCESSFULY! ---")
    return


def fazer_login():
    print("--- ENTER WITH YOUR ACCOUNT: ---\n")
    login = input("Login: ")
    password = input("Password: ")
    with open("main/banco_de_dados/accounts.txt", "r") as arquivo:
        contas = arquivo.readlines()
    for conta in contas:
        login_salvo, senha_salva = conta.strip().split(",")
        if login == login_salvo and password == senha_salva:
            print("\n--- SUCCESSFULLY LOGIN ---")
            return
    while True:
        print("\n--- WRONG INFORMATIONS! ---")
        print("\n--- WOULD YOU LIKE TO CREATE A NEW ACCOUNT? ---\n")
        resp = int(input("[1] YES   OR   [2] NO\n"))
        if resp == 1:
            criar_conta()
            return
        else:
            fazer_login()
            return
