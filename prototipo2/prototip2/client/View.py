class ViewConsole:

    def viewShowmenu(self):
        print("1: Login")
        print("2: Quit")
        while(True):
            option=input("Enter Option: ")
            if(option.isdigit()):
                optionInt=int(option)
                if (option >= 1 and option <= 2):
                    return optionInt
               
            print("ERROR: Introduce un valor correcto")

    def viewGeneral(self):
        option=-1
        while(option!=2):
            option=self.viewShowmenu()
            match option:
                case 1:
                    self.viewLogin()
                    #login
                case 2:
                    #Quit
                    print("Saliendo de la aplicación...")

    def viewLogin(self):
        print("View LOGIN")
        print("Introduce el username/email i el password")
        username=input("Username o email: ")
        passwd=input("Password: ")
        # DaoUserClient ha de fer login
        # Depenent de la resposta va a ser child o User not Autheticated