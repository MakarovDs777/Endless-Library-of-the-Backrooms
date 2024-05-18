# Бесконечная библиотека бэкрумса

[![1ye5qkw3n3fc1.webp](https://i.postimg.cc/DZzYFrjs/1ye5qkw3n3fc1.webp)](https://postimg.cc/5HZmSCMN)

Бесконечная библиотека бэкрумса является продолжением идеи вавилонской библиотеки Борхеса ([видео](https://youtu.be/zFr14SA81zY?si=IeiR5Nwplx6Az_Pv&t=1034)), с учетом того, что закулисная библиотека не ограничена количеством книг, и соответственно количество страниц, и самих книг в ней от одного до бесконечности включая саму бесконечность в то время как вавилонская библиотека Борхеса имеет всего лишь каких-то жалких 25¹³¹²⁰⁰⁰ всевозможных вариаций книг, и 25³²⁰⁰ всевозможных различных страниц... Закулисная библиотека разделена на стеллажы, который обозначаются числом, равным количеству символов последовательности в книге, например, если это стеллаж № 1, то все книги в нем с одним символом и все варианты всех возможных символов на месте одного символа, включая буквы заглавные и строчные, а также включая знаки препинания и точки, если это стеллаж № 2 тогда в каждой книге по 2 символа и все варианты расположения всех возможных букв, цифр, и знаков препинания на месте этих двух символов ну и т.д.

И если библиотека Борхеса это такое огромное здание куб где каждая комната разделена на 6 стеллажей по три полки, на каждой из которых 12 книг объемом по 420 страниц. То  бесконечная бибилотека бэкрумса это такой бесконечный круглый небоскреб расположенный где-то в далеком космосе построенный сверху вниз, и каждый этаж отсчитывается от верхнего к нижнему где на самом вверху самая первый этаж на котором первый стеллаж с книгами в один символ, ниже второй стеллаж где каждая книга с 2 символами, и т.д. Вплоть до самого нижнего бесконечно конечного этажа где есть последний стеллаж с бесконечным числом книг каждая из которых с бесконечным числом страниц .
[![68747470733a2f2f692e706f7374696d672e63632f714d4b774b4d63472f3035333331326464643038623463643739623730.jpg](https://i.postimg.cc/xC6yVdzW/68747470733a2f2f692e706f7374696d672e63632f714d4b774b4d63472f3035333331326464643038623463643739623730.jpg)](https://postimg.cc/r0ttSMgJ)

Идея основана на закулисных библиотеках бэкрумса, и все уровни библиотек которые мне удалось найти:

[33](https://web.archive.org/web/20221002013505/https://backrooms.fandom.com/wiki/Level_33), [477](https://web.archive.org/web/20221004062455/https://backrooms.fandom.com/wiki/Level_477), [795](https://web.archive.org/web/20221003022315/https://backrooms.fandom.com/wiki/Level_795), [813](https://web.archive.org/web/20221013151359/https://backrooms.fandom.com/wiki/Level_813), 
[1142](https://web.archive.org/web/20221013151359/https://backrooms.fandom.com/wiki/Level_1142), [4732](https://web.archive.org/web/20221001125648/https://backrooms.fandom.com/wiki/Level_4732), [230](https://web.archive.org/web/20221003224540/https://backrooms.fandom.com/wiki/Level_230)

Я сделал только набросок... Я надеюсь, что у кого-то может возникнуть представление о том, как в полной мере подойти к реализации этого образа бесконечной библиотеки в будущем... А также о возможности разработки этого образа в будущем... Мне будет достаточно наиболее точно описать идею реализации этого образа, и тогда я смогу его запрограммировать.

Я думаю, что для того, чтобы полностью реализовать идею бесконечной закулисной библиотеки, нам нужно использовать искусственный интеллект, который бы сортировал все действия со всеми видами знаний всеми возможными способами, и описывал эти итерации только таким образом, которым мы создадим что-то значимое для себя, где мы сможем найти что-то для себя. 

# Endless-Library-of-the-Backrooms
В этом примере функция get_all_characters использует функцию itertools.product для генерации всех возможных символов, состоящих из стольких букв, сколько равно номеру стеллажа. Затем функция get_book_characters получает символы, из которых состоит книга, и возвращает их в виде списка.

Вы можете запустить этот код и передать номер стеллажа и номер книги в этом стиллаже в качестве входных данных, чтобы получить текст книги.

# Endless-Library-with-Endless
Переписанный код таким образом что-бы можно было выводить последний бесконечный стеллаж если ввести ∞ с бесконечном числом книг каждая из которых имеет бесконечное числом страниц и не повторяет другие.

# Реквием о бесконечных бесконечностях
Больше всего мне понравился уровень 33 он представляет собой комбинацию всевозможных книг на всевозможных языках, которые вы только можете придумать, включая языки других инопланетных цивилизаций и т.д. И я сделал набросок реализации только 33-го уровня. Следовательно, есть к чему стремиться! Хотя я бы все уровни этих библиотек отнес бы к подуровню общего какого нибудь одного уровня с бесконечным числом всевозможных библиотек, типа уровня бесконечной библиотеки с бесконечным числом всевозможных ДНК, или например уровня бесконечной библиотеки с бесконечным числом чертежей, ну и так далее... и в этом наверное будет одна из проблем в дальнейшем потому что можно придумать бесконечное число библиотек, и поэтому я бы просто сделал разные типы сортировок по флагам например (бесконечные уровни, конечные уровни, обычные, экзотические, нетривиальная геометрия, нетривиальная физика, нетривиальная химия, и т.д.), и сделал бы свой уровень бесконечного небоскреба как такой хаб с бесконечным числом всевозможных библиотек, вот что действительно надо реализовать бесконечный фандом заулисья бэкрумса то есть сделать так что-бы нейросеть сделал все всевозможные написании изменений продолжений всех образов всех уровней [у меня уже есть зарисовка](https://disk.yandex.ru/i/LvmwoQLWi8fAZA), и по ним написала бы бесконечное число реализаций этих уровней... Например бесконечное число уровней библиотек, бесконечное число уровней города, бесконечное число уровней бассейнов вот что действительно было бы круто! Я надеюсь что однажды мы создадим полноценную закулисную приключенческую компьютерную AAA+ игру с какой нибудь полноценной компанией с элементами интерактивного кинематографа наподобии Detroit: Become Human, и  бесконечной процедурной генерацией всего - уровней, сущностей, похожими на те, что нарисовал [Тревор Хендерсон](https://www.youtube.com/watch?v=0rix31kJwPg), NPC, заданий, компаний, и главное, чтобы графика была неотличима от реальности, и что будет постоянный сетевой мультиплеер, и что-бы каждый пользователь смог-бы создавать свои бесконечные процедурно сгенерированые уровни загружать их на сервер, и другие бы пользователи могли-бы скачивать эти уровни, это было бы действительно круто! Я уже даже вижу себе эту такую полноценную трилогию типа в первой части бэкрумс только зарождается это такое место для избранных где бродят только сотрудник организации B.I.G, M.E.G, ASYNC, и изредка каким-то чудом случайные выпавшие из реальности люди которые пытаются оттуда выбраться... Во второй части происходит такой типа сбой, и бэкрумс перестает быть этаким местом для избранных все выходит из под контроля короче туда начинают выпадать из реальности все подряд, и становится некий такой золотой век закулисья где происходит бурное развитие, и его исследование... Ну и в третий части типа такая завершающаяся стадия когда бэкрумс стал чем-то обыденным став полностью уже поделен на зоны различных группировок, и организаций которые контролируют различные территории, и враждуют между собой преследуя свои личные интересы. И в итоге все приходит короче к общему знаменателю где игрок главный протагонист игры, который в итоге решает судьбу мира.

# От себя 
И добавлю от себя, что Вавилонская библиотека - это прошлый век, лучше не изобретать велосипед, а сделать что-то самостоятельно от себя в архивах сайта фандома backrooms есть масса идей для реализации... Короче это было бы неплохо воплотить эту идею в жизнь... С учётом того что это как бы то за что я люблю эту идею бэкрумса потому что идея бэкрумса можно развивать бесконечно, и находить всегда для себя что-то новое! Поэтому бэкрумс он будет актуален всегда! Просто в какие-то периоды его популярность будет угасать а в какие-то подниматься... Сам фандом закулисья я не люблю так как мочератор гавноед постоянно удаляет мои уровни, удалил мои уровень про бесконечные океан воздушных шариков, удалил мой уровень -88888888 бесконечных фракталов, и у уровень суперцентрали но в архивах сайта можно найти что-то интереснное... Поэтому я просто оставлю ссылку на свои уровни в [яндекс диске](https://disk.yandex.ru/d/eJ97GnHKx3SVVw)
