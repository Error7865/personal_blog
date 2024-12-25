
class Base:
    SECRET_KEY='don\'t guess me'

class Dev(Base):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    
class Test(Base):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


config={
    'dev': Dev,
    'test': Test
}