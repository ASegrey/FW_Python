from Note import Note


class Menu:
    def menu():
        while True:
            print("Команды: ")
            print("add  -> Добавление заметки ")
            print("view -> Показать выбранную заметку")
            print("edit -> Изменение заметки ")
            print("dell -> Удаление заметки ")
            print("all  -> Показать все заментки")
            print("find -> Показать все заментки с указанной датой")
            print("exit -> Выход из программы")
            x = input("Введите команду: ")
            print("")
            if x == "exit":
                break
            elif x == "add":
                Note.add_note()
            elif x == "view":
                Note.find_note()
            elif x == "edit":
                Note.change_note()
            elif x == "dell":
                Note.dell_note()
            elif x == "all":
                Note.print_all_notes(Note.read_json_note())
            elif x == "find":
                Note.find_note_date()
            else:
                print("Команда не известна!")