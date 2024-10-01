import requests

try:
    cep = input('Informe o CEP: ')
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    if response.status_code == 200:
        dados = response.json()
        if 'erro' in dados:
            print('ERRO. Cep Inexistente')
        else:
            print(f'Rua: {dados["logradouro"]}\n'
                  f'UF: {dados["uf"]}\n'
                  f'Estado: {dados["estado"]}')
    else:
        print('ERRO de requisição')
except requests.exceptions.ConnectionError:
    print('ERRO de requisição')