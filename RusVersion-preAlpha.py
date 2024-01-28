import itertools

def get_book_text(stellage_number, book_number):
    # Мы получаем символы, из которых состоит книга
    characters = get_characters(stellage_number, book_number)
    
    # Преобразование символов в текст
    text = ''.join(characters)
    
    return text

def get_characters(stellage_number, book_number):
    # Мы получаем все возможные символы для этого стиллажа
    all_characters = get_all_characters(stellage_number)
    
    # Мы получаем символы, из которых состоит книга
    book_characters = get_book_characters(all_characters, book_number)
    
    return book_characters

def get_all_characters(stellage_number):
    # Мы получаем все возможные символы для этого стиллажа
    # Например, для стиллажа № 1 это будут все буквы алфавита, знаки препинания и точки
    # Вам нужно определить, какие символы включать в каждой стиллаж и реализовать здесь соответствующую логику

    # Мы вернем все возможные символы, состоящие из такого количества букв, которое равно номеру стойки
    return list(itertools.product('абвгдеёжзийклмнопрстуфхцчшщъыьэюя', repeat=stellage_number))

def get_book_characters(all_characters, book_number):
    # Мы получаем символы, из которых состоит книга
    # Например, если на полке 100 символов, а номер книги равен 1,
    # тогда первая книга будет состоять из первого символа в списке all_characters

    # Убедитесь, что номер книги не превышает количество символов в стеллаже
    if book_number > len(all_characters):
        raise ValueError('Неверный номер книги')
    
    # Мы получаем символы, из которых состоит книга
    book_characters = list(all_characters[book_number - 1])
    
    return book_characters

# Пример использован
stellage_number = int(input("Enter the rack number: "))
book_number = int(input("Enter the book number: "))
book_text = get_book_text(stellage_number, book_number)
print("Book: ",book_text,sep="\n")
