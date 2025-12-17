from flask import Flask, jsonify, request

#Talend API

class User:
    def __init__(self,username,nom,password,email,rol):
        self.username=username
        self.nom=nom
        self.passwords=password
        self.email=email
        self.rol=rol 
          
#us1=User(username="ana",nom="rob halford",password="12345",email="rob@gmail.com",rol="tutor")
 #print(us1)

listuser = [
    User(username="ana",nom="rob halford",password="12345",email="rob@gmail.com",rol="tutor"),
    User(username="ana",nom="rob halford",password="12345",email="rob@gmail.com",rol="tutor"),
    User(username="ana",nom="rob halford",password="12345",email="rob@gmail.com",rol="tutor")
]


class UserDao:
    def __init__(self):
        self.users=listuser
    
    def getUserByUsername(self,uname):
        user = None
        for u in self.users:
            if u.username == uname:
                user = u.__dict__
        return user

# test UserDao
'''user_dao = UserDao()
response=user_dao.getUserByUsername("maria")
print(response)
response=user_dao.getUserByUsername("AAAA")
print(response)'''
# End TEST
user_dao = UserDao()

app = Flask(__name__)

#Metodo Get User
@app.route('/user',methods=['GET'])
def user():
    resposta=""
    #parametros
    username = request.args.get("username",default="")
    # si els parametros ok
    if username !="": 
    #ira al DAO SERVER Y CERCAR user per username
        resposta=user_dao.getUserByUsername(username)
     #responta con datos usuario si es trobat 
        if resposta == None:
            resposta = {"msg" : "Usuario no encontrado"}
    else:
    # si los parametros no van ok
    # tornara error
        resposta= {"NO HAY USUARIO"}
   
    return resposta 
    return "Json salida getUserName"

if __name__ == '__main__':
    app.run(debug=True)
    
#hacer un post 
#addUser