import json
from os.path import exists

def file_exist(path):
    return {"exist_file": exists(path)}
        
            
def save(path, data):
    f = open(path, "w")
    try:
        file_json = json.dumps(data, indent=2, separators=(",",": "))
        f.write(file_json)
        return {"msg": "DB criado com sucesso","error": False}
    except Exception as e:
        return {"msg": e, "error": True }
    finally:
        f.close()
            
def findAll(path):
    f = open(path, "r")
    try:
        file = f.read()
        file = json.loads(file)        
        return {"error": False, "data": file}
    except Exception as e:
        return {"error": True}
    finally:
        f.close()

