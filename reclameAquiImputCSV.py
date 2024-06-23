import csv
import json


def read_file():
    payload = []
    with open('reclamacoes_list_oficial - Sheet1.csv', 'r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for line in leitor_csv:
            print(line)
            payload.append(line)

    return payload


# Função para extrair informações do csv
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
    # Nome do arquivo CSV
    nome_arquivo = 'registros.csv'
    # Extraindo os nomes dos campos (cabeçalhos) do primeiro registro
    campos = informacoes[0].keys()

    # Abrindo o arquivo CSV para escrita
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)

        # Escrevendo os cabeçalhos
        escritor_csv.writeheader()

        # Escrevendo os registros
        escritor_csv.writerows(informacoes)


if __name__ == '__main__':
    payload = read_file()
    informacoes = extrair_informacoes_by_csv(payload)
    write_file(informacoes=informacoes)
