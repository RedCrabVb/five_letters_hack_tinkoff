# five_letters_hack_tinkoff
хак на мини игру "пять букв" в приложении тинькофф

Нужно создать БД и прописать подключение в скрипте load_file_to_db.py, затем запустить его (данные для заполнения таблиц брал тут https://github.com/danakt/russian-words)
После нужно в файле create_sql.py отредактировать подключение к БД и заполнять массив необходимыми значениями, пример:

```py
    symbol_not_in_word = list("арбзфиксчгнмт")
    symbol_in_word_but_not_index = [['х', 0]]
    symbol_in_word_index = [['у', 3], ['о', 1]]
```

Затем запустить скрипт create_sql.py


Подробнее про работу тут: https://vk.com/@aboroday_1-kak-haknut-tinkoff-prilozhenie-ili-moe-prof-vygoranie
