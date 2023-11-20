if __name__ == "__main__":
    print("Algorithme Tinkoff: create sql")


    table_name = "(select lower(word) as word, n0, n1, n2, n3, n4 from word_of_5_symbols) "
    symbol_not_in_word = list("арбзфиксчгнмт")
    symbol_in_word_but_not_index = [['х', 0]]
    symbol_in_word_index = [['у', 3], ['о', 1]]

    sql = f'select * from {table_name} as res where '

    sql += "("
    for s in symbol_not_in_word:
        sql += f"word not like '%{s}%' and "
    sql += " 1=1) and "

    sql += "("
    for s in symbol_in_word_but_not_index:
        sql += f"(word like '%{s[0]}%' and not n{s[1]} = '{s[0]}') and "
    sql += " 1=1) and "

    sql += "("
    for s in symbol_in_word_index:
        sql += f"n{s[1]} = '{s[0]}' and "
    sql += " 1=1)"

    print(sql)

    import psycopg2
    conn = psycopg2.connect(database="postgres",
                            host="localhost",
                            user="postgres",
                            password="postgrespw",
                            port="49153")
    cursor = conn.cursor()
    res = cursor.execute(sql)

    # FETCH ALL THE ROWS FROM THE CURSOR
    data = cursor.fetchall()

    # PRINT THE RECORDS
    for row in data:
        print(row)
