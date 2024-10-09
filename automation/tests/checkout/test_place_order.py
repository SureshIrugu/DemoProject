from playwright.sync_api import expect
from automation.tests.contest import set_up_tear_down
from automation.src.pages.LoginPage import LoginPage
from automation.src.utils.data import username, password,product_name_2

def test_place_order(set_up_tear_down) -> None:
    """
    Verify that user is able to place an order successfully
    """
    page = set_up_tear_down
    credentials = {'username': username, 'password': password}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    checkout_p = products_p.click_add_to_cart_or_remove(product_name_2)\
        .click_cart_icon()\
        .click_checkout_button()\
        .enter_checkout_details("Fn12", "Ln12", "0011")\
        .click_continue()\
        .click_finish_button()
    expect(checkout_p.get_confirm_message()).to_have_text("Thank you for your order!")