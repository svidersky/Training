from model.user import User
#from selenium_fixture import app


def test_login_with_valid_credentials(app):
    app.login(User.user_0000())


def test_login_with_invalid_credentials(app):
    app.logout()
    app.login(User.random())