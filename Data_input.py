from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Class_implementaition import *
from Func_implementation import insert_db

class DataInput(Toplevel):
    def __init__(self, switch, ges):
        super().__init__()

        self.ges1 = ges
        self.service_list = []
        self.resident_list = []
        self.title("Default")
        self.geometry("350x400")
        self.configure(bg="#FFDAB9")
        self.grab_set()

        self.combo_box1 = ttk.Combobox(self, state ="readonly")
        self.combo_box1.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        self.combo_box1.bind("<FocusIn>", self.focus)
        self.combo_box1.bind("<<ComboboxSelected>>", self.select)

        self.label1 = ttk.Label(self, text="label1", background="#FFDAB9")
        self.label1.grid(row=1, column=0, padx=20, pady=5)

        self.entry1 = ttk.Entry(self)
        self.entry1.grid(row=2, column=0, padx=20, pady=5)
        self.entry1.bind("<FocusIn>", self.focus)

        self.label2 = ttk.Label(self, text="label2", background="#FFDAB9")
        self.label2.grid(row=3, column=0, padx=20, pady=5)

        self.entry2 = ttk.Entry(self)
        self.entry2.grid(row=4, column=0, padx=20, pady=5)
        self.entry2.bind("<FocusIn>", self.focus)

        self.button_add = ttk.Button(self, text="Добавить")
        self.button_add.grid(row=5, column=0, padx=20, pady=10)

        self.button_main_menu = ttk.Button(self, text="Главное меню", command = self.close_window)
        self.button_main_menu.grid(row=6, column=0, padx=20, pady=5)

        self.label_info = ttk.Label(self, text="Default", background="#FFDAB9")
        self.label_info.grid(row=7, column=0, padx=20, pady=5)

        self.grid_columnconfigure(0, weight=1)
        match switch:
            case 1: #перегрузка добавление тарифа
                self.title("Добавление тарифа")
                self.combo_box1.grid_forget()
                self.button_add.config(command = self.add_ser)
                self.label1.config(text="Название тарифа:")
                self.label2.config(text="Цена:")
                self.label_info.config(text="Тариф успешно добавлен")
                self.label_info.grid_forget()
            case 2: #перегрузка добавление жильца
                self.title("Добавление жильца")
                self.combo_box1.grid_forget()
                self.button_add.config(command = self.add_res)
                self.label1.config(text="Фамилия:")
                self.label2.config(text="Имя:")
                self.label_info.config(text="Жилец успешно добавлен")
                self.label_info.grid_forget()
            case 3: #перегрузка изменение данных тарифа
                self.title("Изменение данных тарифа")
                self.service_list = [i.get_name() for i in self.ges1.get_services()]
                self.combo_box1.config(values = self.service_list)
                self.entry1.config(state="disabled")
                self.entry2.config(state="disabled")
                self.label1.config(text="Новое название тарифа:")
                self.label2.config(text="Новая цена:")
                self.label_info.config(text="Данные тарифа успешно изменены")
                self.label_info.grid_forget()
                self.button_add.config(text="Изменить", command = self.change_service)
            case 4: #перегрузка изменение данных жильца
                self.title("Изменение данных жильца")
                self.resident_list = [i.get_surname() + " " + i.get_name() for i in self.ges1.get_residents()]
                self.combo_box1.config(values = self.resident_list)
                self.entry1.config(state="disabled")
                self.entry2.config(state="disabled")
                self.label1.config(text="Новая фамилия:")
                self.label2.config(text="Новое имя:")
                self.label_info.config(text="Данные жильца успешно изменены")
                self.label_info.grid_forget()
                self.button_add.config(text="Изменить", command = self.change_resident)
            case 5: #перегрузка добавление записи
                self.title("Добавление записи")
                self.button_add.config(command = self.add_note)
                self.combo_box1.grid_forget()
                self.label1.config(text="Жилец:")
                self.label2.config(text="Используемый тариф:")
                self.label_info.config(text="Запись успешно добавлена")
                self.label_info.grid_forget()
                self.entry1.grid_forget()
                self.entry2.grid_forget()
                self.service_list = [i.get_name() for i in self.ges1.get_services()]
                self.resident_list = [i.get_surname() + " " + i.get_name() for i in self.ges1.get_residents()]
                self.combo_box2 = ttk.Combobox(self, values = self.resident_list, state="readonly")
                self.combo_box2.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
                self.combo_box2.bind("<FocusIn>", self.focus)
                self.combo_box3 = ttk.Combobox(self, values = self.service_list, state="readonly")
                self.combo_box3.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
                self.combo_box3.bind("<FocusIn>", self.focus)

    def close_window(self):
        self.grab_release()
        self.destroy()

    #!!!!!!!!!!!!!!!!!!!! ДОБАВИТЬ ПРОВЕРКИ !!!!!!!!!!!!!!!!!!!
    def add_ser(self): #добавление тарифа
        if not self.entry1.get().strip() or not self.entry2.get().strip():
            messagebox.showerror("Ошибка", "Заполните оба поля!")
        else:
            try:
                cost = float(self.entry2.get())
                if cost <= 0:
                    messagebox.showerror("Ошибка", "Цена должна быть положительной")
                    return
                if cost > 100000:
                    messagebox.showerror("Ошибка", "Цена не должна превышать разумных пределов")
                    return
            except ValueError:
                messagebox.showerror("Ошибка", "Поле Цена должно содержать число")
                return
            self.ges1.add_service(Service(self.entry1.get(), float(self.entry2.get())))
            self.entry1.delete(0, END)
            self.entry2.delete(0, END)
            self.label_info.grid(row=7, column=0, padx=20, pady=5)


    def add_res(self): #добавление жильца
        if not self.entry1.get().strip() or not self.entry2.get().strip():
            messagebox.showerror("Ошибка", "Заполните оба поля!")
        else:
            self.ges1.add_resident(Resident(self.entry1.get(), self.entry2.get()))
            self.entry1.delete(0, END)
            self.entry2.delete(0, END)
            self.label_info.grid(row=7, column=0, padx=20, pady=5)

    def change_service(self): #изменение тарифа
        if not self.entry1.get().strip() or not self.entry2.get().strip():
            messagebox.showerror("Ошибка", "Заполните оба поля!")
        else:
            try:
                cost = float(self.entry2.get())
                if cost <= 0:
                    messagebox.showerror("Ошибка", "Цена должна быть положительной")
                    return
                if cost > 100000:
                    messagebox.showerror("Ошибка", "Цена не должна превышать разумных пределов")
                    return
            except ValueError:
                messagebox.showerror("Ошибка", "Поле Цена должно содержать число")
                return
            selected_service = self.ges1.find_service(self.combo_box1.get())
            selected_service.set_name(self.entry1.get())
            selected_service.set_cost(float(self.entry2.get()))

            data_to_insert = self.ges1.get_data()
            insert_db(data_to_insert)

            self.service_list = [i.get_name() for i in self.ges1.get_services()]
            self.combo_box1.config(values=self.service_list)
            self.entry1.delete(0, END)
            self.entry2.delete(0, END)
            self.combo_box1.set("")
            self.entry1.config(state="disabled")
            self.entry2.config(state="disabled")
            self.label_info.grid(row=7, column=0, padx=20, pady=5)

    def change_resident(self): #изменение жильца
        if not self.entry1.get().strip() or not self.entry2.get().strip():
            messagebox.showerror("Ошибка", "Заполните оба поля!")
        else:
            selected_surname, selected_name = map(str, self.combo_box1.get().split())
            selected_res = self.ges1.find_res(selected_surname)
            selected_res.set_name(self.entry1.get(), self.entry2.get())

            data_to_insert = self.ges1.get_data()
            insert_db(data_to_insert)

            self.resident_list = [i.get_surname() + " " + i.get_name() for i in self.ges1.get_residents()]
            self.combo_box1.config(values=self.resident_list)
            self.entry1.delete(0, END)
            self.entry2.delete(0, END)
            self.combo_box1.set("")
            self.entry1.config(state="disabled")
            self.entry2.config(state="disabled")
            self.label_info.grid(row=7, column=0, padx=20, pady=5)

    def add_note(self): #добавление записи
        if not self.combo_box2.get().strip() or not self.combo_box3.get().strip():
            messagebox.showerror("Ошибка", "Заполните оба поля!")
        else:
            selected_surname, selected_name = map(str, self.combo_box2.get().split())
            selected_service = self.combo_box3.get()
            selected_res = self.ges1.find_res(selected_surname)
            selected_res.use_service(self.ges1.find_service(selected_service))

            data_to_insert = self.ges1.get_data()
            insert_db(data_to_insert)
            self.label_info.grid(row=7, column=0, padx=20, pady=5)
            self.combo_box2.set("")
            self.combo_box3.set("")

    def focus(self, event):
        self.label_info.grid_forget()

    def select(self, event):
        self.entry1.config(state="normal")
        self.entry2.config(state="normal")