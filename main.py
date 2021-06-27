from tkinter import *


class Table(object):
    def __pack(self):
        for item in range(len(self.__check)):
            self.__check[item].grid(row=item, column=0, sticky=NSEW)
            self.__id[item].grid(row=item, column=1, ipadx=5, sticky=NSEW)
            self.__oper[item].grid(row=item, column=2, ipadx=5, sticky=NSEW)
            self.__client[item].grid(row=item, column=3, ipadx=5, sticky=NSEW)
            self.__type[item].grid(row=item, column=4, ipadx=5, sticky=NSEW)
            self.__amount[item].grid(row=item, column=5, ipadx=5, sticky=NSEW)
            self.__comment[item].grid(row=item, column=6, columnspan=2, ipadx=5, sticky=NSEW)

        self.__table.grid_columnconfigure(0, minsize=10)
        self.__table.grid_columnconfigure(1, minsize=10)
        self.__table.grid_columnconfigure(2, minsize=150)
        self.__table.grid_columnconfigure(3, minsize=150)
        self.__table.grid_columnconfigure(4, minsize=70)
        self.__table.grid_columnconfigure(5, minsize=70)
        self.__table.grid_columnconfigure(6, weight=1)

    def __add(self, idNum, oper, client, typeDeal, amount, comment, new_dialog):
        self.add(idNum, 'Зубенко Михаил Григорьевич', client, typeDeal, amount, comment)
        new_dialog.destroy()

    def new(self):
        new_dialog = Toplevel(self.__master)
        new_dialog.title("Добавить запись о сделке")

        Label(new_dialog, text="id:").grid(row=0, column=0, padx=3, pady=3)
        _id = Entry(new_dialog)
        _id.grid(row=0, column=1, padx=3, pady=3, sticky=EW)

        Label(new_dialog, text="Клиент:").grid(row=1, column=0, padx=3, pady=3)
        client = StringVar()
        client.set("Чапарян В.У.")
        OptionMenu(new_dialog, client, 'Чапарян В.У.',
                   'ООО "Заря"',
                   'Витальченко И.А.',
                   'Рогожин В.Р.',
                   'ОАО "Кошелев"').grid(row=1, column=1, padx=3, pady=3, sticky=EW)

        Label(new_dialog, text="Тип сделки:").grid(row=2, column=0, padx=3, pady=3)
        _type = StringVar()
        _type.set("Застройка")
        OptionMenu(new_dialog, _type, 'Застройка',
                   'Отделка',
                   'Покупка',
                   'Планирование').grid(row=2, column=1, padx=3, pady=3, sticky=EW)

        Label(new_dialog, text="Сумма:").grid(row=3, column=0, padx=3, pady=3)
        amount = Entry(new_dialog)
        amount.grid(row=3, column=1, padx=3, pady=3, sticky=EW)

        Label(new_dialog, text="Коментарий").grid(row=4, column=0, padx=3, pady=3)
        comment = Text(new_dialog, width=25, height=15)
        comment.grid(row=4, column=1, padx=3, pady=3, )

        Button(new_dialog, text='Добавить', command=lambda: self.__add(_id.get(),
                                                                       'Зубенко Михаил Григорьевич',
                                                                       client.get(),
                                                                       _type.get(),
                                                                       amount.get(),
                                                                       comment.get("1.0", END), new_dialog)) \
            .grid(row=5, column=0, padx=3, pady=3, sticky=EW)
        Button(new_dialog, text='Отмена', command=lambda: new_dialog.destroy()).grid(row=5, column=1, padx=3, pady=3,
                                                                                     sticky=EW)

    def add(self, idNum, oper, client, typeDeal, amount, comment):
        check_value = BooleanVar()
        check_value.set(False)
        self.__checkValues.append(check_value)
        self.__check.append(Checkbutton(self.__table,
                                        var=self.__checkValues[len(self.__checkValues) - 1],
                                        onvalue=True, offvalue=False,
                                        relief=SOLID, borderwidth=1))
        self.__id.append(Label(self.__table, relief=SOLID, borderwidth=1, text=idNum))
        self.__oper.append(Label(self.__table, relief=SOLID, borderwidth=1, text=oper))
        self.__client.append(Label(self.__table, relief=SOLID, borderwidth=1, text=client))
        self.__type.append(Label(self.__table, relief=SOLID, borderwidth=1, text=typeDeal))
        self.__amount.append(Label(self.__table, relief=SOLID, borderwidth=1, text=amount))
        self.__comment.append(Label(self.__table, relief=SOLID, borderwidth=1, text=comment))
        self.__pack()

    def delete(self):
        for i in reversed(range(len(self.__check))):
            if self.__checkValues[i].get():
                self.__check[i].grid_forget()
                self.__id[i].grid_forget()
                self.__oper[i].grid_forget()
                self.__client[i].grid_forget()
                self.__type[i].grid_forget()
                self.__amount[i].grid_forget()
                self.__comment[i].grid_forget()

                self.__check.pop(i)
                self.__checkValues.pop(i)
                self.__id.pop(i)
                self.__oper.pop(i)
                self.__client.pop(i)
                self.__type.pop(i)
                self.__amount.pop(i)
                self.__comment.pop(i)

    def __init__(self, master, text='Сделки', bg='lightgrey') -> None:
        super().__init__()
        control = Frame(master)
        control.pack(side=RIGHT, fill=BOTH)

        self.__del = Button(control, text='Удалить выделенные')
        self.__del.config(command=self.delete)
        self.__del.pack(side=TOP, fill=BOTH, padx=5, pady=2)

        self.__new = Button(control, text='Добавить сделку')
        self.__new.config(command=self.new)
        self.__new.pack(side=TOP, fill=BOTH, padx=5, pady=2)

        self.__master = master
        self.__check = []
        self.__checkValues = []
        self.__id = []
        self.__oper = []
        self.__client = []
        self.__type = []
        self.__amount = []
        self.__comment = []
        self.__table = LabelFrame(master, text=text, bg=bg)
        self.__table.pack(side=LEFT, fill=BOTH, expand=1, padx=5, pady=5)
        self.__check.append(Checkbutton(self.__table, relief=SOLID, borderwidth=1, state=DISABLED))
        self.__checkValues.append(BooleanVar())
        self.__id.append(Label(self.__table, relief=SOLID, borderwidth=1, text='id'))
        self.__oper.append(Label(self.__table, relief=SOLID, borderwidth=1, text='Оператор'))
        self.__client.append(Label(self.__table, relief=SOLID, borderwidth=1, text='Клиент'))
        self.__type.append(Label(self.__table, relief=SOLID, borderwidth=1, text='Тип сделки'))
        self.__amount.append(Label(self.__table, relief=SOLID, borderwidth=1, text='Сумма сделки'))
        self.__comment.append(Label(self.__table, relief=SOLID, borderwidth=1, text='Комментарий'))

        self.__pack()


if __name__ == '__main__':
    mainWindow = Tk()
    mainWindow.title("Строительство. Отдел продаж.")
    mainWindow.geometry('800x800')
    table = Table(mainWindow)
    table.add('1', 'Зубенко Михаил Петрович', 'Михайлов Тест Тестович', 'Покупка', '200000.00',
              'Ну и дурак он, что эту развалину купил!')
    mainWindow.mainloop()
