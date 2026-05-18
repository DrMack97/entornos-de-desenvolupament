# Prototipo 4 - WebService de Login con Flask

## Descripción

WebService REST implementado con Flask que proporciona autenticación de usuarios mediante:
- Login con username/email y password
- Validación de usuarios mediante token

## Estructura

```
prototipo4/
├── DaoUser.py           # Data Access Object para gestionar usuarios
├── app.py               # Aplicación Flask con endpoints
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Este archivo
```

## Requisitos

- Python 3.7+
- MySQL 5.7+
- Base de datos `tapatapp` con tabla `User`

## Instalación

1. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

2. **Verificar conexión a BD:**
   - Asegurar que MySQL está en ejecución
   - La BD debe tener la tabla `User` con columnas: id, username, password, email, idrole, token
   - Credenciales por defecto en `DaoUser.py`:
     - Host: localhost
     - User: root
     - Password: david
     - Database: tapatapp

## Ejecución

```bash
python app.py
```

El servidor estará disponible en: `http://localhost:5000`

## Endpoints

### 1. Login con Credenciales

**Endpoint:** `POST /login`

**Content-Type:** `application/json`

**Request Body:**
```json
{
    "username": "mare",
    "password": "12345"
}
```

**Respuesta Exitosa (200):**
```json
{
    "coderesponse": "1",
    "data": {
        "email": "prova@gmail.com",
        "id": 1,
        "idrole": 1,
        "password": "12345",
        "token": "hash_token_generado",
        "username": "mare"
    },
    "msg": "Authenticated"
}
```

**Respuesta Fallida (400):**
```json
{
    "coderesponse": "0",
    "msg": "No validat"
}
```

---

### 2. Login por Token

**Endpoint:** `POST /login`

**Headers:**
```
Authorization: Bearer token_value
Content-Type: application/json
```

**Respuesta Exitosa (200):**
```json
{
    "id": 1,
    "username": "mare",
    "email": "prova@gmail.com",
    "token": "token_hash",
    "idrole": "1",
    "msg": "Usuari Ok",
    "coderesponse": "1"
}
```

**Respuesta Fallida (400):**
```json
{
    "coderesponse": "0",
    "msg": "No validat"
}
```

---

### 3. Obtener todos los usuarios

**Endpoint:** `GET /users`

**Respuesta Exitosa (200):**
```json
{
    "coderesponse": "1",
    "data": [
        {
            "id": 1,
            "username": "mare",
            "email": "prova@gmail.com",
            "idrole": 1,
            "token": "token_hash"
        }
    ],
    "msg": "Usuarios obtenidos"
}
```

---

### 4. Obtener usuario por ID

**Endpoint:** `GET /users/<user_id>`

**Respuesta Exitosa (200):**
```json
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
```

**Respuesta Fallida (404):**
```json
{
    "coderesponse": "0",
    "msg": "Usuario no encontrado"
}
```

---

### 5. Health Check

**Endpoint:** `GET /health`

**Respuesta (200):**
```json
{
    "status": "ok",
    "message": "Servidor funcionando correctamente"
}
```

## Pruebas con cURL

### Login con credenciales:
```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"mare","password":"12345"}'
```

### Login con token:
```bash
curl -X POST http://localhost:5000/login \
  -H "Authorization: Bearer token_aqui" \
  -H "Content-Type: application/json"
```

### Obtener todos los usuarios:
```bash
curl http://localhost:5000/users
```

### Obtener usuario por ID:
```bash
curl http://localhost:5000/users/1
```

### Health check:
```bash
curl http://localhost:5000/health
```

## Notas

- El token se genera automáticamente en el login y se almacena en la BD
- Los tokens se generan usando SHA256 con timestamp aleatorio
- Las contraseñas se almacenan en texto plano en la BD (considere usar hash en producción)
- El servidor corre en modo debug (`debug=True`) - cambiar para producción
- Los mensajes de error devuelven información del servidor - considerar limitar en producción
