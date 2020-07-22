import matplotlib.pyplot as plt
import csv
import pandas as pd

import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()
root.iconbitmap(r'a.ico')

canvas1 = tk.Canvas(root, width = 700, height = 500, bg = '#F1F1F1')
canvas1.pack()
canvas1.create_text(350,30,fill="#FFC54F",font="Universltstd 20 bold",text="SPC Brasil - Importação de Dados por Remessa")

def getfontes ():
    global df, fontessemvazio
    import_file_path = filedialog.askopenfilename()
    canvas1.create_text(450,80,fill='lightgreen',font='Universltstd 13 bold',text= import_file_path)
    df = pd.read_excel (import_file_path)
    fontessemvazio = df.dropna()
    print(fontessemvazio)
browseButton_Excel = tk.Button(text='Fontes', command=getfontes, bg='#154695', fg='white', font=('helvetica', 12, 'bold'), width=15, height=1)
canvas1.create_window(150, 80, window=browseButton_Excel)
def getmodalidades ():
    global df, modssemvazio
    import_file_path = filedialog.askopenfilename()
    canvas1.create_text(450,120,fill='lightgreen',font='Universltstd 13 bold',text= import_file_path)
    df = pd.read_excel (import_file_path)
    modssemvazio = df.dropna()
    print(modssemvazio)
browseButton_Excel = tk.Button(text='Modalidades', command=getmodalidades, bg='#154695', fg='white', font=('helvetica', 12, 'bold'), width=15, height=1)
canvas1.create_window(150, 120, window=browseButton_Excel)
def getpagamentos ():
    global df, pagssemvazio
    import_file_path = filedialog.askopenfilename()
    canvas1.create_text(450,160,fill='lightgreen',font='Universltstd 13 bold',text= import_file_path)
    df = pd.read_excel (import_file_path)
    pagssemvazio = df.dropna()
    print(pagssemvazio)
browseButton_Excel = tk.Button(text='Pagamentos', command=getpagamentos, bg='#154695', fg='white', font=('helvetica', 12, 'bold'), width=15, height=1)
canvas1.create_window(150, 160, window=browseButton_Excel)
def getmovimentacoes ():
    global df, movssemvazio
    import_file_path = filedialog.askopenfilename()
    canvas1.create_text(450,200,fill='lightgreen',font='Universltstd 13 bold',text= import_file_path)
    df = pd.read_excel (import_file_path)
    movssemvazio = df.dropna()
    print(movssemvazio)
browseButton_Excel = tk.Button(text='Movimentações', command=getmovimentacoes, bg='#154695', fg='white', font=('helvetica', 12, 'bold'), width=15, height=1)
canvas1.create_window(150, 200, window=browseButton_Excel)
def getoperacoes ():
    global df, opssemvazio
    import_file_path = filedialog.askopenfilename()
    canvas1.create_text(450,240,fill='lightgreen',font='Universltstd 13 bold',text= import_file_path)
    df = pd.read_excel (import_file_path)
    opssemvazio = df.dropna()
    print(opssemvazio)
browseButton_Excel = tk.Button(text='Operações', command=getoperacoes, bg='#154695', fg='white', font=('helvetica', 12, 'bold'), width=15, height=1)
canvas1.create_window(150, 240, window=browseButton_Excel)

##http://felipegalvao.com.br/blog/2016/02/29/manipulacao-de-dados-com-python-pandas/
##http://felipegalvao.com.br/blog/2016/02/18/ciencia-de-dados-com-python-basico-do-pandas-leitura-de-dataframes/
##As variáveis printadas estão com todos os campos da tabela preenchidos
