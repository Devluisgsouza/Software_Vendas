import openpyxl as op

def exlcuir_venda():
    exit = False
    while True:
        if exit:
            break
        arquivo_bancodd = op.load_workbook("main\\banco_de_dados\\banco.xlsx")
        banco_vendas = arquivo_bancodd["banco_de_vendas"]
        ultima_linha = banco_vendas.max_row
        idstr = input(f"\033[1;36m{"\n"}{"ENTER THE “ID” OF THE SALE YOU WANT TO DELETE: ".center(48)}").lower().strip()
        id = int(idstr)
        for linha in range(2,ultima_linha + 1):
            id_venda = banco_vendas.cell(row=linha, column=1).value
            if id == id_venda:
                banco_vendas.delete_rows(linha,1)
                print("Venda excluida com sucesso")
                arquivo_bancodd.save("main\\banco_de_dados\\banco.xlsx")
                return exit
                
        
        

def alterar_venda():
    pass

exlcuir_venda()