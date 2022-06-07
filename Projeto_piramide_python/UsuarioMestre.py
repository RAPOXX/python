from tkinter import messagebox

class UsuarioMestre():

    def __init__(self,nomemestre,senhamestre,database):
        self.nomemestre = nomemestre
        self.senhamestre = senhamestre
        self.database = database
        self.logado = False
        self.AutenticaUsuarioMestre(self.nomemestre,self.senhamestre)
            

    def InserirUsuario(self,nomeusuario,senhausuario):
        cursor = self.database.cursor()
        cursor.execute(f"INSERT INTO usuario(Nomeusuario,SenhaUsuario,Dependencia) VALUES('{nomeusuario}','{senhausuario}','{self.nomemestre}')")
        self.database.commit()
        print(f"Usuario {nomeusuario} Cadastrado com sucesso")

        
    def DeletaUsuario(self,nomeusuario):
        cursor = self.database.cursor()
        cursor.execute(f"delete from usuario where usuario.Nomeusuario = '{nomeusuario}'")
        self.database.commit()
        print(f"Usuario {nomeusuario} deletado com sucesso")

    def VisualizaUsuarios(self):
        cursor = self.database.cursor()
        cursor.execute("select * from usuario")
        result = cursor.fetchall()
        return result

    def VisualizarDependentes(self,nomeusuario):
        cursor = self.database.cursor()
        cursor.execute(f"select * from usuario where usuario.Dependencia = '{nomeusuario}'")
        result = cursor.fetchall()
        return result
    
    def AutenticaUsuarioMestre(self,nomemestre,senhamestre):
        try:
            if nomemestre !=  '' or senhamestre != '':
                cursor = self.database.cursor()
                cursor.execute(f"select usuariomestre.NomeUsuarioMestre from usuariomestre where usuariomestre.NomeUsuarioMestre = '{nomemestre}'")
                result = cursor.fetchall()
                result2 = result[0]
                result3 = result2[0]
                if nomemestre == result3:
                    cursor = self.database.cursor()
                    cursor.execute(f"select usuariomestre.SenhaUsuarioMestre from usuariomestre where usuariomestre.NomeUsuarioMestre = '{nomemestre}'")
                    result = cursor.fetchall()
                    result2 = result[0]
                    result3 = result2[0]
                    if senhamestre == result3:
                        print("logado com sucesso")
                        self.logado = True

            
                    else:
                        print("dados incorretos")
                        messagebox.showinfo("ERRO","DADOS INCORRETOS")

                else:
                    print("dados incorretos")
                    messagebox.showinfo("ERRO","DADOS INCORRETOS")
            else:
                print("digite os dados nos campos indicados")
                messagebox.showinfo("ERRO","CAMPOS VAZIOS")
        except:
            print("dados incorretos")
            messagebox.showinfo("ERRO","DADOS INCORRETOS")
            