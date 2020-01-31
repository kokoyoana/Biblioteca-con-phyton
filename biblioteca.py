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
        a=input('escriba un titulo ')
       
        archivo=str(open("archivo.txt").readlines())
        a.count(archivo)
  
        if(archivo.find(a)):
           print('repetido')
        elif(self.titulo.archivo):
            print('no esta')  

         
         
         

libro1= libro() 
libro1.titulo=(input('escriba un libro ').casefold())     
libro1.autor=input('escriba el autor '.casefold())
libro1.escribir()
libro1.leer()
libro1.sobre()


