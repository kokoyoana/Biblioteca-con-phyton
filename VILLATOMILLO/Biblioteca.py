class Libro:
    titulo=''
    autor=''
    
    def escribir(self):
        self.titulo = (input('Escriba un libro ').casefold())  
        if self.newexiste():
                print("El libro ya está en la Biblioteca")
        else:
                self.autor = (input('Escriba el autor ').casefold())  
                archivo = open("archivo.txt","a+")
                archivo.write("Titulo: " + self.titulo + " " + "Autor: " + self.autor + "\n")
            
    def leer(self):
        archivo = open("archivo.txt","r")
        print(archivo.read())


    def existe(self):
        archivo = str(open("archivo.txt","r").readlines())
        self.titulo
        if self.titulo in archivo:
            return True
        else:
            return False
    
    def buscar(self):
        archivo = str(open("archivo.txt","r").readlines()) 
        b = input('¿Qué título buscas? ')
        x = archivo.find(b)
        if x > 0:
            print('El libro "' + b + '" ESTÁ en la Biblioteca.')
        else:
            print('El libro "' + b + '" NO EXISTE en la Biblioteca.')
            
    def newexist(self):
        archivo = open ("archivo.txt", "r") 
        palabra = input("Que Libro deseas? ")
        linea = " "
        count = 1
        existe= False
        while (linea):
            linea = archivo.readline()
            L = linea.split()
            if palabra in L:
                print("Se Encuentra en ", count, ":", linea)
                count += 1
                existe=True
        if existe==False:
            print("No existe")
        archivo.close()
                

        
