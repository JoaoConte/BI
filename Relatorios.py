from Modulos import *

class Relatorios():
    def printCliente(self):
        webbrowser.open('cliente.pdf')
    def geraRelClient(self):
        self.c = canvas.Canvas('cliente.pdf')
        self.nomeRel = self.ent_nome.get()
        self.emailRel = self.ent_email.get()
        self.data1Rel = self.ent_data1.get()
        self.data2Rel = self.ent_data2.get()
        self.data3Rel = self.ent_data3.get()
        self.horasRel = self.ent_horas.get()
        self.valorRel = self.ent_valor.get()
        self.dataext=self.data1Rel+' '+self.data2Rel+' '+self.data3Rel

        logo = 'gmail.png'
        self.c.drawImage(logo, 30, 765, width=100, height=40)
        self.c.setFont('Helvetica-Bold', 10)
        var1 = self.nomeRel+' <'+self.emailRel+'>'
        var2 = (540-(len(var1)*4.5))
        self.c.drawString(var2, 779, var1)
        self.c.setFont('Helvetica-Bold', 20)
        self.c.drawString(200, 740, 'Ficha do Cliente')
        self.c.setFont('Helvetica', 18)
        self.c.drawString(50, 670, 'Nome....: ' + self.nomeRel)
        self.c.drawString(50, 640, 'E-mail..: ' + self.emailRel)
        self.c.drawString(50, 610, 'data....: ' + self.dataRel)
        self.c.drawString(50, 580, 'data....: ' + self.horasRel)
        self.c.drawString(50, 550, 'data....: ' + self.valorRel)
    #    self.c.rect(20, 600, 550, 120, fill=False, stroke=True) # Moldura
        self.c.showPage()
        self.c.save()
        self.printCliente()
