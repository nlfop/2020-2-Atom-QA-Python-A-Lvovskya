
from models.models import Access
from mysql_orm_client.mysql_orm_client import MysqlOrmConnection


class MysqlOrmBuilder(object):
    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = self.connection.connection.engine

    def add_req(self):
        req = Access(
            ip="134.249.53.185",
            date="27/May/2016:03:32:09",
            date_code="+0200",
            type_="POST",
            http1="http://almhuette-raith.at/administrator/index.php",
            http2="HTTP/1.1",
            code=200,
            requests=4498,
            url="-",
            browser="-",
        )
        self.connection.session.add(req)
        self.connection.session.commit()

        return req
