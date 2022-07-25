import json

def tranformDict(someJson):
    try:
        #transforma json em dicionario
        someDict = json.loads(someJson)
    except Exception as err:
        return("Erro ao converter json em dicionario",err)
    return someDict

def tranformJson(someDict):
    try:
        #transforma dicionario em json
        someJson = json.dumps(someDict)
    except Exception as err:
        return("Erro ao converter dicionario em json",err)
    return someJson