from Biblioteca  import Libro

class Menu:
    def __init__(self):
        self.libro1= Libro()
    
    def bienvenida(self):
        print("_____________________________Leer--- ((((̲̅̅●̲̲̅̅̅̅=̲̲̅̅̅̅●̲̅̅))))--Está de Moda!__________________________________")
        print("_____________________________________________________________________________________________")
        print("********************---Bienvenido/a a la Biblioteca Virtual---*******************************")
        print("✿◕‿◕✿  ❀◕‿◕❀    ❁◕‿◕❁    ✾◕‿◕✾ ✿◕‿◕✿  ❀◕‿◕❀   ❁◕‿◕❁  ✾◕‿◕✾  ✾◕‿◕✾ ❀◕‿◕❀   ❁◕‿◕❁  ✾◕‿◕✾  ✾◕‿◕✾ ")
        print("______________________________________________________________________________________________")
        print()
        print("Seleccione una opcion: ")
        print("1. Añadir un libro")
        print("2. Consultar Biblioteca")
        print("0. Salir")
        print()
    
    def menu(self):
        while True:
            self.bienvenida()
            entrada_usuario = int(input("Seleccione una opcion: "))
                
            if entrada_usuario == 1:
                self.libro1.escribir()
    
                
            elif entrada_usuario == 2:
                print("hello")
                self.libro1.leer()

            elif entrada_usuario == 0:
                print("✿◕‿◕✿  ❀◕‿◕❀---Hasta luego! Vuelva pronto---✿◕‿◕✿  ❀◕‿◕❀")
                break
            else:
                print('Error, solo de aceptan numeros del 0 al 2')
menu1=Menu()
menu1.menu()
