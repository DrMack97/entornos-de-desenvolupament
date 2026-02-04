from flask import Flask, request, jsonify


app = Flask(__name__)


# 🔹 POST amb JSON
@app.route("/login", methods=["POST"])
def login():
   
    data = request.get_json()


    if not data:
        return jsonify({"error": "JSON requerit"}), 400


    user = data.get("user")
    password = data.get("password")


    if user == "admin" and password == "1234":
        return jsonify({
            "status": "ok",
            "message": "Login correcte"
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Credencials incorrectes"
        }), 401




# 🔹 POST amb application/x-www-form-urlencoded
@app.route("/register", methods=["POST"])
def register():
    nom = request.form.get("nom")
    email = request.form.get("email")


    if not nom or not email:
        return jsonify({"error": "Falten camps"}), 400


    return jsonify({
        "message": "Usuari registrat",
        "nom": nom,
        "email": email
    })




# 🔹 POST amb Headers (API KEY)
@app.route("/secure", methods=["POST"])
def secure():
    api_key = request.headers.get("apikey")


    if api_key != "123456":
        return jsonify({"error": "API Key incorrecta"}), 403


    return jsonify({"message": "Accés autoritzat"})




# 🔹 POST amb text/plain
@app.route("/text", methods=["POST"])
def text():
    content = request.data.decode("utf-8")


    return jsonify({
        "message": "Text rebut",
        "content": content
    })




if __name__ == "__main__":
    app.run(debug=True)
