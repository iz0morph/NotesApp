from Menu import Menu
from Service import Service


class Console:

    def __init__(self):
        self.__menu = Menu(console=self)
        self.__service = Service()
        self.__work = True


    def run(self):
        print("Привет, выбери действие:")
        while self.__work:
            self.__menu.print_menu()
            self.scan()


    def scan(self):
        command = input()
        if self.check_text_for_int(command):
            number = int(command)
            if self.check_command(number):
                self.__menu.run(number)

    def check_command(self, number):
        if number <= self.__menu.size:
            return True
        return False

    def check_text_for_int(self, line):
        if line.isdigit():
            return True
        print("Неверный ввод: введено не число")
        return False

    def add_note(self):
        name = input("Введите название заметки")
        content = input("Запишите свои умные мысли")
        self.__service.add_note(name, content)

    def delete_note(self):
        id = input("Введите id заметки")
        if self.check_text_for_int(id):
            self.__service.delete_note(id)
        else:
            print("Введено не число")

    def change_note(self):
        id = input("Введите id изменяемой заметки")
        if self.check_text_for_int(id):
            text = input("Введите новый текст")
            self.__service.change_note(int(id), text)
        else:
            print("Введено не число")

    def show_note(self):
        id = input("Введите id желаемой заметки")
        if self.check_text_for_int(id):
            self.__service.show_note(id)
        else:
            print("Введено не число")

    def show_all_notes(self):
        self.__service.show_all()

    def date_filter(self):
        earlier_date = input("Введите начальную дату поиска в формате: Y-m-d")
        later_date = input("Введите конечную дату поиска: Y-m-d")
        format_string = '%Y-%m-%d'
        # try:
        #     date_1 = earlier_date.strftime(format_string)
        #     date_2 = later_date.strftime(format_string)
        self.__service.date_filter(earlier_date, later_date)
        # except IOError as e:
        #     print("Неверный ввод даты")

    def stop_working(self):
        self.__work=False

    def delete_all(self):
        self.__service.delete_all()

