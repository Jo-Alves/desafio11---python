from time import time
from utils.utils import clear
import models.crud_json as crud_json
from os.path import abspath
from time import sleep

path = abspath(r"./db/clients.json")

def save_client():
    clear()
    clients = []
    client = {}
    
    while True: 
        file_exist = crud_json.file_exist(path)["exist_file"]
        if file_exist:
            if crud_json.findAll(path)["error"] == False:
                clients = crud_json.findAll(path)["data"] if crud_json.findAll(path)["error"] == False else []
                
        index = len(clients) - 1
        client["id"] = 1 if len(clients) == 0 else clients[index]["id"] + 1
        client["name"] = input("Digite o nome do cliente:\n")
        client["email"] = input("Digite o email do cliente:\n")
        
        clients.append(client)
        if not crud_json.save(path, clients)["error"]:
            print("===============================")
            print("Cliente cadastrado com sucesso.")
            print("===============================")
            sleep(2)
        
        clear()    
        opcao = input("Deseja cadastrar un novo cliente? [S/N]\n")
        if(opcao.lower() != "s"):
            break
        else:
            clear()