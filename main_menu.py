import os
import glob
import tkinter as tk
from tkinter import ttk
from analyze import scanForImports
#X:\CLINICAL\DENTAL\QuickNotes



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # the chosen path of operation
        self._path = "C\\:Users\\ewilcox\\QuickNotes\\QuickNotes-v1.2"
        # config for root win
        self.title('Script Select')
        self.geometry('415x400')
        self.iconbitmap('app/images/tooth_2.ico')

        # widgets
        self.lbl = ttk.Label(self,text='Select a Script')
        self.lbl.grid(row=0,column=0)

        self.script_field = ttk.Entry(width=55)
        self.script_field.place(x=15,y=205)

        #self.continue_img = tk.PhotoImage(file='C:/Users/Ethan/PycharmProjects/Word ERD/edr-images/continue.png')
        self.acpt_scpt_button = ttk.Button(self, width=7, text='Load')

        # script loader button
        self.acpt_scpt_button['command'] = self.button_clicked
        self.acpt_scpt_button.place(x=360,y=203)

        self.listbox = tk.Listbox(self,width=65)
        self.listbox.bind('<Double-1>', self.display_sel)
        self.sb = ttk.Scrollbar(self)
        self.listbox.grid(row=1,column=0)
        self.sb.grid(row=1,column=1,sticky='ns')

        self.listbox.config(yscrollcommand=self.sb.set)
        self.sb.config(command=self.listbox.yview)
        # button to run the script gen program
        self.run_gen_button = ttk.Button(self, text='Load')
        self.run_gen_button['command'] = self.run_gen

        self.get_scripts()


    def display_sel(self,event=None):
        for i in self.listbox.curselection():
            text = self.listbox.get(i)
            self.script_field.delete(0,tk.END)
            self.script_field.insert(0,text)

    def button_clicked(self):
        for i in self.listbox.curselection():
            selected_file = self.listbox.get(i)
            self.load_script(selected_file)


    def load_script(self, file):
        path = 'C:\\Users\\ewilcox\\QuickNotes\\QuickNotes-v1.2\\app\\EDR-scripts'
        os.chdir(path)
        check_file = scanForImports(file+'.py')
        if check_file == True:
            # return to the user that this file isnt secure
            print('File not secure')
        elif check_file == False:
            os.system(f'python {file}.py')

    def run_gen(self):
        path = self._path
        os.chdir(path)
        os.system('python new_script_gen.py')

    def add_items(self, items, box):
        # add items to listbox
        cnt = 0
        for i in range(len(items)):
            box.insert(tk.END,items[cnt].replace('.py',''))
            cnt += 1

    def get_scripts(self):
        # gets a list of python edr note files for the listbox
        path = self._path + '\\app\\EDR-scripts'
        os.chdir(path)
        script_files = []
        for file in glob.glob("*.py"):
            script_files.append(file)
        self.add_items(script_files, self.listbox)



if __name__ == '__main__':
    app = App()
    app.mainloop()
