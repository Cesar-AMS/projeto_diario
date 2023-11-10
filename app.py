from flask import Flask, render_template


app = Flask(__name__)

# rotas e funções


@app.route("/")
def home():
    return render_template("home.html")


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
