import pandas as pd

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.constants import W


class Janela:
    """
    This class is used to transform a csv file into txt. 
    Output file (.txt) path will be the same to the initial file (.csv).
    ...
    Methods
    -------
    No methods available.
    """
    
    def __init__(self):
        
        self.root = Tk()
        self.root.geometry('245x80+450+150')
        self.root.title("Transformação de Arquivo")

        self.Frame1 = Frame(self.root, bg='white', bd=2, relief=RIDGE).grid()
        self.Frame2 = Frame(self.Frame1, bd=2).grid(row=1, column=0, columnspan=4, sticky=W)

        self.w = Label(self.Frame1,)
        self.w.grid(row=0, column=0)

        self.__create_button(color_background='red', text='Transformar', coluna=0, comando=self.__openfile)
        self.__create_button(color_background='red', text='Sair', coluna=1, comando=self.__exit)

        self.root.mainloop()

    def __exit(self):
        self.result = messagebox.askquestion('Test Program', 'Would you like to exit?')
        if self.result == 'yes':
            self.root.destroy()

    def __openfile(self):
        self.root.filename = filedialog.askopenfilename(
            title='Select a file',
            filetypes=(
                ("csv files", "*.csv"), 
                ("all files", "*.*")
                )
            )
        if self.root.filename.endswith('.csv'):
            df = pd.read_csv(str(self.root.filename))
            path = str(self.root.filename)[:-4] + '.txt'
            df.to_csv(path, header=None, index=None, mode='a')
            messagebox.showinfo('Test Program', '.txt file was successfully generated!')
            
    def __create_button(self, color_background, text, coluna, comando=None):
        return Button(
            self.Frame2, 
            padx=1, 
            pady=1, 
            bd=2, 
            fg='black', 
            font=('arial', 11, 'bold'), 
            command=comando,
            width=12, 
            bg=color_background, 
            text=text
            ).grid(row=1, column=coluna)

if __name__ == "__main__":
    Janela()