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
           del x
        else:
            print('no esta')
            
    def buscar(self):
       archivo=str(open("archivo.txt","r").readlines()) 
       b=input('que titulo buscas')
       archivo.index(b)
       print('lo encontro')
       
  
         

libro1= libro() 
libro1.titulo=(input('escriba un libro ').casefold())     
libro1.autor=input('escriba el autor '.casefold())
libro1.escribir()
libro1.leer()
libro1.sobre()
libro1.buscar()


