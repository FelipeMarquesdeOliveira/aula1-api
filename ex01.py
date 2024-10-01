import requests

try:
    uf = input('Digite sua UF(SIGLA): ')
    response = requests.get(f'http://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios')

    if response.status_code == 200:
        dados = response.json()
        for item in dados:
            print(item['nome'])
        print(f'Totalizando: {len(dados)} Municipios')
    else:
        print('ERRO de requisição.')
except requests.exceptions.ConnectionError:
    print('ERRO de requisição.')
except Exception:
    print('ERRO.')