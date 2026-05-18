import mysql.connector
import hashlib
from time import time
import random


class UserDAO:
    """
    Data Access Object para gestionar usuarios en la base de datos.
    Proporciona métodos para login, validación de tokens y gestión de usuarios.
    """

    def __init__(self, host="localhost", user="root", password="david", database="tapatapp"):
        """
        Inicializa el DAO con los parámetros de conexión a la BD.
        
        Args:
            host (str): Host de la base de datos
            user (str): Usuario de la BD
            password (str): Contraseña de la BD
            database (str): Nombre de la base de datos
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connectBBDD(self):
        """
        Establece una conexión con la base de datos MySQL.
        
        Returns:
            connection: Objeto de conexión a MySQL
        """
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return connection
        except mysql.connector.Error as err:
            print(f"Error de conexión a la BD: {err}")
            return None

    def login(self, identifier, password):
        """
        Autentica un usuario usando username o email y contraseña.
        
        Args:
            identifier (str): Username o email del usuario
            password (str): Contraseña del usuario
        
        Returns:
            dict: Información del usuario con token si la autenticación es exitosa, None si falla
        """
        con = self.connectBBDD()
        if not con:
            return None
        
        cursor = con.cursor(dictionary=True)
        try:
            query = """
                SELECT id, username, email, password, idrole, token 
                FROM User
                WHERE (username = %s OR email = %s) AND password = %s
            """
            cursor.execute(query, (identifier, identifier, password))
            user = cursor.fetchone()
            
            if user:
                # Generar token y actualizarlo en la BD
                token = self.setTokenUser(user['username'])
                user['token'] = token
            
            return user
        except mysql.connector.Error as err:
            print(f"Error en login: {err}")
            return None
        finally:
            cursor.close()
            con.close()

    def loginByToken(self, token):
        """
        Valida un usuario usando un token.
        
        Args:
            token (str): Token de autenticación del usuario
        
        Returns:
            dict: Información del usuario si el token es válido, None si no lo es
        """
        con = self.connectBBDD()
        if not con:
            return None
        
        cursor = con.cursor(dictionary=True)
        try:
            query = """
                SELECT id, username, email, password, idrole, token 
                FROM User 
                WHERE token = %s
            """
            cursor.execute(query, (token,))
            user = cursor.fetchone()
            return user
        except mysql.connector.Error as err:
            print(f"Error en loginByToken: {err}")
            return None
        finally:
            cursor.close()
            con.close()

    def setTokenUser(self, username):
        """
        Genera un nuevo token para un usuario y lo almacena en la BD.
        
        Args:
            username (str): Username del usuario
        
        Returns:
            str: Token generado
        """
        con = self.connectBBDD()
        if not con:
            return ""
        
        cursor = con.cursor()
        try:
            token = self.getHash()
            query = "UPDATE User SET token = %s WHERE username = %s"
            cursor.execute(query, (token, username))
            con.commit()
            return token
        except mysql.connector.Error as err:
            print(f"Error en setTokenUser: {err}")
            return ""
        finally:
            cursor.close()
            con.close()

    def getHash(self):
        """
        Genera un hash SHA256 único basado en el tiempo y un número aleatorio.
        
        Returns:
            str: Hash SHA256 en formato hexadecimal
        """
        milliseconds = str(time() * random.randrange(10000))
        data = milliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest()

    def getUserById(self, user_id):
        """
        Obtiene la información de un usuario por su ID.
        
        Args:
            user_id (int): ID del usuario
        
        Returns:
            dict: Información del usuario si existe, None si no
        """
        con = self.connectBBDD()
        if not con:
            return None
        
        cursor = con.cursor(dictionary=True)
        try:
            query = """
                SELECT id, username, email, password, idrole, token 
                FROM User 
                WHERE id = %s
            """
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
            return user
        except mysql.connector.Error as err:
            print(f"Error en getUserById: {err}")
            return None
        finally:
            cursor.close()
            con.close()

    def getAllUsers(self):
        """
        Obtiene la lista de todos los usuarios (sin contraseñas).
        
        Returns:
            list: Lista de usuarios
        """
        con = self.connectBBDD()
        if not con:
            return []
        
        cursor = con.cursor(dictionary=True)
        try:
            query = """
                SELECT id, username, email, idrole, token 
                FROM User
            """
            cursor.execute(query)
            users = cursor.fetchall()
            return users
        except mysql.connector.Error as err:
            print(f"Error en getAllUsers: {err}")
            return []
        finally:
            cursor.close()
            con.close()
