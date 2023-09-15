import json
from Note import Note, Notes
from datetime import datetime


class FileHandler:
    def get_json_obj(self):
        with open("notes.json") as file:
            obj = json.load(file)
        return obj

    def restore_notes(self):
        array = []
        with open("notes.json", "r", encoding='utf-8') as file:
            obj = json.load(file)
            notes = obj['notes']
            for i in notes:
                note = Note(id=i.get('id'), content=i.get('Content'),
                            name=i.get('Name'),
                            creation_date=datetime.strptime(i.get(
                                'Creation Date'), '%Y-%m-%d').date())
                array.append(note)
        return array

    def write_note(self, note: Note):
        obj = self.get_json_obj()
        lst = obj['notes']
        format_string = '%Y-%m-%d'
        creation_date = note.creation_date.strftime(format_string)
        with open("notes.json", 'w', encoding='utf-8') as file:
            new_note = {'id': note.get_id(), 'Creation Date': creation_date,
                        'Name': note.note_name, 'Content': note.content}
            lst.append(new_note)
            json.dump(obj, file, indent=4)

    def rewrite_note(self, id, text):
        obj = self.get_json_obj()
        lst = obj['notes']
        i = 0
        while i < len(lst):
            if lst[i].get('id') == id:
                lst[i]['Content'] = text
                break
            i += 1
        with open("notes.json", 'w', encoding='utf-8') as file:
            json.dump(obj, file, indent=4)

    def delete_note(self, id):
        obj = self.get_json_obj()
        lst = obj['notes']
        i = 0
        while i < len(lst):
            if lst[i].get('id') == id:
                lst.remove(lst[i])
                break
            i += 1
        with open("notes.json", 'w', encoding='utf-8') as file:
            json.dump(obj, file, indent=4)

    def check_last_id(self):
        obj = self.get_json_obj()
        lst = obj['notes']
        if len(lst) != 0:
            return lst[len(lst) - 1].get('id') + 1
        return 0

    def delete_all(self):
        obj = self.get_json_obj()
        lst = obj['notes']
        i = 0
        while i < len(lst):
            lst.remove(lst[i])
        with open("notes.json", 'w', encoding='utf-8') as file:
            json.dump(obj, file, indent=4)
