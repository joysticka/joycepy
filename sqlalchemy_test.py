from sqlalchemy import create_engine,  Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('posgresql://postgres:sistemas2017@localhost:5432/kmmx')
Base = declarative_base()

class User(Base):
	__tablename__= 'users'
	id = Column(Integer, primary_key = True)
	nickname = Column(String)
	name = Column(String)
	passwd = Column(String)

	def __repr__(self):
		return '<User(nickname={nickname}, name = {name}, passwd={passwd})>'.format(nickname=self.nickname,
																					name=self.name,
																					passwd=self.passwd)
	def __str__(self):
		return '<User(nickname={nickname}, name = {name}, passwd={passwd})>'.format(nickname=self.nickname,
																					name=self.name,
																					passwd=self.passwd)

Base.metadata.create_all(engine)
Base.metadata.bind= engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

user = User(nickname='luis1', name='luis', passwd='1234')
session.add(user)
session.commit()