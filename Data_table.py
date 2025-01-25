from tkinter import *
from tkinter import ttk
from Func_implementation import read_db, delete_db


class DataTable(Toplevel):
    def __init__(self, sort_flag, ges):
        super().__init__()

        self.style = ttk.Style()
        self.style.configure("Treeview.Cell", anchor="center")
        self.ges1 = ges
        self.title("Таблица задолженностей")
        self.geometry("900x500")
        self.grab_set()

        self.tree = ttk.Treeview(self, columns=("number", "surname", "name", "debt"), show="headings")
        self.tree.heading("number", text="№")
        self.tree.heading("surname", text="Фамилия")
        self.tree.heading("name", text="Имя")
        self.tree.heading("debt", text="Задолженность")

        self.tree.column("number", width=10)
        self.tree.column("surname", width=150)
        self.tree.column("name", width=150)
        self.tree.column("debt", width=100)

        self.tree.pack(expand=True, fill="both")

        self.main_menu_button = ttk.Button(self, text="Главное меню", command=self.close_window)
        self.main_menu_button.pack(side="bottom", pady=7)

        self.clear_button = ttk.Button(self, text="Удалить данные", command=self.delete_data)
        self.clear_button.pack(side="left", padx=20, pady=7)

        self.total_label = ttk.Label(self, text="Суммарная задолженность: " + str(self.ges1.total_cost()) + " руб.")
        self.total_label.pack(side="right", padx=20, pady=7)

        data_to_show = read_db()
        if sort_flag == 1: #сортировка по сумме
            data_to_show.sort(key=lambda x: x[3])
        if sort_flag == 2: #сортировка по алфавиту
            data_to_show.sort(key=lambda x: x[1])
        c = 1
        for i in data_to_show:
            row = (int(c), i[1], i[2], i[3])
            self.tree.insert("", "end", values=row)
            c += 1

    def close_window(self):
        self.grab_release()
        self.destroy()

    def delete_data(self): #удаление всех записей
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.ges1.clear_notes()
        delete_db()
        self.total_label.config(text="Суммарная задолженность: 0 руб.")