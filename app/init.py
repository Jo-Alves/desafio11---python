from __future__ import barry_as_FLUFL
from controller.client import  save_client
from controller.product import  save_product
from controller.request import  save_requests
from controller.report import generate_report
from utils.utils import clear

def show_menu():    
    menu = ["Cadastro de cliente", "Cadastro de Produto", "Cadastro de pedidos"]
    print("=================== [Menu] ===========================")
    print("============ Escolha uma dessas opções ============")
    print("============ Cadastrar cliente. Digite '1' ============")
    print("============ Cadastrar produto. Digite '2' ============")
    print("============ Cadastrar pedido. Digite '3' ============")
    print("============ Gerar Relatório. Digite '4' ============")
    print('============ Aperte "0" para sair ============')
    while True: 
        opcao = input()
        if(opcao == "0"):
            break
        elif(opcao == "1"):
            save_client()
            break
        elif(opcao == "2"):
            save_product()
            break
        elif(opcao == "3"):
            save_requests()
            break
        elif(opcao == "4"):
            generate_report()
            break  
       

show_menu()