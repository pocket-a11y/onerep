from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import filedialog

window = Tk()
window.title('Коротеев Андрей Денисович')
window.geometry('666x444')

vkladki = ttk.Notebook()

tab1 = ttk.Frame(vkladki)
tab2 = ttk.Frame(vkladki)
tab3 = ttk.Frame(vkladki)

vkladki.add(tab1, text='Калькулятор')
vkladki.add(tab2, text='Чекбоксы')
vkladki.add(tab3, text='Работа с текстом')


# Логика
def Kalc():
    num1 = float(ent1.get())
    num2 = float(ent2.get())
    operation = oper_combo.get()

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Ошибка: На 0 делить нельзя'

    result_lbl1.config(text='Ответ: ' + str(result))


def Check():
    selected_options = ""
    if check1.get():
        selected_options += 'Вы выбрали Первый вариант\n'
    if check2.get():
        selected_options += 'Вы выбрали Второй вариант\n'
    if check3.get():
        selected_options += 'Вы выбрали Третий вариант\n'

    messagebox.showinfo('Выбранные чеки', selected_options)


def File_save():
    text = Entry_file.get()
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        with open(filepath, "w") as file:
            file.write(text)


# Калькулятор
lbl1 = Label(tab1, text='Введите первое число: ')
lbl1.grid(row=0, column=0)
ent1 = Entry(tab1)
ent1.grid(row=0, column=1)

lbl2 = Label(tab1, text='Введите второе число: ')
lbl2.grid(row=1, column=0)
ent2 = Entry(tab1)
ent2.grid(row=1, column=1)

oper_combo = Combobox(tab1)
oper_combo['values'] = ['+', '-', '*', '/']
oper_combo.current(0)
oper_combo.grid(row=2, column=0)

button_of_Kalc = Button(tab1, text='Посчитать', command=Kalc)
button_of_Kalc.grid(row=2, column=1)

result_lbl1 = Label(tab1, text='Ответ: ')
result_lbl1.grid(row=3, columnspan=2)

# Чекбоксы
check1 = IntVar()
check2 = IntVar()
check3 = IntVar()

checkbox1 = Checkbutton(tab2, text='Первый', variable=check1)
checkbox1.grid(row=0, sticky=W)
checkbox2 = Checkbutton(tab2, text='Второй', variable=check2)
checkbox2.grid(row=1, sticky=W)
checkbox3 = Checkbutton(tab2, text='Третий', variable=check3)
checkbox3.grid(row=2, sticky=W)

show_btn = Button(tab2, text='Показать выбор', command=Check)
show_btn.grid(row=3)

# Работа с файлом
Label_file = Label(tab3, text='Введите текст')
Label_file.grid(column=0, row=0)
Entry_file = Entry(tab3)
Entry_file.grid(column=1, row=0)

open_btn = Button(tab3, text='Открыть файл', command=File_save)
open_btn.grid(column=0, row=1)

vkladki.pack(expand=1, fill='both')

window.mainloop()