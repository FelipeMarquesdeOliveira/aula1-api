
import requests

try:
    response = requests.get('http://servicodados.ibge.gov.br/api/v3/noticias/?qtd=10')

    if response.status_code == 200:
        dados = response.json()
        for item in dados['items']:
            print(f"Titulo: {item['titulo']}")
            print(f"Resumo: {item['introducao']}")
            print('-'* 40)
    else:
        print('Erro de requisição')
except requests.exceptions.ConnectionError:
    print('Erro de Requisição')
except Exception:
    print('Erro.')