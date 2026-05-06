import requests
from User import *
from flask import jsonify

class DaoUserClient:
    base_URL = "http://127.0.0.1:5000"

    def login(self, user):
        # Validació paràmetres 
        # TO-DO
        # Petició HTTP al Webservice /login
        URL_peticio= self.base_URL + "/login"
        params_POST = {
            "username": user.username,
            "password": user.password
        }
        response = requests.post(URL_peticio, json=params_POST)
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response=user_data_raw['coderesponse']
            if code_response == '1': # Usuari Validat  (self, id, username, password, email, idrole,token):
                user_raw=user_data_raw['data']
                user=User(user_raw['id'], user_raw['username']
                          , "" ,user_raw['email']
                          , "", user_raw['token'])
                return user
            else: 
                return None
        else:
            return None
    
    def loginToken(self, token):
        URL_peticio= self.base_URL + "/login"
        print(token)
        headers = {'Content-Type': 'application/json', 'api-token': token}
        response = requests.post(URL_peticio,headers=headers) 
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response=user_data_raw['coderesponse']
            if code_response == '1': # Usuari Validat  (self, id, username, password, email, idrole,token):
                user_raw=user_data_raw['data']
                user=User(user_raw['id'], user_raw['username']
                          , "" ,user_raw['email']
                          , "", user_raw['token'])
                return user  
        else:
            return None
    
    def getChilds(self, token):
        URL_peticio = self.base_URL + "/child"
        headers = {'Content-Type': 'application/json', 'api-token': token}
        
        try:
            response = requests.post(URL_peticio, headers=headers)
            if response.status_code == 200:
                data = response.json()
                if data.get('coderesponse') == '1':
                    return data.get('data', [])
                else:
                    print(f"Error: {data.get('msg', 'Unknown error')}")
                    return None
            else:
                print(f"HTTP Error: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error de conexión: {e}")
            return None
        
    def getChildTaps(self, token, id_child):
        URL_peticio = self.base_URL + "/taps"
        headers = {'Content-Type': 'application/json', 'api-token': token}
        data = {"id_child": id_child}
        
        try:
            response = requests.post(URL_peticio, json=data, headers=headers)
            if response.status_code == 200:
                response_data = response.json()
                if response_data.get('coderesponse') == '1':
                    return response_data.get('data', [])
                else:
                    print(f"Error: {response_data.get('msg', 'Unknown error')}")
                    return None
            else:
                print(f"HTTP Error: {response.status_code}")
                return None
        except Exception as e:
            print(f"Connection error: {e}")
            return None

    
    
daoUserClient=DaoUserClient()
resposta=daoUserClient.loginToken("20732fb71deb93f1ec163dc3b03aaafddfff76ccfdf45150e94d01eb099eb651")
print(resposta)
'''
user=User("", "mare", "12345", "", "", "")
resposta=daoUserClient.login(user)
print(resposta)
'''
'''Servei Login
End-point: /login
Method: POST
Estat: Public
Tipus petició : application/json
Paramètres:

username : (string) username o email
password : (string) password
Resposta Usuari validat Ok:
http Response Code: 200 ok

{
  "coderesponse": "1",
  "data": {
    "email": "prova@gmail.com",
    "id": 1,
    "idrole": 1,
    "password": "12345",
    "token": "",
    "username": "mare"
  },
  "msg": "Authenticated"
}
Resposta Usuari No validat: http Response Code: 400 ok

{
     "coderesponse": "0"
     "msg": "No validat"
}
'''
