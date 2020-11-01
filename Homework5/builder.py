from faker import Faker

from mysql_client.mysql_client import MysqlConnection

fake = Faker(locale='ru_RU')


class MysqlBuilder(object):
    def __init__(self, connection: MysqlConnection):
        self.connection = connection

    def add_req(self):
        ip = "134.249.53.185"
        date = "27/May/2016:03:32:09"
        date_code = "+0200"
        type_ = "POST"
        http1 = "http://almhuette-raith.at/administrator/index.php"
        http2 = "HTTP/1.1"
        code = 200
        requests = 4498
        url = "-"
        browser = "-"
        insert_query = f"INSERT INTO access(ip, date, date_code,type,http1,http2,code,requests,url,browser) " \
                       f"VALUES('{ip}', '{date}', '{date_code}', '{type_}', '{http1}', '{http2}', '{code}', '{requests}', '{url}', '{browser}')"

        self.connection.execute_query(insert_query)
