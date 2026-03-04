import requests
from User import *
from flask import jsonify

class DaoUserClient:

    def login(self, User):
        #validacion de parametros
        #TO-DO
        #peticion HTTP al webservice /login 
        URL_peticion = self.base_URL + "login"
        params_POST = {
            "username": user.username,
            "password": user.password
        }
        response = requests.post(URL_peticion, json=params_POST)
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response = user_data_raw['coderesponse']
            if code_response == '1': #
                user= User(user_data_raw['id'], user_data_raw['username']
                        , "" , user_data_raw['email']
                        , user_data_raw['idrole'], user_data_raw['token'])
            else:
                return None
        else:
            return None