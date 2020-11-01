import pytest

from mysql_client.mysql_client import MysqlConnection
from builder import MysqlBuilder


@pytest.fixture(scope='session')
def mysql_client():
    return MysqlConnection(user='Nastya', password='Anastya040901', db_name='python_mysql')


class TestMysql:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql: MysqlConnection = mysql_client
        self.builder = MysqlBuilder(self.mysql)

    def test(self):
        self.builder.add_req()

        res = self.mysql.execute_query('SELECT * FROM access')
        print('\n ' + str(res))