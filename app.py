from flask import Flask, render_template, request, jsonify
from tratacao.controlador import ControladorPreprocessamento

app = Flask(__name__)

controlador_preprocessamento = ControladorPreprocessamento()

@app.route("/", methods=["GET", "POST"])
def minha_rota():
    if request.method == "GET":
        # Lógica para tratamento de solicitações GET
        return render_template("pagina_principal.html")

    elif request.method == "POST":
        # Lógica para tratamento de solicitações POST
        entrada_usuario = request.form.get("entrada_usuario")

        # Validar se a entrada do usuário está presente
        if entrada_usuario:
            # Processar a entrada usando o ControladorPreprocessamento
            resposta_tratada = controlador_preprocessamento.preprocessar(entrada_usuario)

            # Retornar o resultado como JSON
            return jsonify({"entrada": entrada_usuario, "resposta": {"resposta_tratada": resposta_tratada}})

        # Se a entrada do usuário não estiver presente, retornar uma resposta de erro (opcional)
        return jsonify({"erro": "Entrada do usuário não fornecida"})

if __name__ == "__main__":
    app.run(debug=True)
