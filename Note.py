from datetime import date


class Note:
    def __init__(self, name, content, id, creation_date=date.today()):
        self.__note_name = name
        self.__content = content
        self.__note_id = id
        self.__creation_date = creation_date

    def get_id(self):
        return self.__note_id

    def __str__(self):
        return (
            f"{self.__creation_date}\n{self.__note_name}\n"
            f"{self.__content}\n-----------------")

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, text):
        self.__content = text

    @property
    def creation_date(self):
        return self.__creation_date

    @creation_date.setter
    def creation_date(self, date_1):
        date_time_obj = datetime.datetime.strptime(date_1, '%Y-%m-%d')
        self.__creation_date = date_time_obj

    @property
    def note_name(self):
        return self.__note_name

    @creation_date.setter
    def creation_date(self):
        self.__creation_date = date.today()


class Notes(Note):

    def __init__(self):
        self.__list_of_notes = dict()

    def add_note(self, note):
        a = note.get_id()
        self.__list_of_notes.update({a: note})

    @property
    def list_of_notes(self):
        return self.__list_of_notes

    def get_by_id(self, id):
        return self.__list_of_notes.get(id)
