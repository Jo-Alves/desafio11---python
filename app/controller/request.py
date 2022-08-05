from __future__ import barry_as_FLUFL
from urllib import request
import models.crud_json as crud_json
from os.path import abspath
from utils.utils import clear
from time import sleep, time

paths = [abspath(r"./db/requests.json"),
         abspath(r"./db/clients.json"), abspath(r"./db/products.json")]


def save_requests():
    clear()
    try:
        if not crud_json.file_exist(paths[1])["exist_file"] or crud_json.findAll(paths[1])['error'] or len(crud_json.findAll(paths[1])["data"]) == 0:
            print("cliente não existe")
            return

        if not crud_json.file_exist(paths[2])["exist_file"] or crud_json.findAll(paths[2])['error'] or len(crud_json.findAll(paths[2])["data"]) == 0:
            print("Produto não existe")
            return

        while True:
            clients = crud_json.findAll(paths[1])["data"]
            client = {}
            while True:
                have_client = False
                id_client = int(
                    input("Digite o id do cliente para realizar o pedido\n"))
                for data_client in clients:
                    if(data_client["id"]) == id_client:
                        client = data_client
                        have_client = True
                        break
                
                clear()
                if have_client:
                    print("=======[Informação do cliente]=======")
                    print(f"id: {client['id']}")
                    print(f"Cliente: {client['name']}")
                    print(f"Email: {client['email']}")
                    print("===============================")
                    opcao = input(
                        "Você confirma que os dados acima está correta? [S/N]\n")
                    if opcao.lower() == "s":
                        break
                    
                    clear()
                else:
                    print(f"O cliente com o id: {id_client} não existe.\n")
                    have_client = False

            clear()
            products = crud_json.findAll(paths[2])["data"]
            items_request = []
            product = {}
            valor_total = 0
            have_product = False
            
            while True:
                confirm_information_product = False
                id_product = int(input("Digite o id do produto:\n"))
                for data_product in products:
                    if data_product['id'] == id_product:
                        product = data_product
                        have_product = True
                                              
                if not have_product:
                    print(f"O produto com o id: {id_product} não existe.\n")                    

                if have_product == True:
                    while confirm_information_product == False:
                        clear()
                        print("=======[Informação do produto]=======")
                        print(f"id: {product['id']}")
                        print(f"Nome: {product['name']}")
                        print(f"Descrição: {product['description']}")
                        print(f"Preco: {product['price']}")
                        print("===============================")
                        opcao = input("Você confirma que os dados acima está correta? [S/N]\n")
                        if opcao.lower() == "s":                            
                            clear()
                            confirm_information_product = True
                        else:
                           clear()
                           confirm_information_product = False
                           break
                        
                    if confirm_information_product:
                        valor_total += product["price"]
                        items_request.append(product)
                        # clear()
                        confirm_information_product = False
                        option = input("Deseja inserir mais um item ao pedido? [S/N]\n")
                        if option.lower() != "s":
                            clear()
                            break  
                        else:
                            clear()                     

            requests = []
            request = {}
            file_exist = crud_json.file_exist(paths[0])["exist_file"]
            if file_exist:
                if crud_json.findAll(paths[0])["error"] == False:
                    requests = crud_json.findAll(paths[0])["data"] if crud_json.findAll(paths[0])[
                        "error"] == False else []

            index = len(requests) - 1
            request["id"] = 1 if len(requests) == 0 else requests[index]["id"] + 1
            request["client"] = client
            request["items"] = items_request
            request["value_total"] = valor_total

            requests.append(request)
            if not crud_json.save(paths[0], requests)["error"]:
                print("=============================")
                print("Pedido cadastrado com sucesso")
                print("=============================")
                sleep(2)

            clear()
            opcao = input("Deseja cadastrar un novo pedido? [S/N]\n")
            if(opcao.lower() != "s"):
                break
            else:
                clear()
    except Exception as ex:
        print(f"error: {ex}")
