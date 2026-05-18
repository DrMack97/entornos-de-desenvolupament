from flask import Flask, request, jsonify
from DaoUser import UserDAO
import json

app = Flask(__name__)

# Instancia del DAO
dao = UserDAO()


@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint para autenticación de usuarios.
    
    Acepta dos formas de autenticación:
    1. Con username/email y password
    2. Con token en el header Authorization
    
    POST /login
    Content-Type: application/json
    
    Forma 1 - Con credenciales:
    {
        "username": "mare",
        "password": "12345"
    }
    
    Forma 2 - Con token (en header):
    Authorization: Bearer token_value
    
    Returns:
        Respuesta exitosa (200):
        {
            "coderesponse": "1",
            "data": {
                "email": "prova@gmail.com",
                "id": 1,
                "idrole": 1,
                "password": "12345",
                "token": "token_hash",
                "username": "mare"
            },
            "msg": "Authenticated"
        }
        
        Respuesta fallida (400):
        {
            "coderesponse": "0",
            "msg": "No validat"
        }
    """
    try:
        # Verificar si hay autenticación por token en el header
        auth_header = request.headers.get('Authorization')
        
        if auth_header:
            # Extraer token del header "Bearer token_value"
            parts = auth_header.split()
            if len(parts) == 2 and parts[0].lower() == 'bearer':
                token = parts[1]
                user = dao.loginByToken(token)
                
                if user:
                    return jsonify({
                        "id": user['id'],
                        "username": user['username'],
                        "email": user['email'],
                        "token": user['token'],
                        "idrole": str(user['idrole']),
                        "msg": "Usuari Ok",
                        "coderesponse": "1"
                    }), 200
                else:
                    return jsonify({
                        "coderesponse": "0",
                        "msg": "No validat"
                    }), 400
            else:
                return jsonify({
                    "coderesponse": "0",
                    "msg": "Formato de Authorization inválido"
                }), 400
        
        # Autenticación por username/email y password
        data = request.get_json()
        
        # Validar que lleguen los parámetros necesarios
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({
                "coderesponse": "0",
                "msg": "Parámetros faltantes (username, password)"
            }), 400
        
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()
        
        # Validar que los parámetros no estén vacíos
        if not username or not password:
            return jsonify({
                "coderesponse": "0",
                "msg": "Username y password no pueden estar vacíos"
            }), 400
        
        # Realizar login
        user = dao.login(username, password)
        
        if user:
            return jsonify({
                "coderesponse": "1",
                "data": {
                    "email": user['email'],
                    "id": user['id'],
                    "idrole": user['idrole'],
                    "password": user['password'],
                    "token": user['token'],
                    "username": user['username']
                },
                "msg": "Authenticated"
            }), 200
        else:
            return jsonify({
                "coderesponse": "0",
                "msg": "No validat"
            }), 400
    
    except Exception as e:
        print(f"Error en el endpoint /login: {str(e)}")
        return jsonify({
            "coderesponse": "0",
            "msg": f"Error en el servidor: {str(e)}"
        }), 500


@app.route('/users', methods=['GET'])
def get_all_users():
    """
    Endpoint para obtener todos los usuarios (sin contraseñas).
    
    GET /users
    
    Returns:
        Respuesta exitosa (200):
        {
            "coderesponse": "1",
            "data": [
                {
                    "id": 1,
                    "username": "mare",
                    "email": "prova@gmail.com",
                    "idrole": 1,
                    "token": ""
                },
                ...
            ],
            "msg": "Usuarios obtenidos"
        }
    """
    try:
        users = dao.getAllUsers()
        return jsonify({
            "coderesponse": "1",
            "data": users,
            "msg": "Usuarios obtenidos"
        }), 200
    except Exception as e:
        print(f"Error en el endpoint /users: {str(e)}")
        return jsonify({
            "coderesponse": "0",
            "msg": f"Error en el servidor: {str(e)}"
        }), 500


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Endpoint para obtener la información de un usuario específico.
    
    GET /users/<user_id>
    
    Returns:
        Respuesta exitosa (200):
        {
            "coderesponse": "1",
            "data": {
                "id": 1,
                "username": "mare",
                "email": "prova@gmail.com",
                "idrole": 1,
                "token": "token_hash"
            },
            "msg": "Usuario encontrado"
        }
        
        Respuesta fallida (404):
        {
            "coderesponse": "0",
            "msg": "Usuario no encontrado"
        }
    """
    try:
        user = dao.getUserById(user_id)
        
        if user:
            return jsonify({
                "coderesponse": "1",
                "data": user,
                "msg": "Usuario encontrado"
            }), 200
        else:
            return jsonify({
                "coderesponse": "0",
                "msg": "Usuario no encontrado"
            }), 404
    
    except Exception as e:
        print(f"Error en el endpoint /users/<id>: {str(e)}")
        return jsonify({
            "coderesponse": "0",
            "msg": f"Error en el servidor: {str(e)}"
        }), 500


@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint para verificar que el servidor está funcionando.
    
    GET /health
    
    Returns:
        {
            "status": "ok",
            "message": "Servidor funcionando correctamente"
        }
    """
    return jsonify({
        "status": "ok",
        "message": "Servidor funcionando correctamente"
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Manejador para errores 404"""
    return jsonify({
        "coderesponse": "0",
        "msg": "Endpoint no encontrado"
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Manejador para método no permitido"""
    return jsonify({
        "coderesponse": "0",
        "msg": "Método no permitido"
    }), 405


if __name__ == '__main__':
    # Ejecutar la aplicación Flask en modo debug
    # puerto 5000, accesible desde cualquier interfaz
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
