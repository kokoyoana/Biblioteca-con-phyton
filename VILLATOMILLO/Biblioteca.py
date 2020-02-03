class Libro:
    titulo=''
    autor=''
    
    def escribir(self):
        self.titulo=(input('escriba un libro ').casefold())  
        if self.existe():
                print("El Libro Ya esta en la Biblioteca")
        else:
                self.autor=(input('escriba el autor ').casefold())  
                archivo= open("archivo.txt","a+")
                archivo.write("Titulo: "+self.titulo + " " +"Autor: "+ self.autor + "\n")
            
    def leer(self):
        print("hola")
        archivo=open("archivo.txt","r")
        print(archivo.read())


    def existe(self):
        archivo=str(open("archivo.txt","r").readlines())
        self.titulo
        if self.titulo in archivo:
            return True
        else:
            return False


        

#libro1= Libro() 
#libro1.menu()