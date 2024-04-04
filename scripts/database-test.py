from myapp.models import User

def test_user_creation():
    user = User(username='test_user', email='test@example.com')
    assert user.username == 'test_user'
    assert user.email == 'test@example.com'