import tkinter
from tkinter import ttk

class Script:
    def __init__(self,title):
        self.title = title
        self.script_entries = []
        self.var_blocks = []
        self.obj_list = []
        self.intro = 'def clear_view():\n' \
            '    for widget in viewField.winfo_children():\n' \
            '        widget.pack_forget()\n'

        self.open_line = 'def open_master(index):\n' \
                         '    func_field_index[index]()\n'

        self.place_line = 'def place_buttons():\n' \
                          '    counter = 0\n' \
                          '    x_pos = 10\n' \
                          '    y_pos = 30\n' \
                          '    for ent in range(len(entryButtons)):\n' \
                          '        entryButtons[counter].place(x=x_pos,y=y_pos)\n' \
                          '        counter = counter + 1\n' \
                          '        y_pos = y_pos + 30\n'

        self.add_items_line = 'def add_items(items,myListbox):\n' \
                              '    counter = 0\n' \
                              '    for i in range(len(items)):\n' \
                              '        myListbox.insert(END, items[counter])\n' \
                              '        counter = counter + 1\n'

        self.save_line_p2 = "    final_doc = text_box.get(1.0, END)\n" \
                            "    doc.add_paragraph(final_doc)\n" \
                            "    doc.save(f'C:/QuickNotes/Notes/{FILE_NAME}.docx')\n" \
                            "    print('File saved')\n" \
                            "root = Tk()\n" \
                            "menu = Menu(root)\n" \
                            "root.config(menu=menu)\n" \
                            "file = Menu(menu,tearoff=0)\n" \
                            "file.add_command(label='Extraction')\n" \
                            "menu.add_cascade(label='File',menu=file)\n" \
                            "edit = Menu(menu,tearoff=0)\n" \
                            "edit.add_command(label='Save ctrl+s',command=save_to_file)\n" \
                            "menu.add_cascade(label='Edit',menu=edit)\n" \
                            "viewField = LabelFrame(root,text='viewport',height=200,width=170)\n" \
                            "viewField.place(x=105,y=10)\n" \
                            "editor_frame = Frame(height=100,width=100, relief=RAISED, borderwidth=1)\n" \
                            "editor_frame.place(x=300,y=280)\n" \
                            "text_scroll = Scrollbar(editor_frame)\n" \
                            "text_scroll.pack(side=RIGHT,fill=Y)\n" \
                            "text_box = Text(editor_frame,height=10,width=45,font=('Helvetica',11),undo=True,selectbackground='blue',selectforeground='white',yscrollcommand=text_scroll.set)\n" \
                            "text_box.pack()\n" \
                            "text_scroll.config(command=text_box.yview)\n\n" \

        self.save_line_p3 = "def master_accept(event=None):\n" \
                            "    global index_num\n" \
                            "    print(menu_index[index_num].winfo_class())\n" \
                            "    if menu_index[index_num].winfo_class() == 'Listbox':\n" \
                            "        selected_text_list = [menu_index[index_num].get(i) for i in menu_index[index_num].curselection()]\n" \
                            "        text_box.insert(END, paras_index[index_num].get(selected_text_list[0]))\n" \
                            "        values_index[index_num].append(selected_text_list)\n" \
                            "        print(values_index[index_num])\n" \
                            "    index_num = index_num + 1\n" \
                            "    print(index_num)\n" \
                            "    if index_num == len(menu_index):\n" \
                            "        index_num = 0\n" \
                            "    open_master(index_num)\n\n" \
                            "def delete_last_entry():\n" \
                            "    global index_num\n" \
                            "    values_index[index_num].pop()\n" \
                            "    print(values_index[index_num])\n" \
                            "saveButton = Button(text='OK', width=6,command=save_to_file)\n" \
                            "saveButton.place(x=580,y=565)\n" \
                            "default = Listbox(viewField,height=12,width=30)\n" \
                            "default.pack()\n" \
                            "place_buttons()\n" \
                            "master_accept_button = Button(viewField,text='Accept',command=master_accept)\n" \
                            "delete_button = Button(viewField,text='Delete',command=delete_last_entry)\n" \
                            "index_num = 0\n" \
                            "open_master(index_num)\n" \
                            "root.geometry('700x600')\n" \
                            "root.mainloop()"

        self.openFunctions = ['from tkinter import *', 'import docx', 'from datetime import datetime',"\n",
                         f"SCRIPT_NAME = '{self.title}'", '\n', "CURRENT_DATE = datetime.now().strftime('%Y-%m-%d %H:%M:%S')",
                         '\n', "FILE_NAME = SCRIPT_NAME + '-' + CURRENT_DATE", '\n', "doc = docx.Document()", '\n',
                         'all_paras = doc.paragraphs', '\n', self.intro, '\n', self.open_line, '\n', self.place_line, '\n',
                         self.add_items_line, '\n']
        self.body = []

    # topics and their items data will be saved here as a subclass
    class TkObj:
        def __init__(self, name, obj_type):
            self.name = name
            self.obj_type = obj_type
            self.items = [] # items for a topic(entry)
            self.paras = [] # topic lines/paragraphs for each item
            # add pre selection script line and post selection script line

        def gen_items(self): # when more than 1 listbox is created the element is in self.items is shared. when print(self.items) after 1st it is called twice more
            tracker = len(self.paras)
            while True:
                opt = input(f'Add item to {self.name}: (type stop to exit)')
                opt = opt.replace(opt[0],opt[0].upper())
                print(opt)
                opt2 = input(f'Add topic line to {self.name} (type stop again to exit)')
                opt2 = opt2.replace(opt2[0], opt2[0].upper())
                print(opt2)
                if opt == 'stop':
                    break
                else:
                    if tracker >= 2:
                        opt2 = " " + opt2
                    self.items.append(opt)
                    self.paras.append(opt2)
            print(self.items)
            print(self.paras)

    def gen_entry_func(self):
        counter = 0
        entries_length = len(self.script_entries)

        for i in range(entries_length):
            func_block = f"def open_{self.script_entries[counter]}():\n" \
                         f"clear_view()\n" \
                         f"global index_num\n" \
                         f"index_num = {self.script_entries.index(self.script_entries[counter])}\n" \
                         f"{self.script_entries[counter]}_lbl.pack()\n" \
                         f"{self.script_entries[counter]}_listbox.pack()\n" \
                         f"master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)" + "\n" \
                         f"delete_button.pack(side=RIGHT, expand=TRUE, fill=X)\n" \
                         f"{self.script_entries[counter]}_listbox.bind('<Double-1>', master_accept)\n"
            func_block = func_block.replace('\n', '\n    ')
            self.openFunctions.append(func_block)
            self.openFunctions.append('\n')
            counter += 1


    def gen_var_block(self):
        cnt = 0
        dur = len(self.script_entries) - 1
        for i in range(len(self.script_entries)):
            p_cnt = 0
            para_block = f'{self.script_entries[cnt]}_paras = ~"{self.obj_list[cnt].items[p_cnt]}":"{self.obj_list[cnt].paras[p_cnt]}"'
            para_block = para_block.replace('~', '{')
            for i in range(len(self.obj_list[cnt].paras)-1):
                p_cnt += 1
                para_block = para_block + f',"{self.obj_list[cnt].items[p_cnt]}":"{self.obj_list[cnt].paras[p_cnt]}"'

            para_block = para_block + '}'
            var_block_list = f"{self.script_entries[cnt]}_items = {self.obj_list[cnt].items}"
            var_block = f"{self.script_entries[cnt]}_button = Button(text='{self.script_entries[cnt]}',command=open_{self.script_entries[cnt]},width=10)\n" \
                        f"{self.script_entries[cnt]}_listbox = Listbox(viewField,selectmode='single',width=30,height=12)\n" \
                        + var_block_list + '\n' \
                        f"{self.script_entries[cnt]}_entry = Entry()\n" \
                        f"{self.script_entries[cnt]}_lbl = Label(viewField,text='{self.script_entries[cnt]}')\n" \
                        f"add_items({self.script_entries[cnt]}_items,{self.script_entries[cnt]}_listbox)\n" \
                        f"{self.script_entries[cnt]}_values = []\n" \
                        + para_block + '\n'
            self.body.append(var_block)
            self.body.append('\n')
            cnt += 1

        cnt = 0 # below is to create and append the buttons list line to body
        buttons_list_line = f"entryButtons = [{self.script_entries[cnt]}_button"
        for i in range(dur):
            cnt += 1
            buttons_list_line = buttons_list_line + f",{self.script_entries[cnt]}_button"
        buttons_list_line = buttons_list_line + "]"
        self.body.append(buttons_list_line)
        self.body.append('\n')

        cnt = 0
        entry_list_line = f"entryFields = [{self.script_entries[cnt]}_entry"
        for i in range(dur):
            cnt += 1
            entry_list_line = entry_list_line + f",{self.script_entries[cnt]}_entry"

        entry_list_line = entry_list_line + ']'
        self.body.append(entry_list_line)
        self.body.append('\n')

        # below creates and appends the values, paras, and menu index lines to body
        cnt = 0
        menu_index_line = f"menu_index = [{self.script_entries[cnt]}_{self.obj_list[cnt].obj_type}"
        values_index_line = f"values_index = [{self.script_entries[cnt]}_values"
        paras_index_line = f"paras_index = [{self.script_entries[cnt]}_paras"

        for i in range(dur):
            cnt += 1
            menu_index_line = menu_index_line + f",{self.script_entries[cnt]}_{self.obj_list[cnt].obj_type}"
            values_index_line = values_index_line + f",{self.script_entries[cnt]}_values"
            paras_index_line = paras_index_line + f",{self.script_entries[cnt]}_paras"

        menu_index_line = menu_index_line + "]"
        values_index_line = values_index_line + "]"
        paras_index_line = paras_index_line + "]"
        self.body.append(menu_index_line)
        self.body.append('\n')
        self.body.append(values_index_line)
        self.body.append('\n')
        self.body.append(paras_index_line)
        self.body.append('\n')
        # below appends the open function index line to body
        cnt = 0
        func_index_line = f"func_field_index = [open_{self.script_entries[cnt]}"
        for i in range(dur):
            cnt += 1
            func_index_line = func_index_line + f",open_{self.script_entries[cnt]}"
        func_index_line = func_index_line + ']'
        self.body.append(func_index_line)
        self.body.append('\n')

    def obj_data(self):
        cnt = 0
        for i in range(len(self.script_entries)): # gets input to create an entry subclass for each given entry
            opt = 'listbox'
            self.obj_list[cnt] = self.TkObj(self.script_entries[cnt], opt)
            cnt += 1

        obCnt = 0
        for i in range(len(self.obj_list)): # gets input for items for each listbox Tk object subclass
            if self.obj_list[obCnt].obj_type == 'listbox':
                self.obj_list[obCnt].gen_items()
            else:
                pass
            obCnt += 1

    def create_script(self):
        while True:
            new = input("Do you want to add a new topic? y/n")
            if new == 'y':
                an_entry = input("Type topic name:")
                an_entry = an_entry.replace(an_entry[0], an_entry[0].upper())
                print(an_entry)
                self.script_entries.append(an_entry)
                self.obj_list.append(an_entry)
            elif new == 'n':
                print('saving...')
                break
            else:
                print('I only accept y/n')

        self.obj_data()
        self.write_to_file()

    def write_to_file(self):
        self.gen_entry_func()
        cnt = 0
        for i in range(len(self.openFunctions)):
            self.body.append(self.openFunctions[cnt])
            self.body.append('\n')
            cnt += 1
        cnt = 0
        self.body.append('def save_to_file(event=None):')
        self.body.append('\n')
        self.body.append(self.save_line_p2)
        self.body.append('\n')
        self.gen_var_block() # writes the tkinter object declaration blocks to body
        self.body.append(self.save_line_p3)
        self.body.append('\n')


# write a new script
def start_script():
    title = input('Name of new script:')
    new_script = Script(title)
    print('Creating new script..')
    new_script.create_script()
    file = open(f'C:/EDR-scripts/{new_script.title}_script.py', 'w')
    file.writelines(new_script.body)
    file.close()


start_script()
