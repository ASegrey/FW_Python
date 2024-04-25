from datetime import date
import os
import json


class Note:
    def __init__(self, name, data_note):
        self.name = name
        self.date = date.today().strftime('%d-%m-%y')
        self.data_note = data_note
    
        
    def to_json(self): 
        return json.dumps(self, indent = 4, default=lambda o: o.__dict__)
    

    def read_json_note():
        data_notes = {}
        data_notes['notes'] = []
        if (os.path.isfile("note.json")):
            with open("note.json", "r") as file:
                if (file.readline() == None):
                    print("Нет заметок")
                else:
                    with open('note.json', "r") as json_file:
                        data_notes = json.load(json_file)
        else:
            print("Нет заметок")
            file = open("note.json", "w+")
            file.close()
        return data_notes


    def write_json_note(note):
        data_load = Note.read_json_note() 
        data_load['notes'].append({
            'name': note.name,
            'date': note.date,
            'note': note.data_note
        })
        with open('note.json', 'w+', encoding = "UTF-8") as outfile:
            json.dump(data_load, outfile)
    

    def print_all_notes(data_load):
        for p in data_load['notes']:
            print(f"Заметка: '{p['name']}' {p['date']}г.")
            print('=> ' + p['note'])
            print('')