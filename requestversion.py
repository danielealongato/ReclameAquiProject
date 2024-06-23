import requests

url = 'https://iosearch.reclameaqui.com.br/raichu-io-site-search-v1/complains/?company=790&status=PENDING&evaluated=bool:false&index=0&offset=10&order=created&orderType=desc&deleted=bool:false&fields=evaluated,title,solved,userName,status,created,id,description'

payload = {}
headers = {
           'Accept-Encoding': 'gzip, deflate, br',
           'User-Agent': 'PostmanRuntime/7.39.0',
           'Accept': '/',
           'Connection': 'keep-alive',
           }

response = requests.request("GET", url, headers=headers, data=payload)

complains = response.json()["data"]
print(complains)

def transform_data():
    informacoes_extraidas = []
        for complain in complains:
            for item in complain:
                info = {
                    "created": complain['created'],
                    "status": complain['status'],
                    "title": complain['title'],
                    "description": complain['description'],
                    "solved": complain['solved'],
                    "id": complain['id']
                }
            informacoes_extraidas.append(info)
    return informacoes_extraidas

