def criar_conta():
    login = input("Login: ")
    password = input("Password: ")
    with open("main/banco_de_dados/accounts.txt", "a") as arquivo:
        arquivo.write(f"{login},{password}\n")
    print("\naccount created successfully")
    return



def fazer_login():
    print("Enter with your account: \n")
    login = input("Login: ")
    password = input("Password: ")
    with open("main/banco_de_dados/accounts.txt", "r") as arquivo:
        contas = arquivo.readlines()
    for conta in contas:
        login_salvo, senha_salva = conta.strip().split(",")
        if login == login_salvo and password == senha_salva:
            print("\nSuccessfully login")
            return
    while True:
        print("\nWRONG INFORMATIONS!")
        print("\nWOULD YOU LIKE TO CREATE A NEW ACCOUNT? \n")
        resp = int(input("[1] YES   OR   [2] NO\n"))
        if resp == 1:
            criar_conta()
            return
        else:
            fazer_login()
            return
        