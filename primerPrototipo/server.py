from flask import Flask, jsonify, request

app = Flask (__name__)

class User:
    def __init__(self,username,nom,password,email,rol):
        self.username=username
        self.nom=nom
        self.passwords=password
        self.email=email
        self.rol=rol 
        
        
us1=User(username="ana",nom="rob halford",password="12345",email="rob@gmail.com",rol="tutor")
 

listuser = [
    User(username="ana",nom="rob halford",password="12345",email="rob@gmail.com",rol="tutor"),
    User(username="ana",nom="rob halford",password="12345",email="rob@gmail.com",rol="tutor"),
    User(username="ana",nom="rob halford",password="12345",email="rob@gmail.com",rol="tutor")
]

class UserDao:
    def __int__(self):
        self.users = listuser
        
    def getUserByUsername(self,username):
        
        return "AAAA"


@app.route('/user',methods=['GET'])
def user():
    resposta=""
    #parametros
    username = request.args.get("username",default="")
    # si els parametros ok
    if username !="": 
    #ira al DAO SERVER Y CERCAR user per username
    # respondra con datos usuario si es trobat 
        #resposta=("username"+ UserDao.getUserByUsername(username))
        resposta="sasasas"+username
    else:
    # si los parametros no van ok
    # tornara error
        resposta="NO HAY USUARIO"
   
    return resposta 
    return "Json salida getUserName"

if __name__ == '__main__':
    app.run(debug=True)