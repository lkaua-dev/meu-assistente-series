from flask import Flask, jsonify
from assistente import AssistenteMaratona

# Ligando o Servidor Web
app = Flask(__name__)

# O Ponto de Encontro
@app.route("/")
def index():

    assistente = AssistenteMaratona()

    dados_series = assistente.processar_lista()
    return jsonify(dados_series)

if __name__ == "__main__":
    app.run(debug=True, port=5000)