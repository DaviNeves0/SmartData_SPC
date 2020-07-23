import matplotlib.pyplot as plt
import csv
import pandas as pd

import tkinter as tk
from tkinter import filedialog
import pandas as pd


######TELA INICIAL######
root= tk.Tk()
root.iconbitmap(r'a.ico')
root.title('SMARTFILTER')

canvas1 = tk.Canvas(root, width = 700, height = 500, bg = '#F1F1F1')
canvas1.pack()
canvas1.create_text(350,30,fill="#FFC54F",font="Universltstd 20 bold",text="SPC Brasil - Importação de Dados por Remessa")
############

######FUNÇÕES PARA LER CADA ARQUIVO ESCOLHIDO######
def getfontes ():
    global fontes
    import_file_path = filedialog.askopenfilename()
    canvas1.create_text(450,80,fill='lightgreen',font='Universltstd 13 bold',text= import_file_path)
    fontes = pd.read_excel (import_file_path)
def getmodalidades ():
    global modalidades
    import_file_path = filedialog.askopenfilename()
    canvas1.create_text(450,120,fill='lightgreen',font='Universltstd 13 bold',text= import_file_path)
    modalidades = pd.read_excel (import_file_path)
def getpagamentos ():
    global pagamentos
    import_file_path = filedialog.askopenfilename()
    canvas1.create_text(450,160,fill='lightgreen',font='Universltstd 13 bold',text= import_file_path)
    pagamentos = pd.read_excel (import_file_path)
def getmovimentacoes ():
    global movimentacoes
    import_file_path = filedialog.askopenfilename()
    canvas1.create_text(450,200,fill='lightgreen',font='Universltstd 13 bold',text= import_file_path)
    movimentacoes = pd.read_excel (import_file_path)
def getoperacoes ():
    global operacoes
    import_file_path = filedialog.askopenfilename()
    canvas1.create_text(450,240,fill='lightgreen',font='Universltstd 13 bold',text= import_file_path)
    operacoes = pd.read_excel (import_file_path)
############
    
######BOTÕES PARA ESCOLHER OS ARQUIVOS EXCEL######
browseButton_Excel = tk.Button(text='Fontes', command=getfontes, bg='#154695', fg='white', font=('helvetica', 12, 'bold'), width=15, height=1)
canvas1.create_window(150, 80, window=browseButton_Excel)
browseButton_Excel = tk.Button(text='Modalidades', command=getmodalidades, bg='#154695', fg='white', font=('helvetica', 12, 'bold'), width=15, height=1)
canvas1.create_window(150, 120, window=browseButton_Excel)
browseButton_Excel = tk.Button(text='Pagamentos', command=getpagamentos, bg='#154695', fg='white', font=('helvetica', 12, 'bold'), width=15, height=1)
canvas1.create_window(150, 160, window=browseButton_Excel)
browseButton_Excel = tk.Button(text='Movimentações', command=getmovimentacoes, bg='#154695', fg='white', font=('helvetica', 12, 'bold'), width=15, height=1)
canvas1.create_window(150, 200, window=browseButton_Excel)
browseButton_Excel = tk.Button(text='Operações', command=getoperacoes, bg='#154695', fg='white', font=('helvetica', 12, 'bold'), width=15, height=1)
canvas1.create_window(150, 240, window=browseButton_Excel)
############

######INDICADORES######
def gerar_indicadores():
    fonte = entrada.get()
    fonte_buscada = fontes.query(f"ID_STG_FNT_ITT == {fonte}")
    nome_fonte = fonte_buscada.get('NOM_COM')
    ###OPERAÇÃO###
    valor_total_contratado_remessa = operacoes['VLR_CTRD_CSC'].sum()
    qtd_parcelas_remessa = operacoes['QTD_PCL'].sum()
    valor_total_saldo_devedor_remessa = operacoes['VLR_SDO_DDR'].sum()
    qtd_operacoes_remessa = operacoes['QTD_OPR'].sum()
    ###MOVIMENTAÇÃO###
    valor_total_utilizado = movimentacoes['VLR_SDO_UTZ_CRD_RTO'].sum()
    valor_total_faturamento = movimentacoes['VLR_TOT_FAT'].sum()
    valor_total_minimo = movimentacoes['VLR_MIM_FAT'].sum()
    valor_total_parcelas = movimentacoes['VLR_PCL_FAT'].sum()
    qtd_movimentacoes_remessa = movimentacoes['QTD_MVT'].sum()
    ###PAGAMENTO###
    valor_total_pagamentos = pagamentos['VLR_PGT_FAT'].sum()
    pagamentos['DAT_VCT'] = pagamentos['DAT_VCT'].astype(str)
    pagamentos['datas'] = pagamentos['DAT_VCT']
    x = 0
    qtd_registros_vencidos = 0
    while x < 15446:
        pagamentos['datas'][x] = pagamentos['DAT_VCT'][x][4:8] + pagamentos['DAT_VCT'][x][2:4] + pagamentos['DAT_VCT'][x][0:2]
        x+=1
    pagamentos['datas'] = pagamentos['datas'].astype(int)
    x = 0
    while x < 15446:
      if pagamentos['datas'][x] < 20200116:
        qtd_registros_vencidos+=1
      x+=1
    qtd_pagamentos_remessa = pagamentos['QTD_PGT'].sum()
    ###RESULTADOS###
    print('REMESSA DA FONTE: ',nome_fonte.to_string(index = False, header = False))
    print('OPERAÇÕES DE COMPRA')
    print('Valor total contratado (Consórcio): R$',valor_total_contratado_remessa)
    print('Quantidade de parcelas: ',qtd_parcelas_remessa)
    print('Valor total do saldo devedor: R$',valor_total_saldo_devedor_remessa)
    print('Quantidade de operações: ',qtd_operacoes_remessa)
    print('MOVIMENTAÇÕES DE CRÉDITO')
    print('Valor total utilizado (Crédito Rotativo): R$', valor_total_utilizado)
    print('Valor total de faturamento (Cartão de Crédito): R$', valor_total_faturamento)
    print('Valor total mínimo das faturas (Cartão de Crédito): R$', valor_total_minimo)
    print('Valor total das parcelas: R$', valor_total_parcelas)
    print('Quantidade de movimentações: ', qtd_movimentacoes_remessa)
    print('PAGAMENTOS')
    print('Valor total dos pagamentos: R$', valor_total_pagamentos)
    print('Quantidade de registros vencidos: ', qtd_registros_vencidos)
    print('Quantidade de pagamentos: ', qtd_pagamentos_remessa)
############

entrada = tk.Entry(root)
descrição = tk.Label(root, text="Insira o ID da fonte desejada: ")
canvas1.create_window(100,300, window=descrição)
canvas1.create_window(250, 300, window=entrada)
button1 = tk.Button(text='Gerar Indicadores', command=gerar_indicadores, bg='#154695', fg='white')
canvas1.create_window(200, 350, window=button1)
