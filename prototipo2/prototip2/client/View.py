from User import *
from DaoClient import *

class ViewConsole:

    def __init__(self):
        self.daoClient = DaoUserClient()  # FIX: faltaba instanciar daoClient

    def viewShowmenu(self):
        print("1: Login")
        print("2: Quit")
        while True:
            option = input("Enter Option: ")
            if option.isdigit():
                optionInt = int(option)
                if optionInt >= 1 and optionInt <= 2:  # FIX: comparar optionInt (int), no option (str)
                    return optionInt
            print("ERROR: Introduce un valor correcto")

    def viewGeneral(self):
        option = -1
        while option != 2:
            option = self.viewShowmenu()
            match option:
                case 1:
                    self.viewLogin()
                case 2:
                    print("Saliendo de la aplicación...")

    def viewLogin(self):
        print("View LOGIN")
        print("Introduce el username/email i el password")
        username = input("Username o email: ")
        passwd = input("Password: ")
        user = User("", username, passwd, "", "", "")
        resposta_user = self.daoClient.login(user)
        if resposta_user:
            self.viewUser(resposta_user)
        else:
            self.viewUserNotAutenticated()

    def viewUser(self, user):
        print("View user autenticated")
        print(user)

    def viewUserNotAutenticated(self):
        print("View User")
        print("User NOT Authenticated")


viewConsole = ViewConsole()  # FIX: nombre en minúscula para no sobreescribir la clase
viewConsole.viewGeneral()