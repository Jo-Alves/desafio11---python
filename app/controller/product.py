from time import sleep
from utils.utils import clear
import models.crud_json as crud_json
from os.path import abspath
path = abspath(r"./db/products.json")

def save_product():
   try:
        clear()
        products = []
        product = {}
        
        file_exist = crud_json.file_exist(path)["exist_file"]
        while True:     
            if file_exist:
                if crud_json.findAll(path)["error"] == False:
                    products = crud_json.findAll(path)["data"] if crud_json.findAll(path)["error"] == False else []
                
    
            index = len(products) - 1
            product["id"] = 1 if len(products) == 0 else products[index]["id"] + 1
            product["name"] = input("Digite o nome do produto:\n")
            product["description"] = input("Digite a descrição do produto:\n")
            product["price"] = float(input("Digite a preço do produto:\n"))
            
            products.append(product)
            if not crud_json.save(path, products)["error"]:
                print("=============================")
                print("Produto cadastrado com sucesso")
                print("=============================")
                sleep(2)
                
            clear()
            opcao = input("Deseja cadastrar un novo produto? [S/N]\n")
            if(opcao.lower() != "s"):
                break
            else:
                clear()
   except Exception as ex:
       print(f"error: {ex}")
    