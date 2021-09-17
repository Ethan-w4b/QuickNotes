from tkinter import *


def clear_view():
    for widget in viewField.winfo_children():
        widget.pack_forget()
    


def open_master(index):
    func_field_index[index]()


def place_buttons():
    counter = 0
    x_pos = 10
    y_pos = 10
    for ent in range(len(entryButtons)):
        entryButtons[counter].place(x=x_pos,y=y_pos)
        entryFields[counter].place(x=90,y=y_pos)
        counter = counter + 1
        y_pos = y_pos + 30
    


def add_items(items,myListbox):
    counter = 0
    for i in range(len(items)):
        myListbox.insert(END, items[counter])
        counter = counter + 1


def open_consent():
    clear_view()
    global index_num
    index_num = 0
    consent_lbl.pack()
    consent_listbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)
    consent_listbox.bind('<Double-1>', master_accept)


def open_tooth():
    clear_view()
    global index_num
    index_num = 1
    tooth_lbl.pack()
    tooth_listbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)
    tooth_listbox.bind('<Double-1>', master_accept)


def open_provider():
    clear_view()
    global index_num
    index_num = 2
    provider_lbl.pack()
    provider_listbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)
    provider_listbox.bind('<Double-1>', master_accept)


def save_to_file(event=None):
    consent_line = f'Conset -  {consent_values}'
    tooth_line = f'Teeth -  Tooth {tooth_values}'
    provider_line = f'Provider -  Dental car provided by, {provider_values}'
    edr_list = [consent_line,tooth_line,provider_line]
    bad_chars = ['[',']']
    chosen_list = []
    counter = 0
    for i in range(len(edr_list)):
        if len(values_index[counter]) == 0:
            print('empty')
        elif values_index[counter] == ['']:
            print('empty')
        elif values_index[counter] == [[]]:
            print('empty')
        else:
            chosen_list.append(edr_list[counter])
        counter += 1
    newFile = open('EDR.txt','w')
    newFile.writelines(chosen_list)
    newFile.close()
    newFile = open('EDR.txt','r')
    final_doc = newFile.read()
    final_doc = ''.join(i for i in final_doc if not i in bad_chars)
    newFile.close()
    newFile = open('EDR.txt','w')
    newFile.write(final_doc)
    newFile.close()
    print('File saved')

root = Tk()
menu = Menu(root)
root.config(menu=menu)
file = Menu(menu,tearoff=0)
file.add_command(label='Extraction')
menu.add_cascade(label='File',menu=file)
edit = Menu(menu,tearoff=0)
edit.add_command(label='Save ctrl+s',command=save_to_file)
menu.add_cascade(label='Edit',menu=edit)
viewField = LabelFrame(root,text='viewport',height=200,width=170)
viewField.place(x=275,y=10)

consent_button = Button(text='consent',command=open_consent,width=10)
consent_listbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
consent_items = ['yes', 'no']
consent_entry = Entry()
consent_lbl = Label(viewField,text='consent')
add_items(consent_items,consent_listbox)
consent_values = []

tooth_button = Button(text='tooth',command=open_tooth,width=10)
tooth_listbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
tooth_items = ['a', 'b', 'c']
tooth_entry = Entry()
tooth_lbl = Label(viewField,text='tooth')
add_items(tooth_items,tooth_listbox)
tooth_values = []

provider_button = Button(text='provider',command=open_provider,width=10)
provider_listbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
provider_items = ['Bob', 'Dud', 'Dan']
provider_entry = Entry()
provider_lbl = Label(viewField,text='provider')
add_items(provider_items,provider_listbox)
provider_values = []

entryButtons = [consent_button,tooth_button,provider_button]
entryFields = [consent_entry,tooth_entry,provider_entry]
menu_index = [consent_listbox,tooth_listbox,provider_listbox]
values_index = [consent_values,tooth_values,provider_values]
func_field_index = [open_consent,open_tooth,open_provider]
def master_accept(event=None):
    global index_num
    print(menu_index[index_num].winfo_class())
    if menu_index[index_num].winfo_class() == 'Listbox':
        selected_text_list = [menu_index[index_num].get(i) for i in menu_index[index_num].curselection()]
        values_index[index_num].append(selected_text_list)
        print(values_index[index_num])
    else:
        single_text = menu_index[index_num].get()
        values_index[index_num].append(single_text)
        print(values_index[index_num])
    index_num = index_num + 1
    print(index_num)
    if index_num == len(menu_index):
        index_num = 0
    open_master(index_num)
def delete_last_entry():
    global index_num
    values_index[index_num].pop()
    print(values_index[index_num])
saveButton = Button(text='OK', width=6,command=save_to_file)
saveButton.place(x=275,y=310)
default = Listbox(viewField,height=12,width=30)
default.pack()
place_buttons()
master_accept_button = Button(viewField,text='Accept',command=master_accept)
root.bind('<Control_L>',master_accept)
root.bind('<Control-s>',save_to_file)

delete_button = Button(viewField,text='Delete',command=delete_last_entry)
index = 0
root.geometry('500x500')
root.mainloop()
