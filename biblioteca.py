class libro:
    titulo=''
    autor=''

    def escribir(self):
          
        archivo= open("archivo.txt","a+")
        archivo.write("Titulo: "+libro1.titulo + " " +"Autor: "+libro1.autor + "\n")
     
        
    def leer(self):
        archivo=open("archivo.txt","r")
     
        print(archivo.read())
        
        
   
    def sobre(self):
        archivo=str(open("archivo.txt","r").readlines())
        x=input('escribe')
        if x in archivo:
            print('esta')
        else:
            print('no esta')
         
         

libro1= libro() 
libro1.titulo=(input('escriba un libro ').casefold())     
libro1.autor=input('escriba el autor '.casefold())
libro1.escribir()
libro1.leer()
libro1.sobre()


