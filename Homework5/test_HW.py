import pymysql.cursors


connection = pymysql.connect(host='LAPTOP-GGG2NIA2',
                             user='Nastya',
                             password='Anastya040901',
                             db='python_mysql',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

print("connect successful")


preods_query = """
           CREATE TABLE IF NOT EXISTS access12 (
             ip varchar(200) NOT NULL,
             def1 char(1) NOT NULL DEFAULT '-',
             def2 char(1) NOT NULL DEFAULT '-',
             date varchar(200) NOT NULL,
             date_code varchar(5) NOT NULL,
             type varchar(1000) NOT NULL,
             http1 varchar(4000) NOT NULL,
             http2 varchar(8) NOT NULL,
             code int NOT NULL,
             requests varchar(10) NOT NULL,
             url varchar(4000) NOT NULL DEFAULT '-',
             browser varchar(6500) NOT NULL DEFAULT '-',
             def3 char(1) NOT NULL DEFAULT '-'
           )
           """
cur = connection.cursor()
cur.execute(preods_query)

try:
    text_file = open("C://Users//ulvov//Downloads//access.log", "r")
except IOError:
    print("error opening the file")
    exit(2)
with text_file:
    lines = [line.split() for line in text_file]
    for str in range(len(lines)):
        print(str)
        ip = lines[str][0]
        date = lines[str][3].replace("[", "")
        date_code = lines[str][4].replace("]", "")
        type_ = lines[str][5].replace('"', "")
        http1 = lines[str][6].replace("'","").replace('=','equal')
        http2 = lines[str][7].replace('"', "")
        code = lines[str][8]
        requests = lines[str][9]
        url = lines[str][10].replace('"', "").replace("'","").replace('=','')
        browser = lines[str][11]
        s = lines[str][11]
        i = 11
        while s[-1:len(s)] != '"':
            i += 1
            s = lines[str][i]
            browser += s
        browser = browser.replace('"', "")
        browser = browser.replace("'", "")
        insert_query = f"INSERT INTO access12(ip, date, date_code,type,http1,http2,code,requests,url,browser) " \
                               f"VALUES('{ip}', '{date}', '{date_code}', '{type_}', '{http1}', '{http2}', '{code}', '{requests}', '{url}', '{browser}')"
        cur.execute(insert_query)


cur.execute('SELECT * FROM access12')
res = cur.fetchall()
print(res)
connection.commit()
cur.close()