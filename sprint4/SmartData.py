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

    css_string = '''/* global */
/* ------------------------------------------------------------------------------------------------------------------- */
body {
    font-family: "Open Sans", Arial, Helvetica, sans-serif;
    padding: 0;
    margin: 0;
    background: #64d292;
} 
main {
    max-width: 100%;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    padding-bottom: 0.5px;
}
/* template's rules */
/* ------------------------------------------------------------------------------------------------------------------- */
.header {
    display: grid;
    grid-template-columns: 0.5fr 3fr;
    grid-template-areas: "sideMenu contentMenu";
    height: 50px;
    font-size: medium;
}
/* where the metalicts title goes */
.metalitcs {
    background: #112244;
    
    grid-area: sideMenu;
}
.metalitcs img {
    
    max-height:50px;
    width: auto;
    height: auto;
}
/* where left and rightbox goes */
.location {
    background: #112244;
    color: #ffffff;
    box-shadow: -10px 0px 10px 0.5px rgba(0, 0, 0, 0.1);
    grid-area: contentMenu;
}
.leftbox { 
    float:left;  
    background:#112244; 
    width:50%; 
    height: 50px; 
}
.leftbox p {
    padding: 5px;
    margin-left: 10px;
    text-aling:center;
}
.rightbox{ 
    float:left;  
    background:#112244;
    width: 50%;
    height: 50px;
    
} 
.rightbox p {
    padding: 5px;
    margin-left: 10px;
    text-aling:center;
}
/* side menu and page's content */
/* ------------------------------------------------------------------------------------------------------------------- */
/* where side menu and page's content goes*/
.container {
    grid-template-areas: "menu-col content-col";
    font-size: small;
    align-items: center;
}
/* for side menu only */
.container-menu-col {
    margin-top: 30px;
}
/* where divs goes */
.menu-col {
    height: 100%;
    font-weight: bold;
    grid-area: menu-col;
}
/* where page's content goes */
.container-content-col {
    height: 100%;
    overflow: hidden;
    grid-area: content-col;
}
/* dark blue divs */
.index {
    width: 100%;
    height: 50px;
    background: #112244;
    color: white;
    text-align: center;
    vertical-align: middle;
    line-height: 50px;
    box-shadow: 0px 1px 10px 0px rgba(0, 0, 0, 0.1), 0px -1px 10px 0px rgba(0, 0, 0, 0.1);
}
.index_two_rows p{
    width: 100%;
    height: 50px;
    background: #112244;
    color: white;
    text-align: center;
    vertical-align: middle;
    line-height: 15px;
    padding-top: 1rem;
    box-shadow: 0px 1px 10px 0px rgba(0, 0, 0, 0.1), 0px -1px 10px 0px rgba(0, 0, 0, 0.1);
}
/* light blue divs */
.stg-in {
    width: 100%;
    height: 50px;
    background: #3749E9;
    color: white;
    text-align: center;
    vertical-align: middle;
    line-height: 50px;
    box-shadow: 0px 1px 10px 0px rgba(0, 0, 0, 0.1), 0px -1px 10px 0px rgba(0, 0, 0, 0.1);
}
.stg-in:hover {
    background: rgba(116, 114, 115, 0.247);
    color: black;
}
/* white divs */
.stg {
    width: 100%;
    height: 50px;
    background: #ffffff;
    color: black;
    text-align: center;
    vertical-align: middle;
    line-height: 50px;
    box-shadow: 0px 1px 10px 0px rgba(0, 0, 0, 0.1), 0px -1px 10px 0px rgba(0, 0, 0, 0.1);
}
.stg:hover {
    background: rgba(116, 114, 115, 0.247);
}
/* rules for the graphs */
/* ------------------------------------------------------------------------------------------------------------------- */
.head {
    height: 40px;
    text-align: left;
    padding: 10px 0 0 10px;
    background: #112244;
}
/* inside of head*/
.title {
    font-size: 10pt;
    font-weight: bold;
    color: #ffffff;
}
/* inside of head*/
.paragraph {
    font-size: 7pt;
    color: #ffffff;
}
/* imported graphs */
iframe {
    width: 100%;
    height: 100%;
    border-radium: 5px;
}
.content {
    background: #ffffff;
    width: auto;
    height: 80%;
}
.table_value {
    font-size: 30pt;
    font-weight: bolder;
    color: #707070;
}
.table_content {
    background: #ffffff;
    width: auto;
    height: 80%;
    display: grid;
    justify-content: center;
    align-content: center;
}
.result_value {
    font-size: 12pt;
    font-weight: bolder;
    color: #707070;
}
.result_content {
    background: #ffffff;
    width: auto;
    height: 60%;
    display: grid;
    justify-content: center;
    align-content: center;
}
.indexMOD_value {
    font-size: 15pt;
    font-weight: bolder;
    color: #707070;
}
.indexMOD_content {
    background: #ffffff;
    width: auto;
    height: 60%;
    display: grid;
    justify-content: center;
    align-content: center;
}
/* graphs for grid */
/* the bonus graphs can be placed wherever you like to */
/* ------------------------------------------------------------------------------------------------------------------- */
.graph_one {
    background-color: #ffffff;
    grid-area: one;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_two {
    background-color: #ffffff;
    grid-area: two;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_three {
    background-color: #ffffff;
    grid-area: three;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_four {
    background-color: #ffff;
    grid-area: four;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_five {
    background-color: #ffffff;
    grid-area: five;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_six {
    background-color: #ffffff;
    grid-area: six;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_seven {
    background-color: #ffffff;
    grid-area: seven;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_eight {
    background-color: #ffffff;
    grid-area: eight;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_nine {
    background-color: #ffffff;
    grid-area: nine;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_ten {
    background-color: #ffffff;
    grid-area: ten;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_eleven {
    background-color: #ffffff;
    grid-area: eleven;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_twelve {
    background-color: #ffffff;
    grid-area: twelve;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_thirteen {
    background-color: #ffffff;
    grid-area: thirteen;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_fourteen {
    background-color: #ffffff;
    grid-area: fourteen;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_fifteen {
    background-color: #ffffff;
    grid-area: fifteen;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_sixteen {
    background-color: #ffffff;
    grid-area: sixteen;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_seventeen {
    background-color: #ffffff;
    grid-area: seventeen;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
.graph_eighteen {
    background-color: #ffffff;
    grid-area: eighteen;
    box-shadow: 30px 0px 40px rgba(0, 0, 0, 0.1), -30px 0px 40px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}
/* static and dynamic containers - no mediaquery*/
/* each page have it own container because of specific layout */
/* ------------------------------------------------------------------------------------------------------------------- */
/* static_graph_container is the same for all pages that requires it */
.static_graph_container_01 {
    display: grid;
    grid-template-columns: 1fr 1fr 3fr;
    grid-template-rows: 30vh 50vh 10vh;
    grid-gap: 20px;
    grid-template-areas: "one two three" 
                         "four four three";
    margin: 43px 50px 0px 50px;
}
.dynamic_graph_container_FNT {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 70vh 70vh 70vh 70vh;
    grid-gap: 20px;
    grid-template-areas: "one two" 
                         "three three"
                         "four five" 
                         "six seven";
    margin: -60px 50px 50px 50px;
}
.dynamic_graph_container_MVT {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 30vh 30vh 30vh 30vh;
    grid-gap: 10px;
    grid-template-areas: "one two"
                         "one three" 
                         "four three"
                         "four three";
    margin: -60px 50px 50px 50px;
}
.dynamic_graph_container_OPR {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 30vh 30vh 30vh 30vh;
    grid-gap: 10px;
    grid-template-areas: "one two"
                         "one three" 
                         "four three"
                         "four three";
    margin: -60px 50px 50px 50px;
}
.dynamic_graph_container_PGT {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 30vh 30vh 30vh 30vh;
    grid-gap: 10px;
    grid-template-areas: "one two"
                         "one three" 
                         "four three"
                         "four three";
    margin: -60px 50px 50px 50px;
}
.static_graph_container_02 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
    grid-template-rows: 20vh;
    grid-gap: 10px;
    grid-template-areas: "one two three four five";
    margin: 43px 50px 0px 50px;
}
.dynamic_graph_container_result_MVT {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    grid-template-rows: 80vh 80vh 80vh 80vh 80vh;
    grid-gap: 10px;
    grid-template-areas:
                         "one one one one"
                         "two two two two"
                         "three three three three"
                         "four four four four"
                         "five five five five";
    margin: 10px 50px 50px 50px;
}
.dynamic_graph_container_result_OPR {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 80vh 80vh 80vh 80vh 80vh;
    grid-gap: 10px;
    grid-template-areas: "one one two"
                         "three three three"
                         "four four four"
                         "five five five"
                         "six six six";
    margin: 10px 50px 50px 50px;
}
.static_graph_container_03 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    grid-template-rows: 20vh;
    grid-gap: 10px;
    grid-template-areas: "one two three four";
    margin: 43px 50px 0px 50px;
}
.dynamic_graph_container_result_PGT {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    grid-template-rows: 80vh 50vh 80vh 80vh 80vh 80vh 80vh;
    grid-gap: 10px;
    grid-template-areas: "one one one one"
                         "two two three three"
                         "four four four four"
                         "five five five five"
                         "six six six six"
                         "seven seven seven seven"
                         "eight eight eight eight";
    margin: 10px 50px 50px 50px;
}
.dynamic_graph_container_index_MOD {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 0.5fr;
    grid-template-rows: 20vh 30vh 30vh 30vh 20vh 30vh 30vh 30vh 20vh 30vh 30vh 30vh;
    grid-gap: 10px;
    grid-template-areas: "one two three four four"
                         "five five five four four"
                         "five five five six six"
                         "five five five six six"
                         
                         "seven eight nine ten ten"
                         "eleven eleven eleven ten ten"
                         "eleven eleven eleven twelve twelve"
                         "eleven eleven eleven twelve twelve"
                         
                         "thirteen fourteen fifteen sixteen sixteen"
                         "seventeen seventeen seventeen sixteen sixteen"
                         "seventeen seventeen seventeen eighteen eighteen"
                         "seventeen seventeen seventeen eighteen eighteen";
    margin: 43px 50px 50px 50px;
}
.dynamic_graph_container_index_MOD .title {
    font-size: 8pt;
}
.dynamic_graph_container_index_FaixaVAL {
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 100vh 180vh;
    grid-gap: 10px;
    grid-template-areas: "one"
                         "two";
    margin: 43px 50px 50px 50px;
}
'''

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
