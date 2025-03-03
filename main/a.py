
print("--- CREAT YOUR ACCOUNT: ---\n")
login = input("Login: ")
with open("main/banco_de_dados/logins.txt","r") as arquivo:
    log2 = arquivo.read()
print(log2)

