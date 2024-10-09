from playwright.sync_api import  expect
from automation.src.pages.LoginPage import LoginPage
from automation.tests.contest import set_up_tear_down
from automation.src.utils.data import username, password


def test_logout(set_up_tear_down) -> None:

    page = set_up_tear_down
    credentials = {'username': username, 'password': password}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.do_logout()
    expect(login_p.login_button).to_be_visible()