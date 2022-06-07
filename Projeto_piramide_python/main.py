import mysql.connector
from UsuarioMestre import UsuarioMestre
from Usuario import Usuario
from gui import Janela  

def main():

    database = mysql.connector.connect(
        host="localhost",
        user= "root",
        password = "756939845",
        database = "piramide"        

    ) 

  
    #window = Janela(database) 



    #mestre = UsuarioMestre('mestre1','12345',database)
    #for i in mestre.VisualizaUsuarios():
     #   print(i)

    usuario = Usuario('henrique','12345',database)
    
    
    #usuario.InserirUsuario("usuario3","123456")

   # usuario.SelectUsuarios()
    
    #usuario.SelectUsuarios("mestre1",database)
    #mestre.InserirUsuario("usuario2","123456","mestre1",database)
    #mestre.DeletaUsuario("usuario1",database) 
  

if __name__ == "__main__":
    main()