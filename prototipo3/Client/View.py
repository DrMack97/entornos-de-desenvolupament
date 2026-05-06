from User import *
from DaoUserClient import *

class ViewConsole:

    daoClient=DaoUserClient()
    token=""
   
    def viewShowMenu(self):
        print("1: Login")
        print("2: Login Token")
        print("3: Child")
        print("4: Quit")
        while(True):
            option=input("Enter Option: ")
            if option.isdigit():  # Corregido: añadir paréntesis
                optionInt=int(option)
                if optionInt > 0 and optionInt < 5:  # Cambiado a 5 para incluir opción 4
                    return optionInt
            print("Error: Introdueix una opció correcta")

    def viewGeneral(self):
        option=-1
        while(option!=4):  # Cambiado de 2 a 4 para salir correctamente
            option=self.viewShowMenu()
            match option:
                case 1:
                    self.viewLogin()
                case 2:
                    self.viewLoginToken(self.token)
                case 3:
                    self.viewChilds()  # Llamada al método
                case 4:
                    print("Adeu, Gràcies per utilitzar l'aplicació")

    def viewLoginToken(self, token):
        print("View LOGIN TOKEN")
        resposta_user=self.daoClient.loginToken(token)
        if(resposta_user):
            self.viewUser(resposta_user)
            self.token=resposta_user.token
        else:
            self.viewUserNotAutenticated()

    def viewLogin(self):
        print("View LOGIN")
        print("Introdueix el Username o email i el password")
        username=input("Username o email: ")
        passwd=input("Password: ")
        user=User("", username, passwd, "", "", "")
        resposta_user=self.daoClient.login(user)
        if(resposta_user):
            self.viewUser(resposta_user)
            self.token=resposta_user.token
        else:
            self.viewUserNotAutenticated()
    
    def viewUser(self,user):
        print("View User Authenticated")
        print(user)
    
    def viewUserNotAutenticated(self):
        print("View User")
        print("User NOT Authenticated")

    # NUEVO MÉTODO: Añadir este método
    def viewChilds(self):
        """Método para obtener y mostrar los hijos del usuario"""
        if not self.token:
            print("No estás autenticado. Por favor, haz login primero.")
            return
        
        print("Obteniendo lista de hijos...")
        childs = self.daoClient.getChilds(self.token)
        
        if childs:
            print("Hijos del usuario:")
            for child in childs:
                print(f"ID: {child['id']}, Name: {child['name']}")
    
    #Metodo taps
    def viewTaps(self):
        """Muestra los taps de un child"""
        if not self.token:
            print("No estás autenticado. Por favor, haz login primero.")
            return
    
    print("\n=== VER TAPS ===")
    id_child = input("ID del child: ")
    
    taps = self.daoClient.getChildTaps(self.token, id_child)
    
    if taps:
        print(f"\nTaps encontrados: {len(taps)}")
        for tap in taps:
            print(f"  ID: {tap.get('id')}, Fecha: {tap.get('date')}, Estado: {tap.get('status_id', 'N/A')}")
    else:
        print("No se encontraron taps o hubo un error")





        


        



