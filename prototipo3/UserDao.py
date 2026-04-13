from dataclasses import dataclass, asdict
from flask import jsonify
import mysql.connector

class UserDao:
    
    def connectBBDD():
        Connection = mysql.conector.connect(
            host= "localhost",
            user= "root",
            password = "root",
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
        self.cursor.execute(query,(identifier, identifier, password))
        user = self.cursor.fetchone()
        
        # cerrar conexion 
        conn.cursor.close()
        conn.close()
            # si torna 1 registre user ok
            # si no mensaje 
        
        return user