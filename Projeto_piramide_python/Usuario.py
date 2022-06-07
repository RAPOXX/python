

from tkinter import messagebox


class Usuario:

    def __init__(self,nomeusuario,senhausuario,database):
        self.nomeusuario = nomeusuario
        self.senhausuario = senhausuario
        self.database  = database
        self.AutenticaUsuario(nomeusuario,senhausuario)    

    def SelectUsuarios(self):
        cursor = self.database.cursor()
        cursor.execute(f"select * from usuario where usuario.dependencia = '{self.nomeusuario}'")
        result = cursor.fetchall()
        for i in result:
            print(i)

    def InserirUsuario(self,nomeusuario,senhausuario):
        cursor = self.database.cursor()
        cursor.execute(f"insert into usuario(Nomeusuario,SenhaUsuario,Dependencia) values('{nomeusuario}','{senhausuario}','{self.nomeusuario}')")
        self.database.commit()
        print("usuario adicionado com sucesso")

    def DeletarUsuario(self,nomeusuario):
        cursor = self.databse.cursor()
        cursor.execute(f"delete from usuario where usuario.Nomeusuario = '{nomeusuario}'")
        self.database.commit()
        print(f"usuario {nomeusuario} deletado com sucesso")

    def AutenticaUsuario(self,nomeusuario,senhausuario):

        try:
            cursor = self.database.cursor()
            cursor.execute(f"select usuario.Nomeusuario from usuario where usuario.Nomeusuario = '{nomeusuario}'")
            result = cursor.fetchall()
            result2 = result[0]
            result3 = result2[0]

            if nomeusuario == result3:
                cursor = self.database.cursor()
                cursor.execute(f"select usuario.SenhaUsuario from usuario where usuario.Nomeusuario = '{nomeusuario}'")
                result = cursor.fetchall()
                result2 = result[0]
                result3 = result2[0]
                if senhausuario == result3:
                    print("logado com sucesso")
                else:
                    print("dados incorretos")
                    messagebox.showinfo("erro","DADOS INCORRETOS")
            else:
                messagebox.showinfo("erro","DADOS INCORRETOS")
        except:
                messagebox.showinfo("erro","DADOS INCORRETOS")
            
