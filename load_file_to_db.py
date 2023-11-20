if __name__ == "__main__":
    print("Algorithme Tinkoff")
    #AI: python connect to postgres and example insert
    # pip install psycopg2
    import psycopg2
    conn = psycopg2.connect(database="postgres",
                            host="localhost",
                            user="postgres",
                            password="postgrespw",
                            port="49153")
    cursor = conn.cursor()
    cursor.execute("""drop table if exists word_of_5_symbols""")
    cursor.execute("""create table word_of_5_symbols (
        id bigserial,
        n0 varchar,
        n1 varchar,
        n2 varchar,
        n3 varchar,
        n4 varchar, 
        word varchar
    )""")

    opt = 0
    count_word = 0
    with open('all_word2.txt', mode="r", encoding="utf-8") as f:

        for line in f:
            count_word += 1
            if len(line) == 6:
                cursor.execute(
                    f"INSERT INTO word_of_5_symbols (n0, n1, n2, n3, n4, word) VALUES (%s, %s, %s, %s, %s, %s)",
                    (line[0], line[1], line[2], line[3], line[4], line)
                )
                opt += 1
                if opt > 1_000:
                    conn.commit()
                    opt = 0
                    print(count_word)
    conn.commit()
    conn.close()
    
    #select * from word_of_5_symbols where (word like '%а%' and word like '%б%' and word like '%о%') and (not n1 = 'о' and not n0 = 'а' and not n1 = 'а' and not n2 = 'б' and not n0 = 'б') and (not word like '%р%' and not word like '%у%' and not word like '%н%' and not word like '%л%' and not word like '%ь%' and not word like '%к%'); 
    # output:
    #  2332 | в  | д  | о  | б  | а  | вдоба+\

	#  13804 | о  | б  | а  | ч  | е  | обаче+\

	#  13823 | о  | б  | д  | а  | в  | обдав+\

	#  13824 | о  | б  | д  | а  | й  | обдай+\

	#  13826 | о  | б  | д  | а  | м  | обдам+\

	#  13828 | о  | б  | д  | а  | ю  | обдаю+\

	#  13838 | о  | б  | е  | д  | а  | обеда+\

	#  13852 | о  | б  | е  | т  | а  | обета+\

	#  13856 | о  | б  | е  | щ  | а  | обеща+\

	#  13857 | о  | б  | ж  | а  | т  | обжат+\

	#  13870 | о  | б  | и  | д  | а  | обида+\

	#  13877 | о  | б  | и  | ж  | а  | обижа+\

	#  13883 | о  | б  | и  | т  | а  | обита+\

	#  13950 | о  | б  | о  | д  | а  | обода+\

	#  13956 | о  | б  | о  | ж  | а  | обожа+\

	#  13957 | о  | б  | о  | з  | а  | обоза+\

	#  14006 | о  | б  | с  | т  | а  | обста+\

	#  14038 | о  | б  | х  | а  | ю  | обхаю+\

	#  14039 | о  | б  | х  | в  | а  | обхва+\

	#  14047 | о  | б  | щ  | а  | я  | общая+\

	#  14071 | о  | б  | ы  | ч  | а  | обыча+\

	#  14076 | о  | б  | я  | з  | а  | обяза+\

	#  14242 | о  | з  | а  | б  | о  | озабо+\

	#  14704 | о  | с  | о  | б  | а  | особа+\

	#  15108 | о  | ш  | и  | б  | а  | ошиба+\

	#  19077 | с  | д  | о  | б  | а  | сдоба+\

	#  25395 | ч  | т  | о  | б  | а  | чтоба+  
