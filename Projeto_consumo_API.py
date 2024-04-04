import requests
import random

while True:   
    print("Olá bem vindo, aqui você pode acessar notícias do dia! Escolha uma opção: ")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("1 - Acessar uma notícia aleatória.")
    print("2 - Acessar uma notícia randonica por um tópico especifico (Ex. Esportes, Política, Tecnologia, Entretenimento etc).")
    print("3 - Sair do programinho do Leandro")
    print("---------------------------------------------------------------------------------------------------------------------------")

    try:
        resposta = int(input())
    except ValueError:
        print("Por favor, insira um número válido.")
        continue

    if resposta == 1:
        url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-03-04&sortBy=publishedAt&language=pt&apiKey=ad00f4db7ba740e5a9fe50e718b8129b'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            artigos = data.get('articles', [])
            
            if artigos:
                artigo_aleatorio = random.choice(artigos)
                
                print("================================================")
                print("Título:", artigo_aleatorio['title'])
                print("Descrição:", artigo_aleatorio['description'])
                print("Fonte:", artigo_aleatorio['source']['name'])
                print("Publicado em:", artigo_aleatorio['publishedAt'])
                print("URL:", artigo_aleatorio['url'])
                print("================================================")
            else:
                print("Nenhuma notícia encontrada.")
        else:
            print("Erro ao acessar a API de notícias.")
            
    elif resposta == 2: 
        query = input("Digite o termo de busca: ")
        url = f'https://newsapi.org/v2/everything?q={query}&from=2024-03-04&sortBy=publishedAt&language=pt&apiKey=ad00f4db7ba740e5a9fe50e718b8129b'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            artigos = data.get('articles', [])
            
            if artigos:
                artigo_aleatorio = random.choice(artigos)
                
                print("================================================")
                print("Título:", artigo_aleatorio['title'])
                print("Descrição:", artigo_aleatorio['description'])
                print("Fonte:", artigo_aleatorio['source']['name'])
                print("Publicado em:", artigo_aleatorio['publishedAt'])
                print("URL:", artigo_aleatorio['url'])
                print("================================================")
            else:
                print("A notícia deste tópico não foi encontrada.")
        else:
            print("Erro ao acessar a API de notícias.")

    elif resposta == 3:
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida. Escolhe uma válida (1 ou 2 ou 3).")
