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
        query = "Update User Set taken = '"+ token +"' where username = '"+username+"'"
        print(query)
        cursor.execute(query)
        
        """
            UPDATE * User Set token = 
            WHERE (username = %s OR email = %s) AND password = %s
        """
        # Close BBDD
        cursor.close()
        conn.close()
    
    def getHash(self, username=""):
        miliseg = str(int(time() * 1000))
        data = username + miliseg
        #2. crear un objeto hash utilizando el algoritmo SHA-256 y pasarle los datos a hashear
        hash_object = hashlib.sha256(data.encode('utf-8'))
        #3. obtner el resultado del hash en formato hexadecimal
        hex_dig = hash_object.hexdigest()
        
        return hex_dig
    
        
dao=UserDao()
print(dao.getHash("usr1",))

u=dao.login("mare","mare")
print(u)


miliseg = str(int(time() * 1000))
print("Time in milliseconds:", miliseg)

data = "Hola world" + miliseg
print(data)

