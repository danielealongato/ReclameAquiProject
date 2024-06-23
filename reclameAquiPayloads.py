import json
import pandas as pd
import csv
import requests
import time


def colect_complains():
    informacoes_extraidas = []

    page = 10
    while True:

        url = f'https://iosearch.reclameaqui.com.br/raichu-io-site-search-v1/query/companyComplains/10/{page}?company=790'

        payload = {}
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'User-Agent': 'PostmanRuntime/7.39.0',
            'Accept': '/',
            'Connection': 'keep-alive',
        }
        time.sleep(2)
        response = requests.request("GET", url, headers=headers, data=payload)
        print(page)
        if response.status_code != 200 or page>200:
            break

        complains = response.json()["complainResult"]["complains"]["data"]
        #print(complains)
        for complain in complains:
            info = {
                "created": complain['created'],
                "status": complain['status'],
                "title": complain['title'],
                "description": complain['description'],
                "solved": complain['solved'],
                "id": complain['id']
            }
            informacoes_extraidas.append(info)
            print(complain)

        page = page+10
    return informacoes_extraidas


# Função para extrair informações
def extrair_informacoes_by_csv(payload):
    informacoes_extraidas = []
    for reclamacoes in payload:
        for item in reclamacoes:
            reclamacao = json.loads(item).get("data")
            for complain in reclamacao:
                info = {
                    "created": complain.get("created"),
                    "status": complain.get("status"),
                    "title": complain.get("title"),
                    "description": complain.get("description"),
                    "solved": complain.get("solved"),
                    "id": complain.get("id")
                }
                informacoes_extraidas.append(info)
    return informacoes_extraidas


# Função para extrair informações
def extrair_informacoes_by_postman(payload):
    informacoes_extraidas = []
    for reclamacoes in payload:
        info = {
                "created": reclamacoes["created"],
                "status": reclamacoes["status"],
                "title": reclamacoes["title"],
                "description": reclamacoes["description"],
                "solved": reclamacoes["solved"],
                "id": reclamacoes["id"]
        }
        informacoes_extraidas.append(info)
    return informacoes_extraidas

def extrair_informacoes_by_csv(payload):
    informacoes_extraidas = []
    for reclamacoes in payload:
        for item in reclamacoes:
            reclamacao = json.loads(item).get("data")
            for complain in reclamacao:
                info = {
                    "created": complain.get("created"),
                    "status": complain.get("status"),
                    "title": complain.get("title"),
                    "description": complain.get("description"),
                    "solved": complain.get("solved"),
                    "id": complain.get("id")
                }
                informacoes_extraidas.append(info)
    return informacoes_extraidas

def write_file(informacoes):
    fields_names = ['id', 'title', 'status', 'description', 'created', 'solved']
    with open('Reclamacoes01.csv', 'w', newline="", encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields_names)
        writer.writeheader()
        writer.writerows(informacoes)

    # Exibindo as informações extraídas
    for info in informacoes:
        print(json.dumps(info, indent=4, ensure_ascii=False))

def read_file():
    payload=[]
    with open('reclamacoes_list - Sheet1.csv', 'r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for line in leitor_csv:
            print(line)
            payload.append(line)

    return payload

if __name__ == '__main__':
    payload = colect_complains()
    #payload = read_file()
    #informacoes = extrair_informacoes_by_postman(payload)
    write_file(informacoes=payload)