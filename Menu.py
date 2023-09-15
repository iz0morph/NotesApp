from Command import *


class Menu:
    def __init__(self, console):
        self.console = console
        self.commands = list()
        self.commands.append(AddNote(console))
        self.commands.append(ChangeNote(console))
        self.commands.append(ShowTheNote(console))
        self.commands.append(DateFilter(console))
        self.commands.append(ShowAllNotes(console))
        self.commands.append(DeleteNote(console))
        self.commands.append(StopWorking(console))
        self.commands.append(DeleteAll(console))

    def print_menu(self):
        count = 1
        for i in self.commands:
            print(f"{count}. {i.description}")
            count = count + 1
        print('\n')

    @property
    def size(self):
        return len(self.commands)

    def run(self, command):
        self.commands[command - 1].run()
