

import pytest

from models.models import Access
from mysql_orm_client.mysql_orm_client import MysqlOrmConnection
from orm_builder import MysqlOrmBuilder


@pytest.fixture(scope='session')
def mysql_orm_client():
    return MysqlOrmConnection(user='Nastya', password='Anastya040901', db_name='python_mysql')


class TestMysqlOrm(object):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client):
        self.mysql: MysqlOrmConnection = mysql_orm_client
        self.builder: MysqlOrmBuilder = MysqlOrmBuilder(connection=self.mysql)

    def test(self):
        self.builder.add_req()
        access_code_200 = self.mysql.session.query(Access).filter_by(code=200)
        print('\ncode=200 access1: ' + str(access_code_200))





