import matplotlib.pyplot as plt

from Modulos import *

class Funcs():
    def cria(self):
        self.empresa = ''
        self.data_inicial = ''
        self.data_final = ''

    def graf_vei_novos(self):
        self.nome1 = []
        self.valor1 = []
        self.conecta_DB()
        fig = plt.figure(figsize=(13, 6))
        if self.bancodados != 'SQLSERVER':
            self.cursor.execute("SELECT gu.NOME, SUM(fmc.TOT_NOTA_FISCAL) FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO LEFT JOIN GER_USUARIO gu ON gu.USUARIO = fmc.USUARIO WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN ('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO = 'V21' AND fmc.DTA_DOCUMENTO BETWEEN TO_DATE('" + self.data_inicial + "', 'dd/mm/yyyy') AND TO_DATE('" + self.data_final + "','dd/mm/yyyy') GROUP BY gu.NOME")
        else:
            self.cursor.execute("SELECT gu.NOME, SUM(fmc.TOT_NOTA_FISCAL) FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO LEFT JOIN GER_USUARIO gu ON gu.USUARIO = fmc.USUARIO WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN ('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO = 'V21' AND fmc.DTA_DOCUMENTO BETWEEN '" + self.data_inicial + "' AND '" + self.data_final + "' GROUP BY gu.NOME")
        for linha in self.cursor.fetchall():
            nome = linha[0]
            nomex = nome.strip().split(' ')[0]
            self.nome1.append(nomex)
            self.valor1.append((linha[1]))
        self.x = arange(len(self.nome1))
        self.largura = 0.3
        plt.subplot(2,2,1)
        plt.bar(self.x, self.valor1, width=self.largura, label = 'Vendas', color = 'blue')
        plt.title('Venda de Veiculos novos por vendedor')
        plt.xticks(self.x, self.nome1, rotation = 30)
        plt.legend()
        # --------------------------------------------------------------------
        self.nome2 = []
        self.valor2 = []
        self.conecta_DB()
        if self.bancodados != 'SQLSERVER':
            self.cursor.execute("SELECT vf.DES_FAMILIA, COUNT(fmc.NUMERO_NOTA_FISCAL) AS 'UNIDADES' FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO LEFT JOIN FAT_MOVIMENTO_VEICULO fmv ON fmv.EMPRESA = fmc.EMPRESA AND fmv.REVENDA = fmc.REVENDA AND fmv.NUMERO_NOTA_FISCAL = fmc.NUMERO_NOTA_FISCAL AND fmv.SERIE_NOTA_FISCAL = fmc.SERIE_NOTA_FISCAL LEFT JOIN VEI_VEICULO vv ON vv.VEICULO = fmv.VEICULO AND vv.EMPRESA = fmc.EMPRESA LEFT JOIN VEI_MODELO vm ON vm.MODELO = vv.MODELO AND vm.EMPRESA = fmc.EMPRESA LEFT JOIN VEI_FAMILIA vf ON vf.FAMILIA = vm.FAMILIA AND vf.EMPRESA = fmc.EMPRESA WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO = 'V21' AND fmc.DTA_DOCUMENTO BETWEEN '" + self.data_inicial + "' AND '" + self.data_final + "' GROUP BY vf.DES_FAMILIA order by unidades desc ")
        else:
            self.cursor.execute("SELECT vf.DES_FAMILIA, COUNT(fmc.NUMERO_NOTA_FISCAL) AS 'UNIDADES' FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO LEFT JOIN FAT_MOVIMENTO_VEICULO fmv ON fmv.EMPRESA = fmc.EMPRESA AND fmv.REVENDA = fmc.REVENDA AND fmv.NUMERO_NOTA_FISCAL = fmc.NUMERO_NOTA_FISCAL AND fmv.SERIE_NOTA_FISCAL = fmc.SERIE_NOTA_FISCAL LEFT JOIN VEI_VEICULO vv ON vv.VEICULO = fmv.VEICULO AND vv.EMPRESA = fmc.EMPRESA LEFT JOIN VEI_MODELO vm ON vm.MODELO = vv.MODELO AND vm.EMPRESA = fmc.EMPRESA LEFT JOIN VEI_FAMILIA vf ON vf.FAMILIA = vm.FAMILIA AND vf.EMPRESA = fmc.EMPRESA WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO = 'V21' AND fmc.DTA_DOCUMENTO BETWEEN '" + self.data_inicial + "' AND '" + self.data_final + "' GROUP BY vf.DES_FAMILIA order by unidades desc ")
        for linha in self.cursor.fetchall():
             self.nome2.append(linha[0])
             self.valor2.append((linha[1]))
        plt.subplot(2, 2, 2)
        plt.pie(self.valor2, labels = self.nome2, autopct='%1.1f%%')
        plt.title('Unidades por familia')
        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
        #--------------------------------------------------------------------
        self.nome3 = []
        self.valor3 = []
        self.conecta_DB()
        if self.bancodados != 'SQLSERVER':
            self.cursor.execute("SELECT gu.NOME, SUM(fmc.TOT_NOTA_FISCAL)- SUM(fmc.TOT_CUSTO_MEDIO) AS LUCRO FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO LEFT JOIN GER_USUARIO gu ON gu.USUARIO = fmc.USUARIO WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN ('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO = 'V21' AND fmc.DTA_DOCUMENTO BETWEEN TO_DATE('" + self.data_inicial +"', 'dd/mm/yyyy') AND TO_DATE('" + self.data_final + "', 'dd/mm/yyyy') GROUP BY gu.NOME ORDER BY LUCRO DESC")
        else:
            self.cursor.execute("SELECT gu.NOME, SUM(fmc.TOT_NOTA_FISCAL)- SUM(fmc.TOT_CUSTO_MEDIO) AS LUCRO FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO LEFT JOIN GER_USUARIO gu ON gu.USUARIO = fmc.USUARIO WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN ('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO = 'V21' AND fmc.DTA_DOCUMENTO BETWEEN '" + self.data_inicial + "' AND '" + self.data_final + "' GROUP BY gu.NOME ORDER BY LUCRO DESC")
        for linha in self.cursor.fetchall():
            nome = linha[0]
            nomex = nome.strip().split(' ')[0]
            self.nome3.append(nomex)
            self.valor3.append((linha[1]))
        self.x = arange(len(self.nome2))
        self.largura = 0.3
        plt.subplot(2, 2, 3)
        plt.barh(self.nome3, self.valor3, label='Lucro bruto', color='green')
        plt.title('Qualidade da venda de Veiculos novos por vendedor')
        plt.legend()
        plt.show()
        self.desconecta_DB()

    def graf_vei_semi(self):
        self.nome1 = []
        self.valor1 = []
        self.conecta_DB()
        fig = plt.figure(figsize=(13, 6))
        if self.bancodados != 'SQLSERVER':
            self.cursor.execute("SELECT gu.NOME, SUM(fmc.TOT_NOTA_FISCAL) FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO LEFT JOIN GER_USUARIO gu ON gu.USUARIO = fmc.USUARIO WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN ('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO = 'U21' AND fmc.DTA_DOCUMENTO BETWEEN TO_DATE('" + self.data_inicial + "', 'dd/mm/yyyy') AND TO_DATE('" + self.data_final + "','dd/mm/yyyy') GROUP BY gu.NOME")
        else:
            self.cursor.execute("SELECT gu.NOME, SUM(fmc.TOT_NOTA_FISCAL) FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO LEFT JOIN GER_USUARIO gu ON gu.USUARIO = fmc.USUARIO WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN ('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO = 'U21' AND fmc.DTA_DOCUMENTO BETWEEN '" + self.data_inicial + "' AND '" + self.data_final + "' GROUP BY gu.NOME")
        for linha in self.cursor.fetchall():
            nome = linha[0]
            nomex = nome.strip().split(' ')[0]
            self.nome1.append(nomex)
            self.valor1.append((linha[1]))
        self.x = arange(len(self.nome1))
        self.largura = 0.3
        plt.subplot(2,2,1)
        plt.bar(self.x, self.valor1, width=self.largura, label = 'Vendas', color = 'blue')
        plt.title('Venda de Veiculos Seminovos por vendedor')
        plt.xticks(self.x, self.nome1, rotation = 30)
        plt.legend()
        # --------------------------------------------------------------------
        self.nome2 = []
        self.valor2 = []
        self.conecta_DB()
        if self.bancodados != 'SQLSERVER':
            self.cursor.execute("SELECT vf.DES_FAMILIA, COUNT(fmc.NUMERO_NOTA_FISCAL) AS 'UNIDADES' FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO LEFT JOIN FAT_MOVIMENTO_VEICULO fmv ON fmv.EMPRESA = fmc.EMPRESA AND fmv.REVENDA = fmc.REVENDA AND fmv.NUMERO_NOTA_FISCAL = fmc.NUMERO_NOTA_FISCAL AND fmv.SERIE_NOTA_FISCAL = fmc.SERIE_NOTA_FISCAL LEFT JOIN VEI_VEICULO vv ON vv.VEICULO = fmv.VEICULO AND vv.EMPRESA = fmc.EMPRESA LEFT JOIN VEI_MODELO vm ON vm.MODELO = vv.MODELO AND vm.EMPRESA = fmc.EMPRESA LEFT JOIN VEI_FAMILIA vf ON vf.FAMILIA = vm.FAMILIA AND vf.EMPRESA = fmc.EMPRESA WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO = 'U21' AND fmc.DTA_DOCUMENTO BETWEEN '" + self.data_inicial + "' AND '" + self.data_final + "' GROUP BY vf.DES_FAMILIA order by unidades desc ")
        else:
            self.cursor.execute("SELECT vf.DES_FAMILIA, COUNT(fmc.NUMERO_NOTA_FISCAL) AS 'UNIDADES' FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO LEFT JOIN FAT_MOVIMENTO_VEICULO fmv ON fmv.EMPRESA = fmc.EMPRESA AND fmv.REVENDA = fmc.REVENDA AND fmv.NUMERO_NOTA_FISCAL = fmc.NUMERO_NOTA_FISCAL AND fmv.SERIE_NOTA_FISCAL = fmc.SERIE_NOTA_FISCAL LEFT JOIN VEI_VEICULO vv ON vv.VEICULO = fmv.VEICULO AND vv.EMPRESA = fmc.EMPRESA LEFT JOIN VEI_MODELO vm ON vm.MODELO = vv.MODELO AND vm.EMPRESA = fmc.EMPRESA LEFT JOIN VEI_FAMILIA vf ON vf.FAMILIA = vm.FAMILIA AND vf.EMPRESA = fmc.EMPRESA WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO = 'U21' AND fmc.DTA_DOCUMENTO BETWEEN '" + self.data_inicial + "' AND '" + self.data_final + "' GROUP BY vf.DES_FAMILIA order by unidades desc ")
        for linha in self.cursor.fetchall():
             self.nome2.append(linha[0])
             self.valor2.append((linha[1]))
        plt.subplot(2, 2, 2)
        plt.pie(self.valor2, labels = self.nome2, autopct='%1.1f%%')
        plt.title('Unidades por familia')
        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
        #--------------------------------------------------------------------
        self.nome3 = []
        self.valor3 = []
        self.conecta_DB()
        if self.bancodados != 'SQLSERVER':
            self.cursor.execute("SELECT gu.NOME, SUM(fmc.TOT_NOTA_FISCAL)- SUM(fmc.TOT_CUSTO_MEDIO) AS LUCRO FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO LEFT JOIN GER_USUARIO gu ON gu.USUARIO = fmc.USUARIO WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN ('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO = 'U21' AND fmc.DTA_DOCUMENTO BETWEEN TO_DATE('" + self.data_inicial +"', 'dd/mm/yyyy') AND TO_DATE('" + self.data_final + "', 'dd/mm/yyyy') GROUP BY gu.NOME ORDER BY LUCRO DESC")
        else:
            self.cursor.execute("SELECT gu.NOME, SUM(fmc.TOT_NOTA_FISCAL)- SUM(fmc.TOT_CUSTO_MEDIO) AS LUCRO FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO LEFT JOIN GER_USUARIO gu ON gu.USUARIO = fmc.USUARIO WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN ('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN (" + self.revenda +") AND fmc.TIPO_TRANSACAO = 'U21' AND fmc.DTA_DOCUMENTO BETWEEN '" + self.data_inicial + "' AND '" + self.data_final + "' GROUP BY gu.NOME ORDER BY LUCRO DESC")
        for linha in self.cursor.fetchall():
            nome = linha[0]
            nomex = nome.strip().split(' ')[0]
            self.nome3.append(nomex)
            self.valor3.append((linha[1]))
        self.x = arange(len(self.nome2))
        self.largura = 0.3
        plt.subplot(2, 2, 3)
        plt.barh(self.nome3, self.valor3, label='Lucro bruto', color='green')
        plt.title('Qualidade da venda de Veiculos Seminovos por vendedor')
        plt.legend()
        plt.show()
        self.desconecta_DB()

    def graf_oficina(self):
        # Venda por consultor
        self.nome2 = []
        self.total_venda = []
        self.desconto_pecas = []
        self.desconto_mo = []
        self.total_liquido = []
        self.conecta_DB()
        fig = plt.figure(figsize=(13, 6))
        if self.bancodados != 'SQLSERVER':
            self.cursor.execute("SELECT gu.NOME, sum(fmc.TOT_NOTA_FISCAL) as TOTAL_VENDA, sum(fmc.VALDESCONTO) AS DENCONTO_PEÇAS, sum(fmc.VALDESCONTO_MO) DESCONTO_MO, SUM(fmc.TOT_NOTA_FISCAL)-sum(fmc.VALDESCONTO)-sum(fmc.VALDESCONTO_MO) AS TOTAL_LIQUIDO FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO LEFT JOIN GER_USUARIO gu ON gu.USUARIO = fmc.USUARIO WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN ('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN ("+ self.revenda + ") AND fmc.TIPO_TRANSACAO in ('O21','G21','O26','O31') AND fmc.DTA_DOCUMENTO BETWEEN TO_DATE('" + self.data_inicial + "', 'dd/mm/yyyy') AND TO_DATE('" + self.data_final +"', 'dd/mm/yyyy') GROUP BY gu.NOME ORDER BY TOTAL_LIQUIDO  DESC")
        else:
            self.cursor.execute("SELECT gu.NOME, sum(fmc.TOT_NOTA_FISCAL) as TOTAL_VENDA, sum(fmc.VALDESCONTO) AS DENCONTO_PEÇAS, sum(fmc.VALDESCONTO_MO) DESCONTO_MO, SUM(fmc.TOT_NOTA_FISCAL)-sum(fmc.VALDESCONTO)-sum(fmc.VALDESCONTO_MO) AS TOTAL_LIQUIDO FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO LEFT JOIN GER_USUARIO gu ON gu.USUARIO = fmc.USUARIO WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN ('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN ("+ self.empresa + ") AND fmc.REVENDA IN ("+ self.revenda + ") AND fmc.TIPO_TRANSACAO in ('O21','G21','O26','O31') AND fmc.DTA_DOCUMENTO BETWEEN '" + self.data_inicial + "' AND '" + self.data_final +"' GROUP BY gu.NOME ORDER BY TOTAL_LIQUIDO DESC")
        for linha in self.cursor.fetchall():
            nome = linha[0]
            nomex = nome.strip().split(' ')[0]
            self.nome2.append(nomex)
            self.total_venda.append((linha[1]))
            self.desconto_pecas.append((linha[2]))
            self.desconto_mo.append((linha[3]))
            self.total_liquido.append((linha[4]))
        self.x = arange(len(self.nome2))
        self.largura = 0.2
        plt.subplot(1, 2, 1)
        plt.bar(self.x + 0.01, self.total_venda, width=self.largura, label='Total Vendas Bruto', color='blue',)
        plt.bar(self.x + 0.21, self.desconto_pecas, width=self.largura, label='Desconto Peças', color='red')
        plt.bar(self.x + 0.41, self.desconto_mo, width=self.largura, label='Desconto MO', color='yellow')
        plt.bar(self.x + 0.61, self.total_liquido, width=self.largura, label='Total Liquido', color='green')
        plt.title('Venda de Assistência Técnica por Consultor')
        plt.xticks(self.x, self.nome2, rotation=30)
        plt.grid()
        plt.legend()
        # Venda por tipo de OS
        self.nome3 = []
        self.total_venda = []
        self.conecta_DB()
        #fig = plt.figure(figsize=(13, 6))
        if self.bancodados != 'SQLSERVER':
            self.cursor.execute(
                "SELECT fmc.TIPO_OS, SUM(fmc.TOT_NOTA_FISCAL)-sum(fmc.VALDESCONTO)-sum(fmc.VALDESCONTO_MO) AS TOTAL_LIQUIDO FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN ('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN (" + self.empresa + ") AND fmc.REVENDA IN (" + self.revenda + ") AND fmc.TIPO_TRANSACAO in ('O21', 'G21', 'G22', 'O26', 'O31') AND fmc.DTA_DOCUMENTO BETWEEN TO_DATE('" + self.data_inicial + "', 'dd/mm/yyyy') AND TO_DATE('" + self.data_final + "', 'dd/mm/yyyy') GROUP BY fmc.TIPO_OS")
        else:
            self.cursor.execute(
                "SELECT fmc.TIPO_OS, SUM(fmc.TOT_NOTA_FISCAL)-sum(fmc.VALDESCONTO)-sum(fmc.VALDESCONTO_MO) AS TOTAL_LIQUIDO FROM FAT_MOVIMENTO_CAPA fmc LEFT JOIN FAT_TIPO_TRANSACAO ftt ON ftt.TIPO_TRANSACAO = fmc.TIPO_TRANSACAO WHERE fmc.STATUS = 'F' AND fmc.MODALIDADE IN ('A', 'G', 'O', 'V', 'I', 'T', 'M') AND ftt.TIPO = 'S' AND fmc.EMPRESA IN (" + self.empresa + ") AND fmc.REVENDA IN (" + self.revenda + ") AND fmc.TIPO_TRANSACAO in ('O21', 'G21', 'G22', 'O26', 'O31') AND fmc.DTA_DOCUMENTO BETWEEN '" + self.data_inicial +"' AND '" + self.data_final + "' GROUP BY fmc.TIPO_OS")
        for linha in self.cursor.fetchall():
            if linha[0] == 'G':
                self.nome3.append('Garantia')
            elif linha[0] == 'E':
                self.nome3.append('Externa')
            elif linha[0] == 'R':
                self.nome3.append('Revisão')
            elif linha[0] == 'I':
                self.nome3.append('Interna')
            elif linha[0] == 'F':
                self.nome3.append('Franquia')
            self.total_venda.append((linha[1]))
        self.x = arange(len(self.nome3))
        self.largura = 0.3
        plt.subplot(1, 2, 2)
        plt.bar(self.x, self.total_venda, width=self.largura, label='Total Vendas Bruto', color='blue', )
        plt.title('Venda de Assistência Técnica por Tipo de OS')
        plt.xticks(self.x, self.nome3, rotation=30)
        plt.grid()
        plt.show()

    def conecta_DB(self):
        if self.bancodados != 'SQLSERVER':
            self.cbd_ora = cx_Oracle.connect('linx/ninguemsabe@contevaio/XE')
            self.cursor = self.cbd_ora.cursor()
        else:
            self.cbd_sql = pyodbc.connect("Driver="+self.drive+"; Server="+self.servidor+"; Database="+self.banco+"; TrustedConnection=yes")
            self.cursor = self.cbd_sql.cursor()

    def desconecta_DB(self):
        if self.bancodados != 'SQLSERVER':
            self.cbd_ora.close()
        else:
            self.cbd_sql.close()

    def limpa_tela(self):
        self.ent_nome.delete(0, END)
        self.ent_email.delete(0, END)
        self.ent_data1.delete(0, END)
        self.ent_data2.delete(0, END)
        self.ent_data3.delete(0, END)
        self.ent_horas.delete(0, END)
        self.ent_valor.delete(0, END)

    def variaveis(self):
        self.nome = self.ent_nome.get()
        self.email = self.ent_email.get()
        self.data1 = self.ent_data.get()
        self.data2 = self.ent_data.get()
        self.data3 = self.ent_data.get()
        self.horas = self.ent_horas.get()
        self.valor = self.ent_valor.get()

    def calendario_ini(self):
         self.calendario_1 = Calendar(self.principal, locale='pt_br')
         self.calendario_1.place(relx=0.6, rely=0.05)
         self.caldata_ini=Button(self.principal, text='Confirmar data Inicial', command=self.print_cal_ini)
         self.caldata_ini.place(relx=0.6, rely=0.51, height=25, width=120)
    def print_cal_ini(self):
         dataini = self.calendario_1.get_date()
         self.data_inicial1 = self.calendario_1.get_date()
         self.data_inicial = self.data_inicial1#[0:2] + '-' + self.data_inicial1[3:5] + '-' + self.data_inicial1[6:]
         self.calendario_1.destroy()
         self.ent_data_ini.delete(0,END)
         self.ent_data_ini.insert(END, dataini)
         self.caldata_ini.destroy()

    def calendario_fim(self):
         self.calendario_2 = Calendar(self.principal, locale='pt_br')
         self.calendario_2.place(relx=0.7, rely=0.05)
         self.caldata_fim=Button(self.principal, text='Confirmar data Final', command=self.print_cal_fim)
         self.caldata_fim.place(relx=0.7, rely=0.51, height=25, width=120)
    def print_cal_fim(self):
         datafim = self.calendario_2.get_date()
         self.data_final1 = self.calendario_2.get_date()
         self.data_final = self.data_final1#[0:2]+'-'+self.data_final1[3:5]+'-'+self.data_final1[6:]
         self.calendario_2.destroy()
         self.ent_data_fim.delete(0,END)
         self.ent_data_fim.insert(END, datafim)
         self.caldata_fim.destroy()

    def le_conexao(self, caminho):
        try:
            with open(caminho + '\conexao.dat', 'r') as conecta:
                for self.leitura in conecta:
                    if self.leitura[0:12] == '[BANCODADOS]':
                        self.bancodados = self.leitura[13:]
                        self.bancodados = self.bancodados.strip("\n")
                        if self.bancodados == 'SQLSERVER':
                            self.drive = "SQL Server"
                    if self.leitura[0:10] == '[DATABASE]':
                        if self.bancodados == 'SQLSERVER':
                            self.posp = self.leitura.find(':')
                            self.servidor = self.leitura[11:self.posp]
                            self.banco1 = self.leitura[self.posp + 1:]
                            self.banco = self.banco1.strip("\n")
                        else:
                            self.posp = self.leitura.find('/')
                            self.banco1 = self.leitura[11:self.posp]
                            self.banco2 = self.leitura[self.posp + 1:]
                            self.bancoa = self.banco1.strip('\n')
                            self.bancob = self.banco2.strip('\n')
                    if self.leitura[0:16] == '[USUARIO_ORACLE]':
                        self.usuario1 = self.leitura[17:]
                        self.usuario = self.usuario1.strip('\n')
                        self.senha = 'ninguemsabe'
            if self.bancodados != 'SQLSERVER':
                # self.ora_conn = (usuario+"/"+senha+"@"+ bancoa+"/"+bancob)
                self.ora_conn = ('linx/ninguemsabe@contevaio/XE')

        except OSError:
            print('Deu Ruim')
 

