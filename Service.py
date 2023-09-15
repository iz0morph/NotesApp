from FileHanler import FileHandler
from Note import Note, Notes


class Service:

    def __init__(self):
        self.__file_handler = FileHandler()
        a = Notes()
        array = self.__file_handler.restore_notes()
        for i in array:
            a.add_note(i)
        self.__notes = a

    def show_all(self):
        for i in self.__notes.list_of_notes.values():
            print(i)

    def show_note(self, id):
        try:
            print(self.__notes.list_of_notes.get(int(id)))
        except KeyError as e:
            print(f"Такой заметки нет!")

    def add_note(self, name, text):
        id = self.__file_handler.check_last_id()
        new_note = Note(name, text, id)
        self.__notes.add_note(new_note)
        self.__file_handler.write_note(new_note)
        print("Заметка сохранена")

    def delete_note(self, id):
        self.__notes.list_of_notes.pop(id)
        print("Заметка удалена")
        self.__file_handler.delete_note(id)

    def date_filter(self, earlier_date, later_date):
        i: Note
        print("Заметки за выбранный период:\n")
        for i in self.__notes.list_of_notes.values():
            if i.creation_date > earlier_date and i.creation_date < later_date:
                print(i)

    def change_note(self, id, text):
        for key in self.__notes.list_of_notes:
            if key == id:
                self.__notes.list_of_notes[key].content = text
                print(self.__notes.list_of_notes[key].content)
                break
        self.__file_handler.rewrite_note(id, text)
        print("Заметка изменена")

    def delete_all(self):
        self.__file_handler.delete_all()
