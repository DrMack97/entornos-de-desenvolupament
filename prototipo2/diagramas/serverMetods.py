import requests
import json
from datetime import datetime
from typing import List, Optional, Dict, Any
from abc import ABC, abstractmethod

# =============================================
# CLASES DE MODELO (ENTIDADES)
# =============================================

class User:
    def __init__(self, id: int, username: str, password: str, email: str, idrole: int):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.idrole = idrole
    
    def to_dict(self) -> Dict[str, Any]:
        """Convierte el objeto User a diccionario para JSON"""
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'idrole': self.idrole
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        """Crea un objeto User desde un diccionario"""
        return cls(
            id=data.get('id'),
            username=data.get('username'),
            password=data.get('password'),
            email=data.get('email'),
            idrole=data.get('idrole')
        )
    
    def __str__(self):
        return f"{self.username}:{self.password}:{self.email}"


class Child:
    def __init__(self, id: int, child_name: str, sleep_average: float, treatment_id: int, time: int):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'child_name': self.child_name,
            'sleep_average': self.sleep_average,
            'treatment_id': self.treatment_id,
            'time': self.time
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Child':
        return cls(
            id=data.get('id'),
            child_name=data.get('child_name'),
            sleep_average=data.get('sleep_average'),
            treatment_id=data.get('treatment_id'),
            time=data.get('time')
        )


class Tap:
    def __init__(self, id: int, child_id: int, status_id: int, user_id: int, init: str, end: Optional[str] = None):
        self.id = id
        self.child_id = child_id
        self.status_id = status_id
        self.user_id = user_id
        self.init = init
        self.end = end
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'child_id': self.child_id,
            'status_id': self.status_id,
            'user_id': self.user_id,
            'init': self.init,
            'end': self.end
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Tap':
        return cls(
            id=data.get('id'),
            child_id=data.get('child_id'),
            status_id=data.get('status_id'),
            user_id=data.get('user_id'),
            init=data.get('init'),
            end=data.get('end')
        )


class Status:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'name': self.name}
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Status':
        return cls(id=data.get('id'), name=data.get('name'))


class Role:
    def __init__(self, id: int, type_rol: str):
        self.id = id
        self.type_rol = type_rol
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'type_rol': self.type_rol}
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Role':
        return cls(id=data.get('id'), type_rol=data.get('type_rol'))


class Treatment:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
    
    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'name': self.name}
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Treatment':
        return cls(id=data.get('id'), name=data.get('name'))


class UserChildRelation:
    def __init__(self, user_id: int, child_id: int, rol_id: int):
        self.user_id = user_id
        self.child_id = child_id
        self.rol_id = rol_id
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'user_id': self.user_id,
            'child_id': self.child_id,
            'rol_id': self.rol_id
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserChildRelation':
        return cls(
            user_id=data.get('user_id'),
            child_id=data.get('child_id'),
            rol_id=data.get('rol_id')
        )


# =============================================
# CLASE BASE PARA CONEXIÓN AL SERVIDOR
# =============================================

class APIClient:
    """Cliente HTTP para comunicación con el servidor"""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None, timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()
        
        # Configurar headers comunes
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})
    
    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """Maneja la respuesta HTTP y convierte a JSON"""
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP: {e}")
            print(f"Respuesta: {response.text}")
            raise
        except json.JSONDecodeError as e:
            print(f"Error JSON: {e}")
            raise
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Realiza una petición GET"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.get(url, params=params, timeout=self.timeout)
        return self._handle_response(response)
    
    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Realiza una petición POST"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.post(url, json=data, timeout=self.timeout)
        return self._handle_response(response)
    
    def put(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Realiza una petición PUT"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.put(url, json=data, timeout=self.timeout)
        return self._handle_response(response)
    
    def delete(self, endpoint: str) -> Dict[str, Any]:
        """Realiza una petición DELETE"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.delete(url, timeout=self.timeout)
        return self._handle_response(response)


# =============================================
# INTERFACES DAO (ABSTRACTAS)
# =============================================

class BaseDAO(ABC):
    """Clase base abstracta para todos los DAOs"""
    
    def __init__(self, api_client: APIClient):
        self.api_client = api_client


class IUserDAO(BaseDAO, ABC):
    @abstractmethod
    def create(self, user: User) -> int:
        pass
    
    @abstractmethod
    def read(self, user_id: int) -> Optional[User]:
        pass
    
    @abstractmethod
    def update(self, user: User) -> bool:
        pass
    
    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass
    
    @abstractmethod
    def find_all(self) -> List[User]:
        pass
    
    @abstractmethod
    def authenticate(self, username: str, password: str) -> Optional[User]:
        pass
    
    @abstractmethod
    def find_by_username(self, username: str) -> Optional[User]:
        pass
    
    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        pass


class IChildDAO(BaseDAO, ABC):
    @abstractmethod
    def create(self, child: Child) -> int:
        pass
    
    @abstractmethod
    def read(self, child_id: int) -> Optional[Child]:
        pass
    
    @abstractmethod
    def update(self, child: Child) -> bool:
        pass
    
    @abstractmethod
    def delete(self, child_id: int) -> bool:
        pass
    
    @abstractmethod
    def find_all(self) -> List[Child]:
        pass
    
    @abstractmethod
    def find_by_name(self, name: str) -> List[Child]:
        pass
    
    @abstractmethod
    def find_by_treatment(self, treatment_id: int) -> List[Child]:
        pass
    
    @abstractmethod
    def update_sleep_average(self, child_id: int, new_average: float) -> bool:
        pass


class ITapDAO(BaseDAO, ABC):
    @abstractmethod
    def create(self, tap: Tap) -> int:
        pass
    
    @abstractmethod
    def read(self, tap_id: int) -> Optional[Tap]:
        pass
    
    @abstractmethod
    def update(self, tap: Tap) -> bool:
        pass
    
    @abstractmethod
    def delete(self, tap_id: int) -> bool:
        pass
    
    @abstractmethod
    def find_all(self) -> List[Tap]:
        pass
    
    @abstractmethod
    def find_by_child(self, child_id: int) -> List[Tap]:
        pass
    
    @abstractmethod
    def find_by_user(self, user_id: int) -> List[Tap]:
        pass
    
    @abstractmethod
    def find_by_status(self, status_id: int) -> List[Tap]:
        pass
    
    @abstractmethod
    def find_by_date_range(self, start_date: str, end_date: str) -> List[Tap]:
        pass
    
    @abstractmethod
    def close_tap(self, tap_id: int, end_time: str) -> bool:
        pass


# =============================================
# IMPLEMENTACIONES CONCRETAS DE DAO
# =============================================

class UserDAO(IUserDAO):
    """Implementación concreta de UserDAO que se comunica con la API"""
    
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)
        self.endpoint = "users"
    
    def create(self, user: User) -> int:
        """Crea un nuevo usuario en el servidor"""
        try:
            response = self.api_client.post(f"/{self.endpoint}", user.to_dict())
            return response.get('id')
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return -1
    
    def read(self, user_id: int) -> Optional[User]:
        """Obtiene un usuario por ID"""
        try:
            response = self.api_client.get(f"/{self.endpoint}/{user_id}")
            return User.from_dict(response)
        except Exception as e:
            print(f"Error al leer usuario {user_id}: {e}")
            return None
    
    def update(self, user: User) -> bool:
        """Actualiza un usuario existente"""
        try:
            response = self.api_client.put(f"/{self.endpoint}/{user.id}", user.to_dict())
            return response.get('success', False)
        except Exception as e:
            print(f"Error al actualizar usuario {user.id}: {e}")
            return False
    
    def delete(self, user_id: int) -> bool:
        """Elimina un usuario"""
        try:
            response = self.api_client.delete(f"/{self.endpoint}/{user_id}")
            return response.get('success', False)
        except Exception as e:
            print(f"Error al eliminar usuario {user_id}: {e}")
            return False
    
    def find_all(self) -> List[User]:
        """Obtiene todos los usuarios"""
        try:
            response = self.api_client.get(f"/{self.endpoint}")
            users_data = response.get('users', [])
            return [User.from_dict(user_data) for user_data in users_data]
        except Exception as e:
            print(f"Error al obtener todos los usuarios: {e}")
            return []
    
    def authenticate(self, username: str, password: str) -> Optional[User]:
        """Autentica un usuario con username y password"""
        try:
            response = self.api_client.post(f"/{self.endpoint}/authenticate", {
                'username': username,
                'password': password
            })
            if response.get('authenticated'):
                return User.from_dict(response.get('user'))
            return None
        except Exception as e:
            print(f"Error en autenticación: {e}")
            return None
    
    def find_by_username(self, username: str) -> Optional[User]:
        """Busca usuario por nombre de usuario"""
        try:
            response = self.api_client.get(f"/{self.endpoint}/search", {
                'username': username
            })
            users_data = response.get('users', [])
            if users_data:
                return User.from_dict(users_data[0])
            return None
        except Exception as e:
            print(f"Error al buscar usuario por username {username}: {e}")
            return None
    
    def find_by_email(self, email: str) -> Optional[User]:
        """Busca usuario por email"""
        try:
            response = self.api_client.get(f"/{self.endpoint}/search", {
                'email': email
            })
            users_data = response.get('users', [])
            if users_data:
                return User.from_dict(users_data[0])
            return None
        except Exception as e:
            print(f"Error al buscar usuario por email {email}: {e}")
            return None


class ChildDAO(IChildDAO):
    """Implementación concreta de ChildDAO que se comunica con la API"""
    
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)
        self.endpoint = "children"
    
    def create(self, child: Child) -> int:
        """Crea un nuevo niño en el servidor"""
        try:
            response = self.api_client.post(f"/{self.endpoint}", child.to_dict())
            return response.get('id')
        except Exception as e:
            print(f"Error al crear niño: {e}")
            return -1
    
    def read(self, child_id: int) -> Optional[Child]:
        """Obtiene un niño por ID"""
        try:
            response = self.api_client.get(f"/{self.endpoint}/{child_id}")
            return Child.from_dict(response)
        except Exception as e:
            print(f"Error al leer niño {child_id}: {e}")
            return None
    
    def update(self, child: Child) -> bool:
        """Actualiza un niño existente"""
        try:
            response = self.api_client.put(f"/{self.endpoint}/{child.id}", child.to_dict())
            return response.get('success', False)
        except Exception as e:
            print(f"Error al actualizar niño {child.id}: {e}")
            return False
    
    def delete(self, child_id: int) -> bool:
        """Elimina un niño"""
        try:
            response = self.api_client.delete(f"/{self.endpoint}/{child_id}")
            return response.get('success', False)
        except Exception as e:
            print(f"Error al eliminar niño {child_id}: {e}")
            return False
    
    def find_all(self) -> List[Child]:
        """Obtiene todos los niños"""
        try:
            response = self.api_client.get(f"/{self.endpoint}")
            children_data = response.get('children', [])
            return [Child.from_dict(child_data) for child_data in children_data]
        except Exception as e:
            print(f"Error al obtener todos los niños: {e}")
            return []
    
    def find_by_name(self, name: str) -> List[Child]:
        """Busca niños por nombre"""
        try:
            response = self.api_client.get(f"/{self.endpoint}/search", {
                'name': name
            })
            children_data = response.get('children', [])
            return [Child.from_dict(child_data) for child_data in children_data]
        except Exception as e:
            print(f"Error al buscar niños por nombre {name}: {e}")
            return []
    
    def find_by_treatment(self, treatment_id: int) -> List[Child]:
        """Busca niños por tratamiento"""
        try:
            response = self.api_client.get(f"/{self.endpoint}/search", {
                'treatment_id': treatment_id
            })
            children_data = response.get('children', [])
            return [Child.from_dict(child_data) for child_data in children_data]
        except Exception as e:
            print(f"Error al buscar niños por tratamiento {treatment_id}: {e}")
            return []
    
    def update_sleep_average(self, child_id: int, new_average: float) -> bool:
        """Actualiza el promedio de sueño de un niño"""
        try:
            response = self.api_client.put(f"/{self.endpoint}/{child_id}/sleep_average", {
                'sleep_average': new_average
            })
            return response.get('success', False)
        except Exception as e:
            print(f"Error al actualizar promedio de sueño para niño {child_id}: {e}")
            return False


class TapDAO(ITapDAO):
    """Implementación concreta de TapDAO que se comunica con la API"""
    
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)
        self.endpoint = "taps"
    
    def create(self, tap: Tap) -> int:
        """Crea un nuevo registro de tap"""
        try:
            response = self.api_client.post(f"/{self.endpoint}", tap.to_dict())
            return response.get('id')
        except Exception as e:
            print(f"Error al crear tap: {e}")
            return -1
    
    def read(self, tap_id: int) -> Optional[Tap]:
        """Obtiene un tap por ID"""
        try:
            response = self.api_client.get(f"/{self.endpoint}/{tap_id}")
            return Tap.from_dict(response)
        except Exception as e:
            print(f"Error al leer tap {tap_id}: {e}")
            return None
    
    def update(self, tap: Tap) -> bool:
        """Actualiza un tap existente"""
        try:
            response = self.api_client.put(f"/{self.endpoint}/{tap.id}", tap.to_dict())
            return response.get('success', False)
        except Exception as e:
            print(f"Error al actualizar tap {tap.id}: {e}")
            return False
    
    def delete(self, tap_id: int) -> bool:
        """Elimina un tap"""
        try:
            response = self.api_client.delete(f"/{self.endpoint}/{tap_id}")
            return response.get('success', False)
        except Exception as e:
            print(f"Error al eliminar tap {tap_id}: {e}")
            return False
    
    def find_all(self) -> List[Tap]:
        """Obtiene todos los taps"""
        try:
            response = self.api_client.get(f"/{self.endpoint}")
            taps_data = response.get('taps', [])
            return [Tap.from_dict(tap_data) for tap_data in taps_data]
        except Exception as e:
            print(f"Error al obtener todos los taps: {e}")
            return []
    
    def find_by_child(self, child_id: int) -> List[Tap]:
        """Busca taps por niño"""
        try:
            response = self.api_client.get(f"/{self.endpoint}/search", {
                'child_id': child_id
            })
            taps_data = response.get('taps', [])
            return [Tap.from_dict(tap_data) for tap_data in taps_data]
        except Exception as e:
            print(f"Error al buscar taps por niño {child_id}: {e}")
            return []
    
    def find_by_user(self, user_id: int) -> List[Tap]:
        """Busca taps por usuario"""
        try:
            response = self.api_client.get(f"/{self.endpoint}/search", {
                'user_id': user_id
            })
            taps_data = response.get('taps', [])
            return [Tap.from_dict(tap_data) for tap_data in taps_data]
        except Exception as e:
            print(f"Error al buscar taps por usuario {user_id}: {e}")
            return []
    
    def find_by_status(self, status_id: int) -> List[Tap]:
        """Busca taps por estado"""
        try:
            response = self.api_client.get(f"/{self.endpoint}/search", {
                'status_id': status_id
            })
            taps_data = response.get('taps', [])
            return [Tap.from_dict(tap_data) for tap_data in taps_data]
        except Exception as e:
            print(f"Error al buscar taps por estado {status_id}: {e}")
            return []
    
    def find_by_date_range(self, start_date: str, end_date: str) -> List[Tap]:
        """Busca taps por rango de fechas"""
        try:
            response = self.api_client.get(f"/{self.endpoint}/search", {
                'start_date': start_date,
                'end_date': end_date
            })
            taps_data = response.get('taps', [])
            return [Tap.from_dict(tap_data) for tap_data in taps_data]
        except Exception as e:
            print(f"Error al buscar taps por rango de fechas: {e}")
            return []
    
    def close_tap(self, tap_id: int, end_time: str) -> bool:
        """Cierra un tap estableciendo la hora de finalización"""
        try:
            response = self.api_client.put(f"/{self.endpoint}/{tap_id}/close", {
                'end_time': end_time
            })
            return response.get('success', False)
        except Exception as e:
            print(f"Error al cerrar tap {tap_id}: {e}")
            return False
    
    def get_child_sleep_statistics(self, child_id: int) -> Dict[str, Any]:
        """Obtiene estadísticas de sueño para un niño"""
        try:
            response = self.api_client.get(f"/{self.endpoint}/statistics/{child_id}")
            return response
        except Exception as e:
            print(f"Error al obtener estadísticas para niño {child_id}: {e}")
            return {}


# =============================================
# FACHADA/SERVICIO PARA GESTIÓN COMPLETA
# =============================================

class SleepMonitoringService:
    """Fachada que coordina todas las operaciones del sistema"""
    
    def __init__(self, api_base_url: str, api_key: Optional[str] = None):
        self.api_client = APIClient(api_base_url, api_key)
        self.user_dao = UserDAO(self.api_client)
        self.child_dao = ChildDAO(self.api_client)
        self.tap_dao = TapDAO(self.api_client)
    
    def register_sleep_event(self, child_id: int, user_id: int, status_id: int) -> int:
        """Registra un nuevo evento de sueño/vigilia"""
        # Crear timestamp actual
        init_time = datetime.now().isoformat()
        
        # Crear tap
        tap = Tap(
            id=0,  # El servidor asignará el ID
            child_id=child_id,
            status_id=status_id,
            user_id=user_id,
            init=init_time
        )
        
        # Guardar en servidor
        tap_id = self.tap_dao.create(tap)
        
        if tap_id > 0:
            print(f"Evento registrado exitosamente. ID: {tap_id}")
        
        return tap_id
    
    def close_sleep_event(self, tap_id: int) -> bool:
        """Cierra un evento de sueño/vigilia"""
        end_time = datetime.now().isoformat()
        return self.tap_dao.close_tap(tap_id, end_time)
    
    def get_child_sleep_history(self, child_id: int) -> List[Tap]:
        """Obtiene el historial de sueño de un niño"""
        return self.tap_dao.find_by_child(child_id)
    
    def get_daily_summary(self, child_id: int, date: str) -> Dict[str, Any]:
        """Obtiene un resumen diario del sueño de un niño"""
        # Obtener taps del día
        taps = self.tap_dao.find_by_date_range(
            f"{date}T00:00:00",
            f"{date}T23:59:59"
        )
        
        # Calcular estadísticas
        sleep_taps = [t for t in taps if t.status_id == 1]  # status_id 1 = sleep
        awake_taps = [t for t in taps if t.status_id != 1]
        
        return {
            'total_sleep_events': len(sleep_taps),
            'total_awake_events': len(awake_taps),
            'taps': taps
        }
    
    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """Autentica un usuario"""
        return self.user_dao.authenticate(username, password)


# =============================================
# EJEMPLO DE USO
# =============================================

def main():
    # Configurar conexión al servidor
    API_BASE_URL = "https://api.sueño-infantil.com/v1"
    API_KEY = "tu-api-key-aqui"
    
    # Crear servicio
    service = SleepMonitoringService(API_BASE_URL, API_KEY)
    
    # Ejemplo: Autenticar usuario
    user = service.authenticate_user("mare", "12345")
    if user:
        print(f"Usuario autenticado: {user.username}")
        
        # Ejemplo: Registrar evento de sueño
        tap_id = service.register_sleep_event(
            child_id=1,
            user_id=user.id,
            status_id=1  # sleep
        )
        
        # Ejemplo: Obtener historial
        history = service.get_child_sleep_history(child_id=1)
        print(f"Historial de eventos: {len(history)} registros")
        
        # Ejemplo: Obtener resumen diario
        today = datetime.now().strftime("%Y-%m-%d")
        summary = service.get_daily_summary(child_id=1, date=today)
        print(f"Resumen del día: {summary['total_sleep_events']} eventos de sueño")


# =============================================
# CLASE PARA MANEJO DE ERRORES
# =============================================

class APIException(Exception):
    """Excepción personalizada para errores de API"""
    
    def __init__(self, message: str, status_code: Optional[int] = None, response_data: Optional[Dict] = None):
        self.message = message
        self.status_code = status_code
        self.response_data = response_data
        super().__init__(self.message)
    
    def __str__(self):
        base_msg = f"API Error: {self.message}"
        if self.status_code:
            base_msg += f" (Status: {self.status_code})"
        return base_msg


# =============================================
# CONFIGURACIÓN Y UTILIDADES
# =============================================

class Config:
    """Clase de configuración para la aplicación"""
    
    def __init__(self):
        self.api_base_url = "https://api.sueño-infantil.com/v1"
        self.api_key = None
        self.timeout = 30
        self.retry_attempts = 3
        self.debug = False
    
    @classmethod
    def from_env_file(cls, env_file: str = ".env") -> 'Config':
        """Carga configuración desde archivo .env"""
        config = cls()
        try:
            with open(env_file, 'r') as f:
                for line in f:
                    if '=' in line and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        if key == "API_BASE_URL":
                            config.api_base_url = value
                        elif key == "API_KEY":
                            config.api_key = value
                        elif key == "API_TIMEOUT":
                            config.timeout = int(value)
        except FileNotFoundError:
            print(f"Archivo {env_file} no encontrado, usando configuración por defecto")
        
        return config


if __name__ == "__main__":
    main()