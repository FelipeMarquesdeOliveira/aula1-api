import requests

valor = []

try:
    response = requests.get('http://dummyjson.com/products?limit=100')

    if response.status_code == 200:
        dados = response.json()
        for item in dados['products']:
            preco = item['price']
            desconto = item['discountPercentage'] / 100 * preco
            valorDesconto = round(preco - desconto, 2)  
            valor.append(valorDesconto)
    else:
        print('ERRO de requisição.')
except requests.exceptions.ConnectionError:
    print('ERRO de conexão.')
except Exception as e:
    print(f'ERRO: {e}')


total = sum(valor)
print(f'Soma total com desconto: {total:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
