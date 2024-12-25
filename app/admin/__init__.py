from flask import Blueprint
import os
from ..model import Admin

admin=Blueprint('admin', __name__, url_prefix='/open')
@admin.before_request
def load_admin():
    admin = os.environ.get('ADMIN')
    if Admin.query.filter_by(name=admin).first() is None:
        #Admin name and password not load
        Admin.load_admin()

    


from . import views