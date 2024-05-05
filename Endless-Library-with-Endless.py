import tkinter as tk
import itertools

def get_book_text(stellage_number, book_number, language_number):
    # Мы получаем символы, из которых состоит книга
    characters = get_characters(stellage_number, book_number, language_number)
    
    # Преобразование символов в текст
    text = ''.join(characters)
    
    return text

def get_characters(stellage_number, book_number, language_number):
    # Мы получаем все возможные символы для этого стеллажа
    all_characters = get_all_characters(stellage_number, language_number)
    
    # Мы получаем символы, из которых состоит книга
    book_characters = get_book_characters(all_characters, book_number)
    
    return book_characters

def get_all_characters(stellage_number, language_number):
    # Мы получаем все возможные символы для этого стеллажа
    if language_number == 1:
        return list(itertools.islice(itertools.product('абвгдежзийклмнопрстуфхцчшщъыьэюя., 0123456789', repeat=stellage_number), 1000))
    else:
        return list(itertools.islice(itertools.product('abcdefghijklmnopqrstuvwxyz., 0123456789', repeat=stellage_number), 1000))

def get_book_characters(all_characters, book_number):
    # Мы получаем символы, из которых состоит книга
    if book_number > len(all_characters):
        raise ValueError('Неверный номер книги')
    
    # Мы получаем символы, из которых состоит книга
    book_characters = list(all_characters[book_number - 1])
    
    return book_characters

def switch_page():
    stellage_number_input = entry_stellage.get()
    if stellage_number_input == '∞':
        stellage_number = float('inf')
    else:
        stellage_number = int(stellage_number_input)
    book_number = int(entry_page.get())
    book_text = get_book_text(stellage_number, book_number, language_number.get())
    text_output.delete('1.0', tk.END)
    text_output.insert(tk.END, book_text)

# Создание основного окна
root = tk.Tk()
root.title("Библиотека")

# Фрейм для выбора языка
frame_language = tk.Frame(root)
frame_language.pack(pady=10)
label_language = tk.Label(frame_language, text="Выберите язык:")
label_language.pack(side="left")
language_number = tk.IntVar()
language_number.set(1)  # Устанавливаем русский язык по умолчанию
radio_russian = tk.Radiobutton(frame_language, text="Русский", variable=language_number, value=1)
radio_russian.pack(side="left")
radio_english = tk.Radiobutton(frame_language, text="English", variable=language_number, value=2)
radio_english.pack(side="left")

# Фрейм для ввода номера стеллажа и страницы
frame_input = tk.Frame(root)
frame_input.pack(pady=10)
label_stellage = tk.Label(frame_input, text="Номер стеллажа:")
label_stellage.pack(side="left")
entry_stellage = tk.Entry(frame_input, width=10)
entry_stellage.pack(side="left")
label_page = tk.Label(frame_input, text="Номер страницы:")
label_page.pack(side="left")
entry_page = tk.Entry(frame_input, width=10)
entry_page.pack(side="left")
entry_page.bind("<Return>", lambda event: switch_page())  # Обработка нажатия Enter

# Кнопка для переключения на введенную страницу
button_switch = tk.Button(root, text="Переключить", command=switch_page)
button_switch.pack(pady=5)

# Текстовое поле для вывода текста книги
text_output = tk.Text(root, width=50, height=20)
text_output.pack()

root.mainloop()
