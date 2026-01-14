from flask import Flask, jsonify, request

#conexion cliente servidor 
#Talent Api tester
# Clase User
class User:
    def __init__(self, username, nom, password, email, rol="tutor"):
        self.username = username
        self.nom = nom
        self.password = password  # Corregido: de passwords a password
        self.email = email
        self.rol = rol 
    
    def __str__(self):
        return self.nom

# Base de datos inicial
listuser = [
    User(username="rob", nom="rob halford", password="54321", email="rob@gmail.com", rol="tutor"),
    User(username="ana", nom="ana McCastillon", password="12345", email="ana@gmail.com", rol="tutor"),
    User(username="John", nom="John Cannigan", password="12345", email="john@gmail.com", rol="tutor")
]

# Data Access Object
class UserDao:
    def __init__(self):
        self.users = listuser
    
    def getUserByUsername(self, uname):
        for u in self.users:
            if u.username == uname:
                return u.__dict__  # Retorna como diccionario
        return None
    
    def addUser(self, u):
        self.users.append(u)
        return u
    
    def getAllUsers(self):
        return [user.__dict__ for user in self.users]
    
    def userExists(self, username):
        return any(u.username == username for u in self.users)

# Una sola instancia de UserDao
user_dao = UserDao()

app = Flask(__name__)

# ========== ENDPOINT GET (obtener usuario) ==========
@app.route('/user', methods=['GET'])
def get_user():
    username = request.args.get("username", default="")
    
    if username != "": 
        user = user_dao.getUserByUsername(username)
        if user:
            return jsonify(user)  # Retorna el usuario encontrado
        else:
            return jsonify({"msg": "Usuario no encontrado"}), 404
    else:
        return jsonify({"error": "Debe proporcionar un username"}), 400

# ========== ENDPOINT POST (añadir usuario) ==========
@app.route('/user', methods=['POST'])
def add_user():
    try:
        # Obtener datos del cuerpo de la petición (JSON)
        data = request.get_json()
        
        # Validar campos requeridos
        required_fields = ['username', 'nom', 'password', 'email']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Campo requerido faltante: {field}"}), 400
        
        # Verificar si el usuario ya existe
        if user_dao.userExists(data['username']):
            return jsonify({"error": "El usuario ya existe"}), 409
        
        # Crear nuevo usuario
        rol = data.get('rol', 'tutor')  # Valor por defecto si no se proporciona
        new_user = User(
            username=data['username'],
            nom=data['nom'],
            password=data['password'],
            email=data['email'],
            rol=rol
        )
        
        # Añadir a la base de datos
        user_dao.addUser(new_user)
        
        # Retornar respuesta exitosa
        return jsonify({
            "msg": "Usuario creado exitosamente",
            "user": new_user.__dict__
        }), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ========== ENDPOINT GET ALL (obtener todos los usuarios) ==========
@app.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = user_dao.getAllUsers()
        return jsonify({
            "count": len(users),
            "users": users
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ========== ENDPOINT DELETE (eliminar usuario) ==========
@app.route('/user/<username>', methods=['DELETE'])
def delete_user(username):
    try:
        # Buscar usuario
        for i, user in enumerate(user_dao.users):
            if user.username == username:
                # Eliminar usuario
                deleted_user = user_dao.users.pop(i)
                return jsonify({
                    "msg": "Usuario eliminado",
                    "user": deleted_user.__dict__
                }), 200
        
        return jsonify({"error": "Usuario no encontrado"}), 404
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ========== ENDPOINT PUT (actualizar usuario) ==========
@app.route('/user/<username>', methods=['PUT'])
def update_user(username):
    try:
        data = request.get_json()
        
        # Buscar usuario
        for user in user_dao.users:
            if user.username == username:
                # Actualizar campos (si se proporcionan)
                if 'nom' in data:
                    user.nom = data['nom']
                if 'password' in data:
                    user.password = data['password']
                if 'email' in data:
                    user.email = data['email']
                if 'rol' in data:
                    user.rol = data['rol']
                
                return jsonify({
                    "msg": "Usuario actualizado",
                    "user": user.__dict__
                }), 200
        
        return jsonify({"error": "Usuario no encontrado"}), 404
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ========== RUTA PRINCIPAL ==========
@app.route('/')
def index():
    return jsonify({
        "message": "API de usuarios",
        "endpoints": {
            "GET /user?username=<username>": "Obtener un usuario",
            "GET /users": "Obtener todos los usuarios",
            "POST /user": "Crear nuevo usuario (JSON body)",
            "PUT /user/<username>": "Actualizar usuario",
            "DELETE /user/<username>": "Eliminar usuario"
        }
    })

if __name__ == '__main__':
    print("=== Servidor iniciado ===")
    print("Endpoints disponibles:")
    print("  GET  http://localhost:5000/")
    print("  GET  http://localhost:5000/user?username=ana")
    print("  GET  http://localhost:5000/users")
    print("  POST http://localhost:5000/user")
    print("  PUT  http://localhost:5000/user/ana")
    print("  DELETE http://localhost:5000/user/ana")
    print("==========================")
    app.run(debug=True, host='0.0.0.0', port=5000)

    
#hacer un post 
#addUser