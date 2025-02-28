def criar_conta():
    login = input("Login: ")
    password = input("Password: ")
    with open("main/banco_de_dados/accounts.txt", "a") as arquivo:
        arquivo.write(f"{login},{password}\n")
    print("account created successfully")   



def fazer_login():
    login = input("Login: ")
    password = input("Password: ")
    with open("main/banco_de_dados/accounts.txt", "r") as arquivo:
        contas = arquivo.readlines()
    
    for conta in contas:
        login_salvo, senha_salva = conta.strip().split(",")
        if login == login_salvo and password == senha_salva:
            print("Successfully login")
            return
    print("Wrong infomations!")
    