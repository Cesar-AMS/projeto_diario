# app.py
from flask import Flask, render_template, request
from tratacao.tratamento import TratamentoDados

app = Flask(__name__)
tratamento = TratamentoDados()

@app.route("/", methods=["GET", "POST"])
def home():
    resposta = None

    if request.method == "POST":
        # Obter a entrada do usuário do formulário
        entrada_usuario = request.form.get("entrada_usuario")

        # Processar a entrada usando a classe TratamentoDados
        resposta = tratamento.processar_entrada(entrada_usuario)

    return render_template("home.html", resposta=resposta)

# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
