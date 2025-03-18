import openpyxl as op

def exlcuir_venda():
    exit = False
    while True:
        if exit:
            break
        arquivo_bancodd = op.load_workbook("main\\banco_de_dados\\banco.xlsx")
        banco_vendas = arquivo_bancodd["banco_de_vendas"]
        ultima_linha = banco_vendas.max_row
        idstr = input(f"\033[1;36m{"\n"}{"ENTER THE “ID” OF THE SALE YOU WANT TO DELETE ".center(48)}{"\n"}{"\n"}").lower().strip()
        id = int(idstr)
        for linha in range(2,ultima_linha + 1):
            id_venda = banco_vendas.cell(row=linha, column=1).value
            if id == id_venda:
                banco_vendas.delete_rows(linha,1)
                print("Venda excluida com sucesso")
                arquivo_bancodd.save("main\\banco_de_dados\\banco.xlsx")
                break
        while True:
            print(f"{"\n"}{"\033[1;36mWOULD YOU LIKE TO DELETE MORE SALES?".center(53)}")
            resp = input(f"{'[1]YES   OR   [2]NO'.center(45)}{"\n"}").strip()
            if resp == "1":
                break
            elif resp == "2":
                return exit
            else:
                print(f"{"\n"}{"\033[1;31m I CAN'T UNDERSTAND WHAT YOU WANT \033[m".center(56)}")
                print(f"{"\033[1;31mCHOOSE THE OPTION USING THE NUMBERS [1,2]".center(54)}{"\n"}")

                
        
        

def alterar_venda():
    arquivo_bancodd = op.load_workbook("main\\banco_de_dados\\banco.xlsx")
    banco_vendas = arquivo_bancodd["banco_de_vendas"]
    ultima_linha = banco_vendas.max_row
    
    exit = False

    while True:
        if exit:
            break
        idstr = input(f"\033[1;36m{"\n"}{"ENTER THE “ID” OF THE SALE YOU WANT TO CHANGE ".center(48)}{"\n"}{"\n"}").lower().strip()
        id = int(idstr)
        for linha in range(2,ultima_linha + 1):
            id_venda = banco_vendas.cell(row=linha, column=1).value
            if id == id_venda:
                print(f"{"DO YOU WANT TO CHANGE:  ".center(49)}{"\n"}")
                print("[1] PRODUCT NAME ".center(39))
                print("[2] PRODUCT PRICE ".center(39))
                print("[3] DATE OF SALE ".center(39))
                print("[4] RETURN TO MENU ".center(41))
                resp = input("\n").strip()
                match resp:
                    case "1":
                            for linha in range(2,ultima_linha + 1):
                                nome = input(f"{"ENTER WITH THE NEW NAME: "}")
                                nome_venda = banco_vendas.cell(row=linha, column=2).value
                                
                                arquivo_bancodd.save("main\\banco_de_dados\\banco.xlsx")
                    case "1":
                        preço = input(f"{"ENTER WITH THE NEW PRICE: "}")
                        preço_venda = preço
                        arquivo_bancodd.save("main\\banco_de_dados\\banco.xlsx")
                    case "3":
                        data = input(f"{"ENTER WITH THE NEW DATE: "}")
                        data_venda = data
                        arquivo_bancodd.save("main\\banco_de_dados\\banco.xlsx")
                    case "4":
                        return exit
                
















alterar_venda()
# exlcuir_venda()