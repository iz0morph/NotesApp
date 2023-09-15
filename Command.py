__all__ = ['AddNote', 'ChangeNote', 'DeleteNote', 'ShowAllNotes',
           'ShowTheNote', 'DateFilter', 'Command', 'StopWorking', 'DeleteAll']

class Command:
    def __init__(self, description, console):
        self.__description = description
        self.console = console

    @property
    def description(self):
        return self.__description


class AddNote(Command):
    def __init__(self, console):
        super().__init__(description="Добавить заметку", console=console)

    def run(self):
        self.console.add_note()


class ChangeNote(Command):
    def __init__(self, console):
        super().__init__(description="Изменить заметку", console=console)

    def run(self):
        self.console.change_note()


class DeleteNote(Command):
    def __init__(self, console):
        super().__init__(description="Удалить заметку", console=console)

    def run(self):
        self.console.delete_note()


class ShowTheNote(Command):
    def __init__(self, console):
        super().__init__(description="Показать указанную заметку",
                         console=console)

    def run(self):
        self.console.show_note()


class ShowAllNotes(Command):
    def __init__(self, console):
        super().__init__(description="Показать все заметки", console=console)

    def run(self):
        self.console.show_all_notes()


class DateFilter(Command):
    def __init__(self, console):
        super().__init__(description="Показать все заметки за указанный "
                                     "период", console=console)

    def run(self):
        self.console.date_filter()


class StopWorking(Command):
    def __init__(self, console):
        super().__init__(description="Закончить работу", console=console)

    def run(self):
        self.console.stop_working()


class DeleteAll(Command):
    def __init__(self, console):
        super().__init__(description="Удалить все заметки", console=console)

    def run(self):
        self.console.delete_all()
