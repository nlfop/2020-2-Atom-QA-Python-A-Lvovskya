import sqlalchemy
from sqlalchemy.orm import sessionmaker


class MysqlOrmConnection(object):
    def __init__(self, user, password, db_name):
        self.user = 'Nastya'
        self.password = 'Anastya040901'
        self.db_name = 'python_mysql'
        self.port = 3306
        self.host = 'LAPTOP-GGG2NIA2'

        self.connection = self.connect()

        session = sessionmaker(bind=self.connection)
        self.session = session()

    def get_connection(self, db_created=False):
        engine = sqlalchemy.create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{db}'.format(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            db=self.db_name if db_created else ''
        ))
        return engine.connect()

    def connect(self):
        connection = self.get_connection(db_created=False)

        connection.execute('DROP DATABASE IF EXISTS python_mysql')
        connection.execute('CREATE DATABASE python_mysql')
        connection.close()

        return self.get_connection(db_created=True)