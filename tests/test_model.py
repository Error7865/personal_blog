import unittest
from app import create_app, db
from app.model import Admin

class TestModel(unittest.TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.a=Admin(name='Robin', password = 'badman')
        db.session.add(self.a)
        db.session.commit()
        # self.client=self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_admin_password_verification(self):
        

        #verify password
        self.assertTrue(self.a.verify_password('badman'))
        self.assertFalse(self.a.verify_password('batman'))

    def test_get_password(self):
        #try to access password
        with self.assertRaises(NameError):
            print(self.a.password)
