from funcoes.transforma import transfstr
from funcoes.contas import criar_conta, fazer_login
from funcoes.vender_produto import vendaer_produto

# Criação das variáveis


print("WELCOME TO THE SALE SYSTEM\n")
print("DO YOU HAVE AN ACCOUNT?")
resp = str(input("[1] YES   or   [2] NO\n"))
if resp == "1":
    fazer_login()
else:
    criar_conta()

vendaer_produto()
