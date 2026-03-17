import os
import requests
from dotenv import load_dotenv

load_dotenv()


class AssistenteMaratona:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.base_url = "http://www.omdbapi.com/"

    def buscar_serie(self, nome_da_serie):
        """
        Método com parâmetros: Vai à internet buscar uma série específica.
        """

        if not self.api_key:
            return {
                "erro_sistema": "Falha de conexão com a base de dados. (API Key ausente)"
            }

        params = {
            "apikey": self.api_key,
            "t": nome_da_serie,
            "type": "series", 
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()

            dados = response.json()

            if dados.get("Response") == "False":
                return {"titulo": nome_da_serie, "erro": "Série não encontrada."}

            return {
                "titulo": dados.get("Title"),
                "ano": dados.get("Year"),
                "nota": dados.get("imdbRating"),
            }

        except Exception as e:
            return {
                "titulo": nome_da_serie,
                "erro": "Erro: Série não encontrada ou falha de conexão.",
            }

    def processar_lista(self, lista_personalizada=None):
        """
        A Lista Fixa e o Loop (O coração da automação).
        """

        minha_lista = (
            lista_personalizada
            if lista_personalizada is not None
            else [
                "Breaking Bad",
                "Stranger Things",
                "FORMADOS",
            ]
        )

        if len(minha_lista) == 0:
            return [{"aviso": "Nenhuma série na lista"}]

        resultados_finais = []

        for serie in minha_lista:
            resultado = self.buscar_serie(serie)
            resultados_finais.append(resultado)

        return resultados_finais