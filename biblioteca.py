class libro:
    titulo=''
    autor=''

    def escribir(self):
          
        archivo= open("archivo.txt","a+")
        archivo.write("Titulo: "+libro1.titulo + " " +"Autor: "+libro1.autor + "\n")
     
        
    def leer(self):
        archivo=open("archivo.txt","r")
     
        print(archivo.read())
        
        
   
    
        
            
    def buscar(self):
       archivo=str(open("archivo.txt","r").readlines()) 
       b=input('que titulo buscas')
       archivo.index(b)
       print('lo encontro')
       
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
         

libro1= libro() 
libro1.titulo=(input('escriba un libro ').casefold())     
libro1.autor=input('escriba el autor '.casefold())
libro1.escribir()
libro1.leer()
libro1.buscar()
libro1.newexist()

