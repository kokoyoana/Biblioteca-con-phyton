class libro:
    titulo=''
    autor=''
    
    def escribir(self):
            self.titulo=(input('escriba un libro '))
            self.autor=(input('escriba el autor '))
            archivo= open("archivo.txt","a+")
            archivo.write("Titulo: "+self.titulo + " " +"Autor: "+ self.autor + "\n")
            
    def leer(self):
        print("hola")
        archivo=open("archivo.txt","r")
        print(archivo.read())
            
            
    def bienvenida(self):
        print("______________________________________________________")
        print("*******Bievenido/a a la Biblioteca Virtual************")
        print("______________________________________________________")
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
                self.escribir()

            elif entrada_usuario == 2:
                print("hello")
                self.leer()

            elif entrada_usuario == 0:
                print("Hasta luego! Vuelva pronto")
                break
            else:
                print('Error, solo de aceptan numeros del 0 al 2')

        

libro1= libro() 
libro1.menu()