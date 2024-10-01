import requests

lista = []
ingrediente = input("Digite o ingrediente que deseja procurar: ")

try:
    response = requests.get(f'https://dummyjson.com/recipes?limit=50')

    if response.status_code == 200:
        dados = response.json()
        for receita in dados['recipes']:
            for ing in receita['ingredients']:
                if ingrediente.lower() == ing.lower():
                    lista.append(receita)
                    break  

        if lista:
            print(f"Receitas encontradas com {ingrediente}:")
            for receita in lista:
                print(f"Nome: {receita['name']}")
                print("Ingredientes:")
                for ing in receita['ingredients']:
                    print(ing)
                print("Instruções:")
                for instrucao in receita['instructions']:
                    print(instrucao)
                print('-' * 200)
        else:
            print(f'Nenhuma receita encontrada com o ingrediente {ingrediente}.')
    else:
        print('ERRO de requisição.')
except requests.exceptions.ConnectionError:
    print('ERRO de conexão.')
except Exception as e:
    print(f'ERRO: {e}')
