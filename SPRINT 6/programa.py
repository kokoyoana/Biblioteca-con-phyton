class libro:
    titulo=''
    autor=''

    def escribir(self):
          
        archivo= open("archivo.txt","a+")
        archivo.write("Titulo: "+libro1.titulo + " " +"Autor: "+libro1.autor + "\n")
        
    def leer(self):
        archivo=open("archivo.txt","r")
        print(archivo.read())
   
libro1= libro() 
libro1.titulo=(input('escriba un libro '))     
libro1.autor=input('escriba el autor ')
libro1.escribir()
libro1.leer()


