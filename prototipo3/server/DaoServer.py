from dataclasses import dataclass, asdict
import hashlib
from flask import jsonify
import mysql.connector
from time import time
import random

class UserDao:
    
    def connectBBDD(self):
        Connection = mysql.connector.connect(
            host= "localhost",
            user= "root",
            password = "david",
            database="tapatapp"
        )
        return Connection
    
    def getUserByToken(self, token):
        # connexion a BBDD
        conn=self.connectBBDD()
        cursor = conn.cursor(dictionary=True)
        
        # Query per validar Usr
        
        query = "Select * from User where token = '"+ token +"'"
        
        cursor.execute(query)
        user = cursor.fetchone()
        
        # cerrar conexion 
        cursor.close()
        conn.close()
            # si torna 1 registre user ok
            # si no mensaje 
        return user
    
    def login(self, identifier, password):
        # connexion a BBDD
        
        conn=self.connectBBDD()
        cursor = conn.cursor(dictionary=True)
        
        # Query per validar Usr
        
        query = """
            SELECT * FROM User
            WHERE (username = %s OR email = %s) AND password = %s
        """
        cursor.execute(query,(identifier, identifier, password))
        user = cursor.fetchone()
        token = ""
        if user:
            token = self.setTokenUser(user['username'])
            print(user)
            user['token'] = token
            
        # cerrar conexion 
        cursor.close()
        conn.close()
            # si torna 1 registre user ok
            # si no mensaje 
        return user
    
    def setTokenUser(self, username):
        # connexion a BBDD
        conn=self.connectBBDD()
        cursor = conn.cursor(dictionary=True)
        # generar Token
        token = self.getHash() #token=self.getHash(username)
        #Update a BBDD camp token al usario por username
        print(type(token))
        query = "UPDATE User SET token = '"+ token +"' WHERE username = '"+username+"'"
        
        cursor.execute(query) # Ejecuta la query 
        
        conn.commit() #siempre despues de ejecuta una query HACEMOS COMMIT
        
        """
            UPDATE * User Set token = 
            WHERE (username = %s OR email = %s) AND password = %s
        """
        # Close BBDD
        cursor.close()
        conn.close()
    
    def getHash(self):
        miliseg = str(time() * random.randrange (10000))
        data =  miliseg
        #2. crear un objeto hash utilizando el algoritmo SHA-256 y pasarle los datos a hashear
        hash_object = hashlib.sha256(data.encode('utf-8'))
        #3. obtner el resultado del hash en formato hexadecimal
        hex_dig = hash_object.hexdigest()
        
        return hex_dig



if __name__ == '__main__':
    dao = UserDao()
    u = dao.getUserByToken("963a39ec7e53dab8e2af71d4ab7e81b5d7a58896b7f01624376d9c8c29d6ceae")
    print(u)
