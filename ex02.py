import requests

n = 5  
nomes = []

try:
    response = requests.get(f'http://randomuser.me/api/?results={n}')

    if response.status_code == 200:
        dados = response.json()
        for item in dados['results']:
            nomes.append(item['name']['first'])
    else: 
        print('ERRO de requisição')
except requests.exceptions.ConnectionError:
    print('ERRO de requisição')
except Exception:
    print('ERRO.')

nomes.sort()
print(nomes)
