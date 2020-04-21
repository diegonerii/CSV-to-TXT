import csv
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.constants import W


root = Tk()
root.geometry('470x360+450+150')
root.title("Transformação de Arquivo")


Frame1 = Frame(root, bg='white', bd=2, relief=RIDGE)
Frame1.grid()

Frame2 = Frame(Frame1, bd=2)
Frame2.grid(row=1, column=0, columnspan=4, sticky=W)


imagem = PhotoImage(file='C:/Users/diego.neri/Pictures/revemarr.png')
w = Label(Frame1, image=imagem)
w.imagem = imagem
w.grid(row=0, column=0)


def exit():
    result = messagebox.askquestion('TI - Revemar', 'Deseja realmente sair?')
    if result == 'yes':
        root.destroy()
        return


def openfile():
    text_list = []
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/diego.neri/Documents/", title='Selecione o Arquivo',
                                               filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    if root.filename.endswith('.csv'):
        with open("C:/Users/diego.neri/Documents/teste.txt", "w") as outputfile:
            with open(root.filename, 'r') as inputfile:
                [outputfile.write(" ".join(row) + '\n') for row in csv.reader(inputfile)]
            outputfile.close()
            print(root.filename)
            messagebox.showinfo('TI - Revemar', 'Arquivo txt gerado com sucesso!')
    """elif:
            messagebox.showinfo("Erro de Visualização", 'Tipo de arquivo deve ser .csv')"""


def create_buttom(nome, color_background, text, coluna, comando):
    nome = Button(Frame2, padx=1, pady=1, bd=2, fg='black', font=('arial', 11, 'bold'), command=comando,
                  width=12, bg=color_background, text=text).grid(row=1, column=coluna)


create_buttom('Abrir', 'red', 'Transformar', 0, openfile)
create_buttom('Sair', 'red', 'Sair', 1, exit)


root.mainloop()
