import requests
from User import *

class DaoUserClient:

    def __init__(self, base_URL="http://localhost:5000/"):
        self.base_URL = base_URL  # FIX: base_URL no estaba definida en __init__

    def login(self, user):
        # Peticion HTTP al webservice /login 
        URL_peticion = self.base_URL + "login"
        params_POST = {
            "username": user.username,
            "password": user.password
        }
        try:
            response = requests.post(URL_peticion, json=params_POST)
            if response.status_code == 200:
                user_data_raw = response.json()
                code_response = user_data_raw['coderesponse']
                if code_response == '1':
                    user_raw = user_data_raw['data']  # user_raw es el dict del user
                    user = User(
                        user_raw['id'],
                        user_raw['username'],
                        "",
                        user_raw['email'],
                        user_raw['idrole'],
                        user_raw['token']
                    )
                    return user
                else:
                    return None
            else:
                return None
        except requests.exceptions.ConnectionError:
            print("ERROR: No se puede conectar al servidor. ¿Está corriendo server.py?")
            return None
    
    def getChildsByUser(self, user):
        # Peticion HTTP al webservice /Child
        URL_peticion = self.base_URL + "Child"
        params_POST = {
            "id_user": user.id
        }
        try:
            response = requests.post(URL_peticion, json=params_POST)
            if response.status_code == 200:
                data_raw = response.json()
                code_response = data_raw['coderesponse']
                if code_response == '1':
                    return data_raw['data']  # lista de dicts con los childs
                else:
                    return None
            else:
                return None
        except requests.exceptions.ConnectionError:
            print("ERROR: No se puede conectar al servidor. ¿Está corriendo server.py?")
            return None