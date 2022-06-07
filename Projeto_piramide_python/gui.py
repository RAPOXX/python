from cProfile import label
from re import I
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pymysql import NULL

from setuptools import Command

from UsuarioMestre import UsuarioMestre
#from tkinter import messagebox


class Janela:

    def __init__(self,database):
        self.database = database
        self.interface()
    def interface(self):   
        self.janela = Tk()
        self.janela.title("Login")
        self.janela.geometry("200x200")
        self.janela.resizable(width=0,height=0)
        

        label1 = ttk.Label(self.janela,text="USUARIO: ").grid(column=1,row=2)

        self.entrada_usuario = ttk.Entry(self.janela,)
        self.entrada_usuario.grid(column=2,row=2,padx=10,pady=10)

        label1 = ttk.Label(self.janela,text="SENHA: ").grid(column=1,row=3)
        self.entrada_senha = ttk.Entry(self.janela,show="*")
        self.entrada_senha.grid(column=2,row=3)

        btn = ttk.Button(self.janela,text="Login",command=self.nova_janela)
        btn.grid(column=2,row=4,padx=10,pady=10)

        self.janela.mainloop()
   
    def hello():
        print("hello")

    def DeletaUsuario(self,nomeusuario,mestre):
        usuario = str(nomeusuario.get())
        mestre.DeletaUsuario(usuario)
        messagebox.showinfo("USUARIO DELETADO",f"USUARIO {usuario} DELETADO COM SUCESSO")
    
    def AdicionaUsuario(self,nomeusuario,senhausuario,mestre):
        usuario = str(nomeusuario.get())
        senha = str(senhausuario.get())
        mestre.InserirUsuario(usuario,senha)
        messagebox.showinfo("CADASTRO EFETUADO",f"USUARIO {usuario} CADASTRADO COM SUCESSO ")
    
    def VisualizarUsuarios(self,mestre,treeview):
        treeview.insert("","end",values=['','','',''])
        for user in mestre.VisualizaUsuarios():
                treeview.insert("","end",values=user)
    
    def JanelaCadastrar(self,mestre):
        janela = Tk()
        janela.title("CADASTRAR USUARIO")
        janela.geometry("500x500")
        janela.resizable(width=0,height=0)

        label1 = Label(janela,text="Usuario: ")
        label1.grid(column=0,row=1)

        nomeusuario = Entry(janela)
        nomeusuario.grid(column=1,row=1)

        label2 = Label(janela,text="Senha: ")
        label2.grid(column=0,row=2)

        senhausuario =  Entry(janela,show="*")
        senhausuario.grid(column=1,row=2)

    
        button = Button(janela,text="Cadastrar",command=lambda: self.AdicionaUsuario(nomeusuario,senhausuario,mestre))     
        button.grid(column=1,row=3)

        janela.mainloop()

    def JanelaDeletar(self,mestre):
        janela = Tk()
        janela.geometry("500x500")
        janela.title("DELETAR USUARIO")

        label1 = Label(janela,text="USUARIO")
        label1.grid(column=0,row=1)

        nomeusuario = Entry(janela)
        nomeusuario.grid(column=1,row=1)

        button = Button(janela,text="DELETAR",command=lambda: self.DeletaUsuario(nomeusuario,mestre))
        button.grid(column=0,row=2)
        janela.mainloop()

    def JanelaVisualizar(self,mestre):

        janela = Tk()
        janela.title("VISULIZAR USUARIOS")
        janela.geometry("500x500")

        button = Button(janela,text='ATUALIZAR',command=lambda: self.VisualizarUsuarios(mestre,tv))
        button.pack(anchor=CENTER)
    
     
        tv = ttk.Treeview(janela,columns=['Id','Nome','Senha','Dependencia'],show='headings')
        tv.column('Id',minwidth=0,width=50)
        tv.column('Nome',minwidth=0,width=250)
        tv.column('Senha',minwidth=0,width=100)
        tv.column('Dependencia',minwidth=0,width=100)
        tv.heading('Id',text='Id')
        tv.heading('Nome',text='Nome')
        tv.heading('Senha',text='Senha')
        tv.heading('Dependencia',text='Dependencia')
        tv.pack()

        janela.mainloop()

    def VisualizarDependentes(self,mestre,treeview,nomeusuario):
        usuario = str(nomeusuario.get())
        for user in mestre.VisualizarDependentes(usuario):
            treeview.insert("","end",values=user)

    def JanelaDependentes(self,mestre):

        janela = Tk()
        janela.title("VISULIZAR DEPENDENTES")
        janela.geometry("500x500")

        usuario = Entry(janela)
        usuario.pack(anchor=CENTER)

        button = Button(janela,text="PROCURAR",command=lambda: self.VisualizarDependentes(mestre,tv,usuario))
        button.pack(anchor=CENTER)
     
        tv = ttk.Treeview(janela,columns=['Id','Nome','Senha','Dependencia'],show='headings')
        tv.column('Id',minwidth=0,width=50)
        tv.column('Nome',minwidth=0,width=250)
        tv.column('Senha',minwidth=0,width=100)
        tv.column('Dependencia',minwidth=0,width=100)
        tv.heading('Id',text='Id')
        tv.heading('Nome',text='Nome')
        tv.heading('Senha',text='Senha')
        tv.heading('Dependencia',text='Dependencia')
        tv.pack()


        janela.mainloop()


    def nova_janela(self):
        user = str(self.entrada_usuario.get())
        password = str(self.entrada_senha.get())
        mestre = UsuarioMestre(user,password,self.database)

        if mestre.logado:
            self.janela.destroy()
            janela2 = Tk()
            janela2.title("AREA DO USUARIO MESTRE")
            janela2.state("zoomed")

            barrademenu = Menu(janela2)
            menucontatos = Menu(barrademenu)
            menucontatos.add_command(label="CADASTRAR",command= lambda: self.JanelaCadastrar(mestre))
            menucontatos.add_command(label="DELETAR",command=lambda: self.JanelaDeletar(mestre))
            menucontatos.add_command(label="VISUALIZAR",command=lambda: self.JanelaVisualizar(mestre))
            menucontatos.add_command(label="VISUALIZAR DEPENDENTES",command=lambda: self.JanelaDependentes(mestre))
            barrademenu.add_cascade(label="OPÇOES",menu=menucontatos)


            janela2.config(menu=barrademenu)
            janela2.mainloop()

    def MensagemErro():
            messagebox.showinfo("ERRO","DADOS VAZIOS")



