# with open("data/notes.txt", "r", encoding="utf-8") as file:
#     content = file.read()
# print(content)

# with open("data/notes.txt", "r", encoding="utf-8") as file:
#     for i in file:
#         print(i.strip("-"))

# with open("data/notes.txt", "a", encoding="utf-8") as file:
#     file.write("Добавление новой заметки")

# with open ("data/notes.txt", "r", encoding="utf-8") as file:
#     content = file.read()
# print(content)

# file = open("data/notes.txt", "r", encoding="utf-8")
# content = file.read()
# print(content)
# file.close()

# with open("data/notes.txt", "w", encoding="utf-8") as file:
#     file.write("Попытка записи в режиме чтения. ")
#     file.write("Вторая запись.")

# with open("data/notes.txt", "r", encoding="utf-8") as file:
#     for i in file:
#         clean_line = i.strip()
#         print(clean_line)   

# 1. Показать
# 2. Добавить
# 3. Сохранить
# 0. Выйти

def load_notes_txt():
    notes = []
    with open ("data/notes.txt", "r", encoding="utf-8") as file:
        for i in file:
            clean = i.strip()
            if clean != "":
                notes.append(clean)
    return notes

def show_notes_txt(notes):
    if len(notes) == 0:
        print("Заметок нет")
        return

    number = 1
    for i in notes:
        print(number, ".", i)
        number = number+1

def add_note_txt(notes):
    text = input("Введите заметки: ").strip()
    if text == "":
        print("Пустую заметку нельзя добавить")
        return
    
    notes.append(text)
    print("Добавлено!")

def save_notes_txt(notes):
    with open("data/notes.txt", "w", encoding="utf-8") as file:
        for i in notes:
            file.write(i+"\n")

notes = load_notes_txt()

while True:
    print("\n1. Показать")
    print("2. Добавить")
    print("3. Сохранить")
    print("0. Выйти")

    choice = input("Выбор: ")

    if choice == "1":
        show_notes_txt(notes)
    elif choice =="2":
        add_note_txt(notes)
    elif choice =="3":
        save_notes_txt(notes)
        print("Выход")
    elif choice =="0":
        save_notes_txt(notes)
        print("Выход")
        break
    else:
        print("Неверный выбор")
