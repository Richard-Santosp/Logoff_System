from tkinter import *
from tkinter import font
from config import *
import platform

fundo = "#000000"
campo = '#000000'
botoes ='#1C1C1C'
fonte_cor = '#76b57c'

SO = platform.system()

if SO == "Windows":
    def encerrar_windows():
        root = Tk()
        root.title('Encerrar sistema Windows')
        root.resizable(False, False)
        root.configure(bg=fundo)

        fonte_label = font.Font(family='Sans', size='12',weight='bold')
        texto = Label(root, text='Em quanto tempo deseja que o sistema seja desligado?',width=44, height=3, bg=campo, font=fonte_label)
        texto.grid(row=0, column=0, columnspan=3, padx=2, pady=4)


        fonte_botoes = font.Font(family='Sans', size='11',weight='bold')
        times = [1800, 3600, 5400, 7200, 9000, 10800]
        timer_button = 30
        linha = 1
        coluna = 0
        for times_value in times:
            timer_logoff = Button(root, text= f'{format_number(timer_button)}', width=15, height=3, font=fonte_botoes,command=lambda t=times_value:logoff_windows(t), relief=RAISED, overrelief=RIDGE, bg=botoes, fg=fonte_cor)
            timer_logoff.grid(row=linha, column=coluna, padx=2, pady=4)
            timer_button += 30
            if coluna != 2:
                coluna += 1
            else:
                coluna = 0
                linha += 1

        botao_abortar = Button(root, text='Encerrar logoff',command=encerrar_logoff_windows, width=48, height=2, relief=RAISED, overrelief=RIDGE, bg=botoes, fg=fonte_cor, font=fonte_botoes)
        botao_abortar.grid(row=linha, column=0,columnspan=3, padx=2, pady=4)

        root.mainloop()

    encerrar_windows()
else:
    def encerrar_linux():
        root = Tk()
        root.title('Encerrar sistema Linux')
        root.resizable(False, False)
        root.configure(bg=fundo)

        fonte_label = font.Font(family='Sans', size='12',weight='bold')
        texto = Label(root, text='Em quanto tempo deseja que o sistema seja desligado?',width=44, height=3, bg=campo, font=fonte_label)
        texto.grid(row=0, column=0, columnspan=3, padx=2, pady=4)


        fonte_botoes = font.Font(family='Sans', size='11',weight='bold')
        times = [30, 60, 90, 120, 150, 180]
        timer_button = 30
        linha = 1
        coluna = 0
        for times_value in times:
            timer_logoff = Button(root, text= f'{format_number(timer_button)}', width=15, height=3, font=fonte_botoes,command=lambda t=times_value:logoff_linux(t), relief=RAISED, overrelief=RIDGE, bg=botoes, fg=fonte_cor)
            timer_logoff.grid(row=linha, column=coluna, padx=2, pady=4)
            timer_button += 30
            if coluna != 2:
                coluna += 1
            else:
                coluna = 0
                linha += 1

        botao_abortar = Button(root, text='Encerrar logoff',command=encerrar_logoff_linux, width=48, height=2, relief=RAISED, overrelief=RIDGE, bg=botoes, fg=fonte_cor, font=fonte_botoes)
        botao_abortar.grid(row=linha, column=0,columnspan=3, padx=2, pady=4)

        root.mainloop()

    encerrar_linux()