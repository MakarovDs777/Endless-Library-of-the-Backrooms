import itertools

def get_book_text(stellage_number, book_number):
    # Получаем символы, из которых состоит книга
    characters = get_characters(stellage_number, book_number)
    
    # Преобразуем символы в текст
    text = ''.join(characters)
    
    return text

def get_characters(stellage_number, book_number):
    # Получаем все возможные символы для данного стеллажа
    all_characters = get_all_characters(stellage_number)
    
    # Получаем символы, из которых состоит книга
    book_characters = get_book_characters(all_characters, book_number)
    
    return book_characters

def get_all_characters(stellage_number):
    # Получаем все возможные символы для данного стеллажа
    # Например, для стеллажа номер 1 это будут все буквы алфавита, знаки препинания и точки
    # Вам нужно определить, какие символы включать в каждый стеллаж
    # и реализовать соответствующую логику здесь
    
    # Вернем все возможные символы, состоящие из стольких букв, сколько равно номеру стеллажа
    return list(itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=stellage_number))

def get_book_characters(all_characters, book_number):
    # Получаем символы, из которых состоит книга
    # Например, если в стеллаже есть 100 символов, а номер книги равен 1,
    # то первая книга будет состоять из первого символа в списке all_characters
    
    # Проверяем, что номер книги не превышает количество символов в стеллаже
    if book_number > len(all_characters):
        raise ValueError('Неверный номер книги')
    
    # Получаем символы, из которых состоит книга
    book_characters = list(all_characters[book_number - 1])
    
    return book_characters

# Пример использования
stellage_number = 2
book_number = 1
book_text = get_book_text(stellage_number, book_number)
print(book_text)
