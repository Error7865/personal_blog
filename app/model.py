from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import mapped_column
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from flask_login import UserMixin
import os
import re
from . import db, login_manager

class Admin(db.Model, UserMixin):
    __tablename__= 'admin'
    id= mapped_column('ID', Integer, primary_key=True)
    name = mapped_column('NAME', String, nullable=False)
    pswd = mapped_column('PASSWORD', String(300), unique= True)

    @property
    def password(self):
        raise NameError('Passowrd can\'t access.')

    @password.setter
    def password(self, value):
        self.pswd = generate_password_hash(value)

    @staticmethod
    def load_admin():
        a = Admin(
            name=os.environ.get('ADMIN'),
            password=os.environ.get('PASSWORD')
            )
        db.session.add(a)
        db.session.commit()


    def verify_password(self, psw:str)->bool:
        return check_password_hash(self.pswd, psw)
    
    def __repr__(self):
        return f'<id: {self.id}> <name: {self.name}>'
    

class Article(db.Model):
    __tablename__='article'
    id= mapped_column('ID', Integer, primary_key=True)
    name = mapped_column('Name', String(200), unique=True, nullable=False)
    timestamp = mapped_column('TimeStamp', DateTime, default=datetime.now())
    markdown_text = mapped_column('markdown', String, unique=True)
    html_text = mapped_column('html', String, unique=True)
    
    def to_json(self):
        '''This will convert data to json'''
        return {
                'title': self.name,
                'markdown': self.markdown_text
            }

    @staticmethod
    def only_txt(st: str):
        '''This will return string after extract all html
        tags'''
        pattern= '<[A-Za-z0-9]*>|</[A-Za-z0-9]*>'
        return re.sub(pattern, '',st)

    def __repr__(self):
        return f'<id: {self.id}> <name: {self.name}> '


@login_manager.user_loader
def load_user(id:int):
    return Admin.query.get(id)