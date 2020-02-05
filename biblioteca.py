class Libro:
    titulo=''
    autor=''
    
    def escribir(self):
        self.titulo=(input('Escriba un libro ').casefold())  
        if self.existe():
                print("El Libro ya está en la Biblioteca")
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
        
 
    def eliminar(self):
        archivo = open("archivo.txt", "r")
        lineas = archivo.readlines()#lineas en un array / 
        i =0
        while i<len(lineas):
            print(i , lineas[i])
            i= i+1
        indice = int(input("Indicar indice que desea borrar"))

        del lineas [indice]
        archivo = open("archivo.txt", "w")
        for valor in lineas:
            archivo.write(valor)
    

