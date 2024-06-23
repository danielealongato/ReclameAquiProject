import requests

url = 'https://iosearch.reclameaqui.com.br/raichu-io-site-search-v1/complains/?company=790&status=PENDING&evaluated=bool:false&index=1&offset=10&order=created&orderType=desc&deleted=bool:false'
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}

try:
    response = requests.get(url, proxies=proxies, timeout=30)  # Aumentar o timeout para 30 segundos
    response.raise_for_status()  # Verifica se houve erro na requisição
    data = response.json()
    print(data)
except requests.exceptions.Timeout:
    print("A requisição expirou")
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
