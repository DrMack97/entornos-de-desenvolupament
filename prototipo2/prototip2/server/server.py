from flask import Flask, request, jsonify
from DaoServer import UserDAO, ChildDao
from dadesServer import *
from dataclasses import dataclass, asdict

@dataclass
class ApiResponse():
    msg: str
    coderesponse: str
    data: object  # FIX: 'list' era demasiado restrictivo, puede ser None o dict

# Instantiate DAOs
userDao = UserDAO()
childDao = ChildDao()

app = Flask(__name__)

@app.route('/getusers', methods=['GET'])
def getusers():
    response = ApiResponse(
        msg="All Users",
        coderesponse="1",
        data=userDao.getAllUsers()
    )
    return jsonify(asdict(response)), 200


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    identifier = data.get('username')  # username o email
    password = data.get('password')
    user = userDao.login(identifier, password)

    if user:
        response = ApiResponse(
            msg="Authenticated",
            coderesponse="1",
            data=user.__dict__  # FIX: serializar el objeto User como dict
        )
        return jsonify(asdict(response)), 200
    else:
        response = ApiResponse(
            msg="Not authenticated",
            coderesponse="0",
            data=None
        )
        return jsonify(asdict(response)), 200


@app.route('/Child', methods=['POST'])
def child():
    data = request.get_json()
    user_id = data.get('id_user')

    response = ApiResponse(msg="Child", coderesponse="-1", data="")

    # FIX: validación corregida (la original tenía typos y lógica incorrecta)
    if user_id is None:
        return jsonify(asdict(response)), 400

    try:
        user_id = int(user_id)
    except (ValueError, TypeError):
        return jsonify(asdict(response)), 400

    u = User(id=user_id, username="", password="", email="", idrole=1, token="")
    listChilds = childDao.getChild(u)  # FIX: era getChilds (typo)
    response.coderesponse = "1"        # FIX: era corereponse (typo)
    response.msg = str(len(listChilds))
    response.data = listChilds
    return jsonify(asdict(response)), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)