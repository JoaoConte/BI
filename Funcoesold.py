from PySimpleGUI import PySimpleGUI as sg
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Monta telas
def tela_senha(eixox, eixoy): # Tela informação Usuario e senha (somente para Oracle)
    global xusuario, xsenha
    sg.theme('Reddit')
    layout = [
        [sg.Text('Senha do banco de dados                                    ')],
        [sg.Text('Senha ', size=(6)), sg.Input(size=(14), key='xsenha',  password_char='*')],
        [sg.Button('>> Empresa')]
    ]
    return sg.Window('Validador Operação Assistida', layout= layout, finalize = True, location = (eixox, eixoy))

def tela_empresa(eixox, eixoy, lista_empresa): # Tela seleção Empresa
    sg.theme('Reddit')
    layout = [
        [sg.Text('Selecione a Empresa                                        ')],
        [sg.Combo(lista_empresa, key='emp')],
        [sg.Button('<< Senha'), sg.Button('>> Revenda')]
    ] 
    return sg.Window('Validador Operação Assistida', layout= layout, finalize = True, location = (eixox, eixoy))
    
def tela_revenda(eixox, eixoy, lista_revenda): # Tela selecao Revenda
    sg.theme('Reddit')
    layout = [
        [sg.Text('Selecione a Revenda                                         ')],
        [sg.Combo(lista_revenda, key='rev')],
        [sg.Button('<< Empresa'), sg.Button('>> Seleção Módulos')]
    ] 
    return sg.Window('Validador Operação Assistida', layout= layout, finalize = True, location = (eixox, eixoy))
    
def menu_principal():
    pass 

#Faz leitura do Script
def valida(script):
    cursor.execute(script)
    for linha in cursor.fetchall():
        retorna = int(linha[0])    
    return retorna

#----- Gera PDF lista validados
def imprime_lista(matriz, saida, titulo):
    try:
        pdf = canvas.Canvas(saida+'.pdf')
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(80,800, 'Operação Assistida Peças - '+titulo)
        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawString(400,780, 'GO LIVE: 01'+vdataini)
        pdf.drawString(80,760, 'Empresa: '+empresa+' Revenda: '+revenda+' Cliente: ' + razao[0])
        pdf.setFont("Helvetica", 11)
        x = 740
        for ocorrencia in matriz:
            x -= 13
            pdf.drawString(50,x, '- ' + ocorrencia)
        pdf.drawString(50,20, 'Documento dispensa assinatura pois só pode ser emitido quando todos os itens estiverem validados') 
        pdf.drawString(350,8, 'Data/Hora: '+ vdata)    
        pdf.save()
        sg.popup(saida+'.pdf criado com sucesso!')
    except:
        sg.popup('Erro ao gerar '+saida+'.pdf')
    return
#---- Gera PDF lista de não validados
def imprime_erro(matriz, saida, titulo):
    try:
        pdf = canvas.Canvas(saida+'.pdf')
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(80,800, 'Operação Assistida Peças - '+titulo)
        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawString(80,760, 'Empresa: '+empresa+' Revenda: '+revenda+' Cliente: ' + razao[0])
        pdf.setFont("Helvetica", 11)
        x = 740
        for ocorrencia in matriz:
            x -= 13
            pdf.drawString(50,x, '- ' + ocorrencia)
        pdf.save()
        sg.popup(saida+'.pdf criado com sucesso!')
    except:
        sg.popup('Erro ao gerar '+saida+'.pdf')
    return    