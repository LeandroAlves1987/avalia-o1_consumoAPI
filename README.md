# Avaliação de Desenvolvomento WEB III - Consumo de API's - Fornecedor de notícias aleatórias.

## Introdução

Este programa foi desenvolvido para permitir aos usuários acessar notícias aleatórias ou específicas de diferentes tópicos, utilizando a API da "NewsAPI". Este apresenta um menu interativo contendo 3 opções.

## Funcionalidades

### 1. Acessar uma notícia aleatória:

Ao selecionar esta opção (a primeira), o programa acessa a API da NewsAPI e busca notícias relacionadas à palavra-chave da "tesla" (que foi concedido como padrão) publicadas após a data de 4 de março de 2024. Ele então exibe um artigo aleatório entre os resultados obtidos, mostrando:

- Título da notícia
- Descrição
- Fonte (nome do veículo de mídia)
- Data de publicação
- URL para o acesso a notícia completa, caso disperte curiosidade do usuário

### 2. Acessar uma notícia aleatória por um tópico específico:

Nesta opção, o usuário pode digitar um termo de busca específico (por exemplo, "Esportes", "Política", "Tecnologia", "Entretenimento", etc.). O programa então realiza uma consulta da API com base neste tópico de busca e exibe um artigo aleatório dos resultados, mostrando:

- Título da notícia
- Descrição
- Fonte (nome do veículo de mídia)
- Data de publicação
- URL para acessar a notícia completa

### 3. Sair do programa

Esta opção basicamente permite ao usuário encerrar o programa e sair.

## Requisitos

- Python 3.x
- Biblioteca `requests`
- Chave de API da NewsAPI

## Notas Adicionais

- É importante que haja internet para garantir o funcionamento da aplicação.
- O programa pode haver limitações. Portanto é necessário respeitar seus limites.
- O programa foi projetado exculsivamente para buscar notícias em português, de modo em que o usuário entenda melhor e de forma confortável os artigos fornecidos.
