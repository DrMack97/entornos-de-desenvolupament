app = Flask(__name__)

@app.route("/user", methods=['GET'])
def user():
    repuesta = ""
    #parametros 
    username = request.args.get("username",default="")
    #si los parametros ok 
    if username !="":
        #
        respuesta=user.dao.getUserByUsername(username)
        #
        