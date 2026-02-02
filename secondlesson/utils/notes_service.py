def show_notes(notes):
    if len(notes) == 0:
        print("Нет заметок")
        return
    
    number = 1
    for i in notes:
        status = "👌" if i["done"] else " "
        print(number,".", "[", status, "]", i["text"])
        number = number + 1

def add_note(notes):
    text = input("Введите заметку: ").strip()
    if text == "":
        print("Пустую заметку нелья добавить")
        return
    notes.append({"text": text, "done": False})
    print("Добавлено")

def toggle_done(notes):
    if len(notes) == 0:
        print("Список пуст")
        return
    
    num = input("Номер заметки: ").strip()
    if not num.isdigit():
        print("Нужно число")
        return
    
    index = int(num) - 1
    if index < 0 or index >= len(notes):
        print("Нет такой заметки")
        return
    
    notes[index]["done"] = not notes[index]["done"]
    print("Статус изменен")
    
def delete_notes(notes):
    note_d = input("Введите номер заметки, которую нужно удалить: ").strip()

    if not note_d.isdigit():
        print("Нужно ввести число")
        return

    index = int(note_d) - 1

    if index < 0 or index >= len(notes):
        print("Заметка не найдена")
        return

    notes.pop(index)
    print("Заметка удалена")