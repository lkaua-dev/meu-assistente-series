# Assistente de Maratona 🍿

Uma API local desenvolvida em Python com Flask que consome a API do OMDb para buscar informações sobre séries de TV (título, ano de lançamento e avaliação no IMDb). 

## 🚀 Funcionalidades
* **Busca de Séries:** Retorna dados em formato JSON das séries solicitadas.
* **Tratamento de Erros:** Sistema blindado contra falhas na API, séries inexistentes e listas vazias.
* **Segurança:** Uso de variáveis de ambiente (`.env`) para proteger a API Key.
* **Arquitetura:** Construído utilizando Programação Orientada a Objetos (POO).

## 🛠️ Tecnologias Utilizadas
* Python 3
* Flask (Servidor Backend)
* Requests (Consumo de API Externa)
* python-dotenv (Gestão de Variáveis de Ambiente)

## ⚙️ Como rodar o projeto localmente

1. Clone este repositório:
    ```bash
    git clone https://github.com/lkaua-dev/meu-assistente-series.git
    ```

2. Entre na pasta do projeto:
    ```bash
    cd meu-assistente-series
    ```

3. Crie e ative o ambiente virtual (Windows):
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

4. Instale as bibliotecas necessárias:
    ```bash
    pip install -r requirements.txt
    ```

5. Crie um arquivo chamado .env na raiz do projeto e adicione a sua chave da OMDb API:
    ```bash
    API_KEY=coloque_sua_chave_aqui
    ```

6. Inicie o servidor:
    ```bash
    python app.py
    ```

7. Acesse no navegador:
    ```bash
    http://localhost:5000
    ```
