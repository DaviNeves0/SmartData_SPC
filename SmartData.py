import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox
import threading
import os
import shutil
from PIL import ImageTk, Image
import fontes

class app_menu(object):
    def __init__(self):
        self.root = tk.Tk()
        window_height = 250
        window_width = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.root.iconphoto(False, tk.PhotoImage(file='./icones/icon.png'))  
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.root.resizable(0, 0)
        self.root.title("SmartData")
        self.frame_progresso = tk.Frame(self.root)
        self.frame_progresso.place(relx=0.0, rely=0.756, relheight=0.244, relwidth=1.024)
        self.frame_progresso.configure(relief='flat')
        self.frame_progresso.configure(borderwidth="2")
        self.frame_progresso.configure(background="#14141c")
        self.frame_menu = tk.Frame(self.root)
        self.frame_menu.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.frame_menu.configure(relief='flat')
        self.frame_menu.configure(borderwidth="2")
        self.frame_menu.configure(background="#7d9096")
        self.lbl_titulo_menu = tk.Label(self.frame_menu, font=('Impact', 15, 'bold'))
        self.lbl_titulo_menu.place(x=195, rely=0.35, anchor="center")
        self.lbl_titulo_menu.configure(background="#7d9096")
        self.lbl_titulo_menu.configure(foreground="#6442c9")
        self.lbl_titulo_menu.configure(text='''• SmartData •\n- Análise de fontes -\n\n\nSimples, fácil e rápido.''')
        self.lbl_FNT = tk.Label(self.frame_menu, font=('Segoe UI', 9, 'bold'))
        self.lbl_FNT.place(relx=0.056, rely=0.700, height=30)
        self.lbl_FNT.configure(background="#7d9096")
        self.lbl_FNT.configure(foreground="#2dc225")
        self.lbl_FNT.configure(text='''FONTE\n(FNT)''')

        global lbldialog        
        lbldialog = self.lbldialog = tk.Label(self.frame_progresso, font=('Segoe UI', 9, 'bold'))
        self.lbldialog.configure(background="#14141c")
        self.lbldialog.configure(foreground="white")
        self.lbldialog.configure(text='''''')
        self.lbldialog.place(x=450, rely=0.219, anchor="center")
        
        global lbldialog2
        lbldialog2 = self.lbldialog2 = tk.Label(self.frame_progresso, font=('Segoe UI', 9, 'bold'))
        self.lbldialog2.configure(background="#14141c")
        self.lbldialog2.configure(foreground="white")
        self.lbldialog2.configure(text='''''')
        self.lbldialog2.place(x=450, rely=0.645, anchor="center")
        
        global entrada1    
        entrada1 = self.entrada1 = tk.Entry(self.frame_menu, relief="solid")
        self.entrada1.place(relx=0.190, rely=0.700,height=25, relwidth=0.600)
        self.entrada1.configure(background="white")
        self.entrada1.configure(foreground="#000000")
        
        self.btn_FNT = tk.Button(self.frame_menu, font=('Segoe UI', 9, 'bold'), bd=0, command=lambda:self.SelecionarArquivo(self.entrada1))
        self.btn_FNT.place(relx=0.744, rely=0.700, height=25, width=90)
        self.btn_FNT.configure(activebackground="#ececec")
        self.btn_FNT.configure(activeforeground="#000000")
        self.btn_FNT.configure(background="#a83246")
        self.btn_FNT.configure(disabledforeground="#a3a3a3")
        self.btn_FNT.configure(foreground="white")
        self.btn_FNT.configure(pady="0")
        self.btn_FNT.configure(relief="flat")
        self.btn_FNT.configure(text='''PROCURAR''')
        
        self.btnGenerate = tk.Button(self.frame_menu, font=('Segoe UI', 13, 'bold'), bd=0, command=self.inicia_thread)
        self.btnGenerate.place(relx=0.275, rely=0.833, height=35, width=170)
        self.btnGenerate.configure(activebackground="#7d9096")
        self.btnGenerate.configure(activeforeground="#7d9096")
        self.btnGenerate.configure(background="#6442c9")
        self.btnGenerate.configure(disabledforeground="#7d9096")
        self.btnGenerate.configure(foreground="white")
        self.btnGenerate.configure(pady="0")
        self.btnGenerate.configure(relief="flat")
        self.btnGenerate.configure(text='''VER ANÁLISE''')

    def inicia_thread(self):
        self.btn_FNT['state'] = 'disable'
        self.btnGenerate['state'] = 'disable'
        
        style = ttk.Style()
        style.theme_use('alt')
        style.configure("bar.Horizontal.TProgressbar", foreground='white', background='#0051ff',
                        troughcolor='white', troughrelief = 'flat')
        self.progbar = ttk.Progressbar(self.frame_progresso, length=800, style='bar.Horizontal.TProgressbar')
        self.progbar.config(maximum=4, mode='indeterminate')
        self.progbar.place(x=450, rely=0.419, width=900, height=25, anchor="center")

        self.progbar.start()
        self.thread_secundario = threading.Thread(target=GerarRelatorio)
        self.thread_secundario.start()
        self.root.after(50, self.checa_thread)

    def checa_thread(self):
        if self.thread_secundario.is_alive():
            self.root.after(50, self.checa_thread)
        else:
            self.progbar.stop()

            style = ttk.Style()
            style.theme_use('alt')
            style.configure("bar.Horizontal.TProgressbar", foreground='#0051ff', background='#0051ff',troughcolor='#0051ff', troughrelief = 'flat')
            self.progbar = ttk.Progressbar(self.frame_progresso, length=800, style='bar.Horizontal.TProgressbar')
            self.progbar.config(maximum=4, mode='indeterminate')
            self.progbar.place(x=450, rely=0.419, width=900, height=25, anchor="center")
            self.btn_FNT['state'] = 'normal'
            self.btnGenerate['state'] = 'normal'

    def SelecionarArquivo(self, entrada):
        entrada.delete(0, 'end')
        filename = filedialog.askopenfilename(filetypes=(("Arquivos XLSX",".xlsx"),("Todos os Arquivos",".*")))
        entrada.insert(0, filename)

def GerarRelatorio():
    relatorio=filedialog.askdirectory()
    lbldialog.config()

    print('Analisando fonte, aguarde...')
    lbldialog.config(text='Análisando fonte, aguarde...')   
    
    conteudo = "/conteudo"
    pasta = relatorio + conteudo
    access_rights = 0o777
    try:
        os.mkdir(pasta, access_rights)
    except OSError:
        lbldialog2.config()
    else:
        print ("Pasta de conteúdo criada com sucesso!")

    original = './imgs/favicon.png'
    alvo = pasta + '/favicon.png'
    try:
        shutil.copyfile(original, alvo)
    except OSError:
        lbldialog2.config()
    else:
        lbldialog2.config()

    f = open(pasta + '/forma.css','w', encoding='utf-8')
    f.write(css_string)
    f.close()
    lbldialog2.config()
    
    try:shutil.copyfile(original, alvo)
    except OSError:lbldialog2.config()
    else:lbldialog2.config()   
    tabela_fnt = entrada1.get()
    try:
        lbldialog2.config(text='Verificando fonte...')
        fontes.validacao(relatorio, pasta, tabela_fnt)
        print("Verificando validação da fonte...")
    except FileNotFoundError:
        lbldialog2.config(text='Não foi possível verificar a fonte:\nUsuário não selecionou nada.')
        raise 
    else:
        lbldialog2.config(text='Fonte validada com sucesso.')
        print("Fonte validada com sucesso.")
        
    lbldialog.config(text='Análise concluída com sucesso!')
    print("Análise concluida com sucesso.")

    MsgBox = messagebox.askquestion ("Sucesso!", "Análise sem erros!\n\nSelecione ""'Sim'"" para abrir o relatório.")
    if MsgBox == 'yes':
        file_name = relatorio + "./análisecompleta_fonte.html"
        os.startfile (file_name)

janela = app_menu()
janela.root.mainloop()
