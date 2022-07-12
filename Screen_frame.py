from Modulos import *

class Screen():
    def tela(self):
        self.principal.title('Gerencial de vendas')  # Titulo da janela
        self.principal.geometry('840x400')  # Tamanho inicial da tela
        self.principal.resizable(False, False)  # Redimencionamento (default = True)

    def tela_cards(self):
        self.telacards = Toplevel()
        self.telacards.title('Geral de vendas')
        self.telacards.geometry('600x400')
        self.telacards.resizable(False, False)
        self.telacards.transient(self.principal)
        self.telacards.focus_force()
        self.telacards.grab_set()
        self.card_vendas()

    def frame_p(self):
        self.frame_principal = Frame(self.principal, bg='blue')  # Criação dos frames
        self.frame_principal.place(relx=0.02, rely=0.11)  # Posição relativa do Frame