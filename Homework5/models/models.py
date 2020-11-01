from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Access(Base):
    __tablename__ = 'access1'
    __table_args__ = {'python_mysql': 'utf8'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(16), nullable=False)
    def1 = Column(String(1), nullable=False, default='-')
    def2 = Column(String(1), nullable=False, default='-')
    date = Column(String(200), nullable=False)
    date_code = Column(String(5), nullable=False)
    type_ = Column(String(4), nullable=False)
    http1 = Column(String(4000), nullable=False)
    http2 = Column(String(8), nullable=False)
    code = Column(Integer, nullable=False)
    requests = Column(Integer, nullable=False)
    url = Column(String(4000), nullable=False, default='-')
    browser = Column(String(5000), nullable=False, default='-')
    def3 = Column(String(1), nullable=False, default='-')

    def __repr__(self):
        return f"<Access(" \
               f"ip='{self.ip}'," \
               f"def1='{self.def1}', " \
               f"def2='{self.def2}', " \
               f"date='{self.date}'" \
               f"date_code='{self.date_code}'," \
               f"type='{self.type_}'," \
               f"http1='{self.http1}'," \
               f"http2='{self.http2}'," \
               f"code='{self.code}'," \
               f"requests='{self.requests}',"\
               f"url='{self.url}'," \
               f"browser='{self.browser}'," \
               f"def3='{self.def3}'," \
               f")>"



