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

Application()