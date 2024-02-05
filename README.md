# Бесконечная библиотека бэкрумса

[![1ye5qkw3n3fc1.webp](https://i.postimg.cc/DZzYFrjs/1ye5qkw3n3fc1.webp)](https://postimg.cc/5HZmSCMN)

Бесконечная библиотека бэкрумса является продолжением идеи вавилонской библиотеки Борхеса, с учетом того, что закулисная библиотека не ограничена количеством страниц, а бесконечна, закулисная библиотека будет разделена на стеллажы, который обозначаются числом, равным количеству символов последовательности в книге, например, если это стеллаж № 1, то все книги в нем с одной буквой и все варианты всех возможных букв на месте одной буквы, включая заглавные и строчные, а также включая знаки препинания и точки. Количество стиллажей бесконечно.

Идея основана на подсобных помещениях бесконечных библиотек:

Level_4732:   https://web.archive.org/web/20221001125648/https://backrooms.fandom.com/wiki/Level_4732

Level_230:   https://web.archive.org/web/20221003224540/https://backrooms.fandom.com/wiki/Level_230

В этом примере функция get_all_characters использует функцию itertools.product для генерации всех возможных символов, состоящих из стольких букв, сколько равно номеру стеллажа. Затем функция get_book_characters получает символы, из которых состоит книга, и возвращает их в виде списка.

Вы можете запустить этот код и передать номер стеллажа и номер книги в качестве входных данных, чтобы получить текст книги.

Я сделал только набросок... Я надеюсь, что у кого-то может возникнуть представление о том, как в полной мере подойти к реализации этого образа бесконечной библиотеки в будущем... А также о возможности разработки этого образа в будущем... Мне будет достаточно наиболее точно описать идею реализации этого образа, и тогда я смогу его запрограммировать.

И добавлю от себя, что Вавилонская библиотека - это прошлый век, лучше не изобретать велосипед, а сделать что-то самостоятельно в архивах сайта backrooms есть масса идей для реализации вроде того же бесконечного кинотеатра с бесконечным количеством фильмов, и это было бы неплохо воплотить эту идею в жизнь...

Я надеюсь, что однажды мы создадим полноценную закулисную игру с бесконечной процедурной генерацией уровней, сущностями, похожими на те, что нарисовал Тревор Хендерсон, NPC, заданиями, компаниями, и что графика будет неотличима от реальности, и что будет постоянный сетевой мультиплеер, это было бы действительно круто!
