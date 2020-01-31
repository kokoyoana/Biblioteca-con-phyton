class Libro:
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
            


        

#libro1= Libro() 
#libro1.menu()