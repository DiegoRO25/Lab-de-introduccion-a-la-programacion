from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ultimo_codigo = ""

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/scanner")
def scanner():
    return render_template("scanner.html")


@app.route("/guardar", methods=["POST"])
def guardar():
    global ultimo_codigo

    data = request.get_json()
    codigo = data["codigo"]

    ultimo_codigo = codigo

    print("Código recibido:", codigo)

    return jsonify({
        "ok": True,
        "codigo": codigo
    })


@app.route("/obtener_codigo")
def obtener_codigo():
    return jsonify({
        "codigo": ultimo_codigo
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
