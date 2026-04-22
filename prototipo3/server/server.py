from flask import Flask, request, jsonify
from DaoServer import UserDao
from dataclasses import dataclass, asdict

@dataclass
class ApiResponse():
    msg: str
    coderesponse: str
    data: list  # FIX: 'list' era demasiado restrictivo, puede ser None o dict

# Instantiate DAOs
userDao = UserDao()

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    identifier = data.get('username')  # username o email
    password = data.get('password')
    user = userDao.login(identifier, password)
    
    response = ApiResponse(
        msg="login",
        coderesponse="1",
        data=user
    )
    
    if user:
        response = ApiResponse(
            msg="Authenticated",
            coderesponse="1",
            data=user  # FIX: serializar el objeto User como dict
        )
        return jsonify(asdict(response)), 200
    else:
        response = ApiResponse(
            msg="Not authenticated",
            coderesponse="0",
            data=None
        )
        return jsonify(asdict(response)), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
    '''@app.route('/getusers', methods=['GET'])
def getusers():
    response = ApiResponse(
        msg="All Users",
        coderesponse="1",
        data=userDao.getAllUsers()
    )
    return jsonify(asdict(response)), 200'''