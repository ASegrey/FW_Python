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
        if os.path.isfile("note.json"):
            with open("note.json", "r") as file:
                size = os.path.getsize("note.json")
                if size != 0:
                    with open('note.json', "r") as json_file:
                        data_notes = json.load(json_file)
        else:
            file = open("note.json", "w+")
            file.close()
        return data_notes


    def write_json_note(note):
        data_load = Note.read_json_note() 
        for p in data_load['notes']:
            if p['name'] == note.name and p['date'] == note.date:
                print(f"Заметка '{note.name}' с датой {note.date} уже существует!")
                print('')
                return
        data_load['notes'].append({
            'name': note.name,
            'date': note.date,
            'note': note.data_note
        })
        with open('note.json', 'w+', encoding = "UTF-8") as outfile:
            json.dump(data_load, outfile)
            print("Заметка успешно сохранена")
    

    def print_all_notes(data_load):
        if len(data_load['notes']) == 0: 
            print("Нет заметок")
        else:    
            for p in data_load['notes']:
                Note.print_note(p)
        
    def print_note(p):
        print(f"Заметка: '{p['name']}'")
        print(f"Дата: {p['date']}г.")
        print('Описание => ' + p['note'])
        print('')   

    def add_note():
        text_heading = input("Введите заголовок заметки: ")
        text_note = input("Введите тело заметки: ")
        Note.write_json_note(Note(text_heading,text_note))

    def dell_note():
        note_name = input("Введите заголовок заметки для удаления: ")
        note_date = input("Введите дату заметки в формате 'дд-мм-гг': ")
        data_load = Note.read_json_note()
        for p in data_load['notes'].copy():
            if p.get('name') == note_name and p.get('date') == note_date:
                data_load['notes'].remove(p)
                with open('note.json', 'w+', encoding = "UTF-8") as outfile:
                    json.dump(data_load, outfile)
                    print(f"Заметка '{note_name}' с датой {note_date} УДАЛЕНА!")
                return
        print(f"Заметка '{note_name}' с датой {note_date} не найдена!")
        print('')

    def find_note():
        note_name = input("Введите заголовок заметки для поиска: ")
        note_date = input("Введите дату заметки в формате 'дд-мм-гг': ")
        data_load = Note.read_json_note()
        for p in data_load['notes']:
            if p['name'] == note_name and p['date'] == note_date:
                Note.print_note(p)
                return       
        print(f"Заметка '{note_name}' с датой {note_date} не найдена!")
        print('')
        
    def find_note_date():
        note_date = input("Введите дату заметок в формате 'дд-мм-гг': ")
        data_load = Note.read_json_note()
        is_note = False
        for p in data_load['notes']:
            if  p['date'] == note_date:
                Note.print_note(p)
                is_note = True
        if is_note == False:        
            print(f"Заметок с датой {note_date} нет!")
            print('')

    def change_note():
        note_name = input("Введите заголовок заметки для изменения: ")
        note_date = input("Введите дату заметки в формате 'дд-мм-гг': ")
        note_data = input("Введите тело заметки: ")
        data_load = Note.read_json_note()
        for p in data_load['notes']:
            if p['name'] == note_name and p['date'] == note_date:
                p['note'] = note_data
                with open('note.json', 'w+', encoding = "UTF-8") as outfile:
                    json.dump(data_load, outfile)
                    print(f"Заметка '{note_name}' с датой {note_date} изменена!")
                return
        print(f"Заметка '{note_name}' с датой {note_date} не найдена!")
        print('')
