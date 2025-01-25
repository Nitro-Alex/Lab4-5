from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from Data_input import DataInput
from Data_table import DataTable
from Class_implementaition import *
from Func_implementation import read_db

class HomeWindow(Tk):
    def __init__(self, ges):
        super().__init__()
        self.ges1 = ges

        self.title("ЖЭС №1")
        self.geometry("1000x600")
        self.configure(bg='lightgreen')
        self.option_add("*tearOff", FALSE)

        label_title = ttk.Label(self, text="ЖЭС №1", font=("Arial", 30, "bold"), background='lightgreen')
        label_title.pack(pady=20)

        #создание кнопок
        button_add = ttk.Button(self, text="Добавить\nзапись", command = lambda: self.open_data_window(5))
        button_exit = ttk.Button(self, text="Выход", command=self.exit_program)
        button_add.place(relx=0.35, rely=0.5, width=120, height=70)
        button_exit.place(relx=0.55, rely=0.5, width=120, height=70)

        #создание меню
        menu_bar = Menu()
        self.config(menu=menu_bar)

        manual_input = Menu()
        manual_input.add_command(label="Добавить тариф", command = lambda: self.open_data_window(1))
        manual_input.add_command(label="Добавить жильца", command = lambda: self.open_data_window(2))

        change_data = Menu()
        change_data.add_command(label="Изменить тариф", command = lambda: self.open_data_window(3))
        change_data.add_command(label="Изменить жильца", command = lambda: self.open_data_window(4))

        input_menu = Menu()
        input_menu.add_cascade(label="Ввести данные вручную", menu=manual_input)
        input_menu.add_command(label="Добавить данные из файла", command = self.open_file)
        input_menu.add_cascade(label="Изменить данные", menu=change_data)

        summ_dolg = Menu()
        summ_dolg.add_command(label="В обычном порядке", command=lambda: self.open_data_table(0))
        summ_dolg.add_command(label="Сортировать по сумме задолженности", command = lambda: self.open_data_table(1))
        summ_dolg.add_command(label="Сортировать по алфавиту", command=lambda: self.open_data_table(2))

        output_menu = Menu()
        output_menu.add_cascade(label="Вывод таблицы задолженностей", menu=summ_dolg)
        output_menu.add_command(label="Сохранить данные в файл", command=self.save_file)

        menu_bar.add_cascade(label="Ввод данных", menu=input_menu)
        menu_bar.add_cascade(label="Вывод данных", menu=output_menu)

    def exit_program(self):
        self.destroy()

    def open_file(self): #чтение входных данных из файла
        filepath = filedialog.askopenfilename(title="Выберите текстовый файл", filetypes=(("Текстовые файлы", "txt"),))
        services = []
        residents = []
        if filepath != "":
            with open(filepath, 'r') as file:
                lines = file.readlines()
                is_in_services = False
                is_in_residents = False
                for line in lines:
                    line = line.strip()
                    if line == "Services":
                        is_in_services = True
                        is_in_residents = False
                        continue
                    if line == "Residents":
                        is_in_services = False
                        is_in_residents = True
                        continue
                    if is_in_services and line:
                        ser_name, cost = line.split()
                        services.append((ser_name, float(cost)))
                    if is_in_residents and line:
                        surname, name = line.split()
                        residents.append((surname, name))
            for i in services:
                self.ges1.add_service(Service(i[0], i[1]))
            for i in residents:
                self.ges1.add_resident(Resident(i[0], i[1]))
        else:
            pass

    def save_file(self): #сохранение данных в файл
        data_to_save = read_db()
        filepath = filedialog.asksaveasfilename(title="Выберите текстовый файл", filetypes=(("Текстовые файлы", "txt"),))
        if filepath != "":
            with open(filepath, "w") as file:
                for i in data_to_save:
                    file.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + " " + str(i[3]) + "\n")
        else:
            pass

    def open_data_window(self, switch):
        data_input = DataInput(switch, self.ges1)

    def open_data_table(self, sort_flag):
        data_table = DataTable(sort_flag, self.ges1)