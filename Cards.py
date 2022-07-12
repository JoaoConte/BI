import tkinter
from Modulos import *

class Cards_M():
    def card_vendas(self):
        if self.empresa == '':
            tkinter.messagebox.showinfo(title='Seleção Empresa', message='Selecione a(s) Empresa(s) e confirme a seleção')
            return
        if self.data_inicial =='':
            tkinter.messagebox.showinfo(title='Data Inicial', message='Selecione a Data Inicial e depois Execute')
            return
        if self.data_final =='':
            tkinter.messagebox.showinfo(title='Data Final', message='Selecione a Data Final e depois Execute')
            return
        btnstat_ve = tkinter.NORMAL
        self.conecta_DB()
        if self.bancodados != 'SQLSERVER':
            self.cursor.execute("SELECT SUM(fmc.TOT_NOTA_FISCAL) FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO WHERE FMC.STATUS = 'F' AND fmc.MODALIDADE IN ('A','G','O','V','I','T','M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN ("+ self.revenda + ") AND fmc.TIPO_TRANSACAO = 'V21' AND fmc.DTA_DOCUMENTO BETWEEN TO_DATE('"+ self.data_inicial +"', 'dd/mm/yyyy') AND TO_DATE('"+ self.data_final +"','dd/mm/yyyy')")
        else:
            self.cursor.execute("SELECT SUM(fmc.TOT_NOTA_FISCAL) FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO WHERE FMC.STATUS = 'F' AND fmc.MODALIDADE IN ('A','G','O','V','I','T','M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN ("+ self.revenda +") AND fmc.TIPO_TRANSACAO = 'V21' AND fmc.DTA_DOCUMENTO BETWEEN '" + self.data_inicial + "' AND '" + self.data_final + "'")
        for linha in self.cursor.fetchall():
            if linha[0] is None:
                t_veiculos_novos = 0
                btnstat_ve = tkinter.DISABLED
            else:
                t_veiculos_novos = float(linha[0])
        self.valor_novos = Label(self.principal, text='Veiculos Novos', font=('verdana', 14, 'bold'))
        self.valor_novos.place(relx=0.05, rely=0.35)
        res1 = f'{t_veiculos_novos:_.2f}'
        pos = (20-(len(res1))+55)/100
        self.veiculos_novos = res1.replace('.', ',').replace('_', '.')
        self.valor_novos = Label(self.principal, text=self.veiculos_novos, font=('verdana', 14, 'bold'))
        self.valor_novos.place(relx = pos, rely = 0.35) # 0.55
        self.det_veinovos = Button(self.principal, text='Detalhar', font=('verdana',8,'bold'), stat=btnstat_ve, command=self.graf_vei_novos)
        self.det_veinovos.place(relx=0.85, rely=0.35)
        #
        btnstat_sn = tkinter.NORMAL
        if self.bancodados != 'SQLSERVER':
            self.cursor.execute("SELECT SUM(fmc.TOT_NOTA_FISCAL) FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO WHERE FMC.STATUS = 'F' AND fmc.MODALIDADE IN ('A','G','O','V','I','T','M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN ("+ self.revenda + ") AND fmc.TIPO_TRANSACAO = 'U21' AND fmc.DTA_DOCUMENTO BETWEEN TO_DATE('" + self.data_inicial + "', 'dd/mm/yyyy') AND TO_DATE('" + self.data_final + "','dd/mm/yyyy')")
        else:
            self.cursor.execute("SELECT SUM(fmc.TOT_NOTA_FISCAL) FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO WHERE FMC.STATUS = 'F' AND fmc.MODALIDADE IN ('A','G','O','V','I','T','M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN ("+ self.revenda + ") AND fmc.TIPO_TRANSACAO = 'U21' AND fmc.DTA_DOCUMENTO BETWEEN '" + self.data_inicial + "' AND '" + self.data_final + "'")
        for linha in self.cursor.fetchall():
            if linha[0] is None:
                t_veiculos_seminovos = 0
                btnstat_sn = tkinter.DISABLED
            else:
                t_veiculos_seminovos = float(linha[0])
        self.valor_seminovos = Label(self.principal, text='Veiculos Seminovos', font=('verdana', 14, 'bold'))
        self.valor_seminovos.place(relx=0.05, rely=0.50)
        res1 = f'{t_veiculos_seminovos:_.2f}'
        self.veiculos_seminovos = res1.replace('.', ',').replace('_', '.')
        pos = (20-(len(res1))+55)/100
        self.valor_seminovos = Label(self.principal, text=self.veiculos_seminovos, font=('verdana', 14, 'bold'))
        self.valor_seminovos.place(relx=pos, rely=0.50)
        self.det_veisnovos = Button(self.principal, text='Detalhar', font=('verdana', 8, 'bold'), stat=btnstat_sn, command = self.graf_vei_semi)  # , command=self.geraRelClient)
        self.det_veisnovos.place(relx=0.85, rely=0.50)
        #
        btnstat_pc = tkinter.NORMAL
        if self.bancodados != 'SQLSERVER':
            self.cursor.execute("SELECT SUM(fmc.TOT_NOTA_FISCAL) FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO WHERE FMC.STATUS = 'F' AND fmc.MODALIDADE IN ('A','G','O','V','I','T','M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO = 'P21' AND fmc.DTA_DOCUMENTO BETWEEN TO_DATE('" + self.data_inicial + "', 'dd/mm/yyyy') AND TO_DATE('" + self.data_final + "','dd/mm/yyyy')")
        else:
            self.cursor.execute("SELECT SUM(fmc.TOT_NOTA_FISCAL) FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO WHERE FMC.STATUS = 'F' AND fmc.MODALIDADE IN ('A','G','O','V','I','T','M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO = 'P21' AND fmc.DTA_DOCUMENTO BETWEEN '" + self.data_inicial + "' AND '" + self.data_final + "'")
        for linha in self.cursor.fetchall():
            if linha[0] is None:
                t_pecas = 0
                btnstat_pc = tkinter.DISABLED
            else:
                t_pecas = float(linha[0])
        self.valor_pecas = Label(self.principal, text='Peças', font=('verdana', 14, 'bold'))
        self.valor_pecas.place(relx=0.05, rely=0.65)
        res1 = f'{t_pecas:_.2f}'
        self.pecas = res1.replace('.', ',').replace('_', '.')
        pos = (20-(len(res1))+55)/100
        self.valor_pecas = Label(self.principal, text=self.pecas,font=('verdana', 14, 'bold'))
        self.valor_pecas.place(relx=pos, rely=0.65)
        self.det_pecas = Button(self.principal, text='Detalhar', font=('verdana', 8, 'bold'), stat=btnstat_pc)  # , command=self.geraRelClient)
        self.det_pecas.place(relx=0.85, rely=0.65)
        #
        btnstat_of = tkinter.NORMAL
        if self.bancodados != 'SQLSERVER':
            self.cursor.execute("SELECT SUM(fmc.TOT_NOTA_FISCAL) FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO WHERE FMC.STATUS = 'F' AND fmc.MODALIDADE IN ('A','G','O','V','I','T','M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO IN ('O21','G21') AND fmc.DTA_DOCUMENTO BETWEEN TO_DATE('" + self.data_inicial + "', 'dd/mm/yyyy') AND TO_DATE('" + self.data_final + "','dd/mm/yyyy')")
        else:
            self.cursor.execute("SELECT SUM(fmc.TOT_NOTA_FISCAL) FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO WHERE FMC.STATUS = 'F' AND fmc.MODALIDADE IN ('A','G','O','V','I','T','M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO IN ('O21','G21') AND fmc.DTA_DOCUMENTO BETWEEN '" + self.data_inicial + "' AND '" + self.data_final + "'")
        for linha in self.cursor.fetchall():
            if linha[0] is None:
                btnstat_of = tkinter.DISABLED
                t_oficina = 0
            else:
                t_oficina = float(linha[0])
        self.valor_oficina = Label(self.principal, text='Assistencia Técnica', font=('verdana', 14, 'bold'))
        self.valor_oficina.place(relx=0.05, rely=0.80)
        res1 = f'{t_oficina:_.2f}'
        self.oficina = res1.replace('.', ',').replace('_', '.')
        pos = (20-(len(res1))+55)/100
        self.valor_oficina = Label(self.principal, text=self.oficina, font=('verdana', 14, 'bold'))
        self.valor_oficina.place(relx=pos, rely=0.80)
        self.det_oficina = Button(self.principal, text='Detalhar', font=('verdana', 8, 'bold'), stat=btnstat_of, command = self.graf_oficina)  # , command=self.geraRelClient)
        self.det_oficina.place(relx=0.85, rely=0.80)
        self.desconecta_DB()