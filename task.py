from tkinter import *
from tkinter import messagebox
from random import randint

a = []

def mas():
    n = edit1.get()
    if not n:
        messagebox.showerror('Помилка', 'Розмірність масиву не вказана')
        return

    try:
        n = int(n)
    except ValueError:
        messagebox.showerror('Помилка', 'Введіть ціле число')
        return

    a.clear()
    listbox1.delete(0, END)
    listbox2.delete(0, END)

    for i in range(n):
        a.append(randint(-50, 50))
        listbox1.insert(END, a[i])
    label4['text'] = 'Результат:'

def sort():
    n = len(a)
    for j in range(n - 1):
        for i in range(n - j - 1):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]

    listbox2.delete(0, END)
    for i in range(n):
        listbox2.insert(END, a[i])

        if a[i] < 0:
            listbox2.itemconfig(i, {'fg': 'red'})
        elif a[i] > 0:
            listbox2.itemconfig(i, {'fg': 'green'})
        else:
            listbox2.itemconfig(i, {'fg': 'blue'})

def count_unique():
    unique_count = len(set(a))
    label4['text'] = f'Кількість різних чисел: {unique_count}'

def about_author():
    messagebox.showinfo('Про автора', 'Автор: Бичко Даша\nЕлектронна пошта: bychko.dasha6@gmail.com')

def problem_statement():
    messagebox.showinfo('Умова задачі', 'Знайти кількість різних чисел масиву. Виконати сортування за спаданням (метод обміну).')

def set_light_theme():
    root.config(bg='lightgray')
    for widget in (label1, label2, label3, label4, listbox1, listbox2, edit1):
        widget.config(bg='lightgray', fg='black')
    listbox1.config(bg='white')
    listbox2.config(bg='white')
    edit1.config(bg='white')

def set_dark_theme():
    root.config(bg='black')
    for widget in (label1, label2, label3, label4, listbox1, listbox2, edit1):
        widget.config(bg='black', fg='white')
    listbox1.config(bg='gray80')
    listbox2.config(bg='gray80')
    edit1.config(bg='gray80')

def set_default_theme():
    root.config(bg='#F0F0F0')
    for widget in (label1, label2, label3, label4, listbox1, listbox2, edit1):
        widget.config(bg='#F0F0F0', fg='black')
    listbox1.config(bg='white')
    listbox2.config(bg='white')
    edit1.config(bg='white')

def do_popup(event):
    popupmenu.post(event.x_root, event.y_root)

# Головне вікно
root = Tk()
root.title('Масиви')
root.geometry('600x300')

label1 = Label(text='Вихідний масив')
label2 = Label(text='Посортований масив')
label1.place(x=20, y=30)
label2.place(x=200, y=30)

listbox1 = Listbox(height=10, width=20)
listbox2 = Listbox(height=10, width=20)
listbox1.place(x=20, y=70)
listbox2.place(x=200, y=70)

label3 = Label(text='Кількість елементів масиву:')
label3.place(x=400, y=30)

edit1 = Entry()
edit1.place(x=400, y=70)

button1 = Button(text='Заповнити', width=20, command=mas)
button1.place(x=400, y=100)

button2 = Button(text='Сортувати', width=20, command=sort)
button2.place(x=400, y=130)

button3 = Button(text='Знайти кількість різних', width=20, command=count_unique)
button3.place(x=400, y=160)

label4 = Label(text='Результат:')
label4.place(x=400, y=210)

# Меню
main_menu = Menu(root)
root.config(menu=main_menu)

array_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Дії з масивом', menu=array_menu)
array_menu.add_command(label='Заповнити', command=mas)
array_menu.add_command(label='Сортувати', command=sort)
array_menu.add_command(label='Кількість різних', command=count_unique)

about_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Про програму', menu=about_menu)
about_menu.add_command(label='Про автора', command=about_author)
about_menu.add_command(label='Умова задачі', command=problem_statement)

popupmenu = Menu(root, tearoff=0)
popupmenu.add_command(label="Світлий", command=set_light_theme)
popupmenu.add_command(label="Темний", command=set_dark_theme)
popupmenu.add_command(label="Відновити початкові кольори", command=set_default_theme)
root.bind("<Button-3>", do_popup)

root.mainloop()
