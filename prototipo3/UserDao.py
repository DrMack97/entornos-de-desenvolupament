from dataclasses import dataclass, asdict
from flask import jsonify
import mysql.connector

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
    
dao=UserDao()
u=dao.login("mate","mate")
print(u)