from app import create_app, db
import unittest

class TestClient(unittest.TestCase):
    def setUp(self):
        app=create_app('test')
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home(self):
        response = self.client.get('/main/')
        self.assertIn('<ol', response.get_data(as_text=True))        