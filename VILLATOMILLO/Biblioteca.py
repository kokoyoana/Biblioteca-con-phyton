class Libro:
    titulo=''
    autor=''

    def escribir(self):
        archivo = open("archivo.txt", "w+")
        self.titulo = input('Escriba un libro ')
        linea = " "
        existe = False
        while(linea):
            linea = archivo.readline()
            L = linea.split()
            if self.titulo in L:
                print("El Libro ya está en la biblioteca.")
                existe = True
        if existe == False:
            self.autor = (input('Escriba el autor '))
            archivo = open("archivo.txt","a+")
            archivo.write(self.titulo + "; " + "autor: " + self.autor + "\n")
        archivo.close()
            
    def consultar(self):
        archivo = open("archivo.txt","r")
        print(archivo.read())

    def buscar(self):
        archivo = open("archivo.txt", "r")
        palabra = input("¿Qué libro deseas? ")
        linea = " "
        count = 1
        existe = False
        while(linea):
            linea = archivo.readline()
            L = linea.split("; ")
            if palabra in L:
                print("Se encuentra en ", count, ":", linea)
                count += 1
                existe = True
        if existe == False:
            print("No existe")
        archivo.close()

    def eliminar(self):
        archivo = open("archivo.txt", "r")
        lineas = archivo.readlines()#lineas en un array / 
        i = 0
        while i<len(lineas):
            print(i , lineas[i])
            i = i+1
        indice = int(input("Indicar indice que desea borrar"))

        del lineas [indice]
        archivo = open("archivo.txt", "w")
        for valor in lineas:
            archivo.write(valor)
