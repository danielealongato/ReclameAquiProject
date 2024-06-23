import requests

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
print(complains)

informacoes_extraidas = []
for complain in complains:
    for item in complain:
        info = {
            "created": item.get("created"),
            "status": item.get("status"),
            "title": item.get("title"),
            "description": item.get("description"),
            "solved": item.get("solved"),
            "id": item.get("id")
        }
        informacoes_extraidas.append(info)

