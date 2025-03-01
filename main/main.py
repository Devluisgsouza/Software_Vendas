from funcoes.contas import criar_conta, fazer_login
from funcoes.vender_produto import vender_produto


print("WELCOME TO THE SALE SYSTEM\n")
print("DO YOU HAVE AN ACCOUNT?")
resp = str(input("[1] YES   or   [2] NO\n"))
if resp == "1":
    fazer_login()
else:
    criar_conta()
print("\nWOULD YOU LIKE TO ACCESS THE SALES SYSTEM?")
resp = int(input("[1] YES   OR   [2] CLOSE SYSTEM: \n"))
if resp == 1:
    vender_produto()
