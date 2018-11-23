# @Author  : xy.zhang
# @Email   : zhangxuyi@wanshare.com
# @Time    : 18-11-19

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50))
    password_hash = Column(String(64))
    salt = Column(String(64))
    
    def __repr__(self):
        return f"<User(id={self.id}, user_name={self.user_name}, password_hash={self.password_hash}, salt={self.salt}>"
    

if __name__ == '__main__':
    engine = create_engine("sqlite:///data.db3", echo=True)
    Base.metadata.create_all(engine)


