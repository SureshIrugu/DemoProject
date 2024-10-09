import pytest
from playwright.sync_api import expect
from automation.tests.contest import set_up_tear_down
from automation.src.pages.LoginPage import LoginPage
from automation.src.utils.data import username, password, product_name, product_name_1, product_name_3


def test_product_details(set_up_tear_down) -> None:
    """verify product details after selecting product"""
    page = set_up_tear_down
    credentials = {'username': username, 'password': password}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.click_on_item_link()
    expect(products_p.get_add_remove_cart_locator(product_name))

def test_product_filter_a_to_z(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': username, 'password': password}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.click_filter_sort_by_name(order='za')
    expect(products_p.get_add_remove_cart_locator(product_name_3))

def test_add_to_cart(set_up_tear_down) -> None:
    """
    Verify that add to cart button is changed to Remove when clicked
    """
    page = set_up_tear_down
    credentials = {'username': username, 'password': password}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.click_add_to_cart_or_remove(product_name)
    expect(products_p.get_add_remove_cart_locator(product_name)).to_have_text("Remove")

def test_remove_product_from_cart(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.click_add_to_cart_or_remove(product_name_1)
    products_p.click_add_to_cart_or_remove(product_name_1)
    expect(products_p.get_add_remove_cart_locator(product_name_1)).to_have_text("Add to cart")