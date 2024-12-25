from app import create_app, db
from app.model import *

app = create_app('dev')
@app.cli.command(help='Testing will perform')
def test():
    import unittest
    tests = unittest.TestLoader().discover(start_dir='tests', pattern='test_*.py')
    unittest.TextTestRunner(verbosity=2).run(tests)

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)