def criar_conta():
    print("--- CREAT YOUR ACCOUNT: ---\n")
    login = input("Login: ")
    password = input("Password: ")
    with open("main/banco_de_dados/logins.txt","r") as arquivo:
        log = arquivo.read() 
    if login in log:
        print("\n--- THIS ACCOUNT ALREADY EXISTS IN THE SYSTEM ---\n")
        criar_conta()
    else:
        with open("main/banco_de_dados/logins.txt","a") as arquivo:
            arquivo.write(f"{login}\n")
        with open("main/banco_de_dados/passwords.txt","a") as arquivo:
            arquivo.write(f"{password}\n")
        print("\n--- ACCOUNT CREATED SUCCESSFULY! ---")
        with open("main/banco_de_dados/accounts.txt", "a") as arquivo:
            arquivo.write(f"{login},{password}\n")
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

def acessar_sistema():
    while True:
        print("\nWOULD YOU LIKE TO ACCESS THE SALES SYSTEM?")
        resp = input("[1] YES   OR   [2] CLOSE SYSTEM: \n").replace(" ","").lower()
        if resp == "1":
            vender_produto()
            break
        elif resp == "2":
            print("\n--- SEE YOU SOON! ---\n")
            break
        else:
            print("I CAN'T UNDERSTAND WHAT YOU WANT")

def vender_produto():
    print("--- WELCOME TO SALES SYSTEM! ---")
    print("\nPRODUCTS OVER R$100.00 HAVE A 10% DISCOUNT!\n")
    total = 0
    totprod = 0
    totdesc = 0
    sacola = []
    while True:
        name = input("Product's name: ")
        price = float(input("Product's price: ").replace(",", "."))
        with open("main/banco_de_dados/price.txt", "a") as arquivo:
            arquivo.write(f"{price}\n")
        with open("main/banco_de_dados/name.txt", "a") as arquivo:
            arquivo.write(f"{name}\n")
        if price < 100:
            total += price
            totprod += 1
            sacola.append((name, price))
        else:
            price = price - (price * 0.1)
            totdesc += 1
            total += price
            totprod += 1
            sacola.append((name, price))
        while True:
            decide = input("Add more products? [1] Yes [2] No: ").replace(",", ".").lower()
            if decide == "2":
                print(f"\nTotal products: {totprod}")
                print(f"Total products on sale: {totdesc}")
                print(f"Total to pay: {total}")
                print("\nYOUR BAG: ")
                for name, price in sacola:
                    print(f"{name}  -  R${price}")
                break
            elif decide == "1":
                break
            else:
                print("\n--- I CAN'T UNDERSTAND WHAT YOU WANT ---\n")
        if decide != "1" and "2":
            break

print("--- WELCOME TO THE SALE SYSTEM --- \n")
while True:
    print("--- DO YOU HAVE AN ACCOUNT? ---")
    resp = str(input("[1] YES   or   [2] NO\n").replace(" ","").lower())
    if resp == "1":
        fazer_login()
        acessar_sistema()
        break
    elif resp == "2":
        criar_conta()
        acessar_sistema()
        break
    else:
        print("--- I CAN'T UNDERSTAND WHAT YOU WANT ---")
        