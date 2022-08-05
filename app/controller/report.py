from utils.utils import clear
from os.path import abspath
from models.crud_json import file_exist
from models.crud_json import findAll
path = abspath(r"./db/requests.json")
from time import sleep
def generate_report():
    clear()
    if not file_exist(path)["exist_file"]:
        print("==========================")        
        print("Não há pedidos no momento.")        
        print("==========================")        
        return
    
    requests = findAll(path)
    if requests["error"]:
        print(requests["error"])
        return
    print("======================== [Relatório de pedidos] ============================")
    for request in requests["data"]:
        print(f"Pedido nº: {request['id']}")
        print(f"Cliente: {request['client']['name']}")
        print("Valor total: {:.2f}".format(request['value_total']))
        print("================================================")
        sleep(0.8)