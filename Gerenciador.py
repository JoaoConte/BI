from Modulos import *
from Relatorios import Relatorios
from Funcoes import Funcs
from Cards import Cards_M
from Screen_frame import *

caminho =  os.path.abspath(os.path.dirname('.')) # Pega diretorio atual
# Carrega informações do Conexão.dat

principal = tix.Tk()

class Application(Funcs, Relatorios, Cards_M, Screen):
    def __init__(self):
        self.principal = principal
        self.le_conexao(caminho)
        self.tela()
        self.widgets()
        self.frame_p()
        self.cria()
        principal.mainloop()

    def seleciona_revenda(self):
        empresa = []
        revenda = []
        for i in self.listbox.curselection():
            empresa.append(str(self.listbox.get(i)[0]))
            revenda.append(str(self.listbox.get(i)[2]))
        self.empresa = ', '.join(empresa)
        self.revenda = ', '.join(revenda)

    def widgets(self):
        # Datas
        # Calendario Inicial
        self.btn_calendar_ini = Button(self.principal, text='Data Inicial', command=self.calendario_ini)
        self.btn_calendar_ini.place(relx=0.6, rely=0.02)
        self.ent_data_ini = Entry(self.principal, width=10)
        self.ent_data_ini.place(relx=0.6, rely=0.10)

        # Calendario Final
        self.btn_calendar_fim = Button(self.principal, text='Data Final', command=self.calendario_fim)
        self.btn_calendar_fim.place(relx=0.7, rely=0.02)
        self.ent_data_fim = Entry(self.principal, width=10)
        self.ent_data_fim.place(relx=0.7, rely=0.10)

        # Selecão de revendas

        self.conecta_DB()
        self.cursor.execute("SELECT empresa, revenda,razao_social FROM GER_REVENDA")
        self.listbox = Listbox(principal, width=50, height=3, selectmode=MULTIPLE)
        self.listbox.place(relx=0.01, rely=0.01)
        a = 0
        for linha in self.cursor.fetchall():
            a = a + 1
            combo = str(linha[0]) + '.' + str(linha[1]) + ' - ' + linha[2]
            self.listbox.insert(a, combo)
        btn = Button(principal, text='Seleção de revendas', font=('verdana',8,'bold'), command=self.seleciona_revenda)
        btn.place(relx=0.4, rely=0.09)
        self.desconecta_DB()

        #iNICIA OS CARDS
        self.btn_executar = Button(self.principal, text='Executar', font=('verdana',8,'bold'), command=self.card_vendas)                      # Criação dos botões
        self.btn_executar.place(relx=0.8,rely=0.09)     # Posição relativa dos botões


####################################################################################

        # # Botões
        # self.btn_limpar = Button(self.principal, text='Limpar', font=('verdana',8,'bold'), command=self.limpa_tela)                      # Criação dos botões
        # self.btn_limpar.place(relx=0.2,rely=0.65)     # Posição relativa dos botões
        # #
        # self.btn_imprimir = Button(self.principal, text='Imprimir', font=('verdana',8,'bold'), command=self.geraRelClient)
        # self.btn_imprimir.place(relx=0.4, rely=0.65)
        # # Campos
        # self.lbl_nome = Label(self.principal, text='Nome', font=('verdana',8,'bold'))
        # self.lbl_nome.place(relx=0.15, rely=0.25)
        # self.ent_nome = Entry(self.principal)
        # self.ent_nome.place(relx=0.15, rely=0.30, relwidth=0.65)
        # #
        # self.lbl_email = Label(self.principal, text='E-mail', font=('verdana',8,'bold'))
        # self.lbl_email.place(relx=0.15, rely=0.35)
        # self.ent_email = Entry(self.principal)
        # self.ent_email.place(relx=0.15, rely=0.40, relwidth=0.65)
        # #
        # self.lbl_valor = Label(self.principal, text='Valor', font=('verdana',8,'bold'))
        # self.lbl_valor.place(relx=0.15, rely=0.45)
        # self.ent_valor = Entry(self.principal)
        # self.ent_valor.place(relx=0.15, rely=0.50, relwidth=0.10)
        # #
        # self.lbl_data1 = Label(self.principal, text='Data', font=('verdana',8,'bold'))
        # self.lbl_data1.place(relx=0.40, rely=0.45)
        # self.ent_data1 = Entry(self.principal)
        # self.ent_data1.place(relx=0.40, rely=0.50, relwidth=0.03)
        # #
        # self.lbl_data2 = Label(self.principal, text='/', font=('verdana', 8, 'bold'))
        # self.lbl_data2.place(relx=0.43, rely=0.50)
        # self.ent_data2 = Entry(self.principal)
        # self.ent_data2.place(relx=0.45, rely=0.50, relwidth=0.03)
        # #
        # self.lbl_data3 = Label(self.principal, text='/', font=('verdana', 8, 'bold'))
        # self.lbl_data3.place(relx=0.48, rely=0.50,)
        # self.ent_data3 = Entry(self.principal,)
        # self.ent_data3.place(relx=0.50, rely=0.50, relwidth=0.05)
        # #
        # self.lbl_horas = Label(self.principal, text='Horário', font=('verdana',8,'bold'))
        # self.lbl_horas.place(relx=0.70, rely=0.45)
        # self.ent_horas = Entry(self.principal)
        # self.ent_horas.place(relx=0.70, rely=0.50, relwidth=0.10)

Application()