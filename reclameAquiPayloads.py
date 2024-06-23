import json
import pandas as pd
import csv
import requests


def colect_complains():
    url = 'https://iosearch.reclameaqui.com.br/raichu-io-site-search-v1/complains/?company=790&status=PENDING&evaluated=bool:false&index=20&offset=10&order=created&orderType=desc&deleted=bool:false&fields=evaluated,title,solved,userName,status,created,id,description'

    payload = {}
    headers = {
               'Accept-Encoding': 'gzip, deflate, br',
               'User-Agent': 'PostmanRuntime/7.39.0',
               'Accept': '/',
               'Connection': 'keep-alive',
               }

    response = requests.request("GET", url, headers=headers, data=payload)

    complains = response.json()["data"]
    return complains

# Função para extrair informações
def extrair_informacoes(payload):
    informacoes_extraidas = []
    for reclamacoes in payload:
        reclamacao = dict(reclamacoes).get('data')
        for item in reclamacao:
            info = {
                "created": item.get("created"),
                "status": item.get("status"),
                "title": item.get("title"),
                "description": item.get("description"),
                "solved": item.get("solved"),
                "id": item.get("id")
            }
            informacoes_extraidas.append(info)
    return informacoes_extraidas


def write_file(informacoes):
    fields_names = ['id', 'title', 'status', 'description', 'created', 'solved']
    with open('ReclamacoesNew.csv', 'a', newline="", encoding='utf-8') as csvfile:
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
            payload.append(json.dumps(line, indent=4))

    return payload

if __name__ == '__main__':
#    payload = colect_complains()

    informacoes = extrair_informacoes(payload)
    write_file(informacoes=informacoes)