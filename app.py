from flask import Flask, render_template, request, jsonify
from frete import calcular_frete

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calcular", methods=["POST"])
def calcular():
    try:
        dados = request.get_json()

        valor_carrinho = float(dados["valor_carrinho"])
        regiao = dados["regiao"]

        frete = calcular_frete(valor_carrinho, regiao)

        return jsonify({
            "frete": frete
        })

    except ValueError as erro:
        return jsonify({
            "erro": str(erro)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)