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
        archivo= open('archivo.txt').readlines()
  
        if a!=archivo :
           print('esta repetido')
        else:
           print('libro guardado')
         

libro1= libro() 
libro1.titulo=(input('escriba un libro '))     
libro1.autor=input('escriba el autor ')
libro1.escribir()
libro1.leer()
libro1.sobre()

