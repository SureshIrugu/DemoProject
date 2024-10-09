from automation.src.pages.CartPage import CartPage


class ProductListPage:

    def __init__(self, page):
        self.page = page
        self._products_header = page.locator("span.title")
        self._burger_menu = page.locator("button#react-burger-menu-btn")
        self._logout_btn = page.locator("#logout_sidebar_link")
        self._item_name = page.locator("//div[text()='Sauce Labs Backpack']")
        self._item_inventory = page.locator('[data-test="inventory-item-name"]')
        self._add_to_cart = page.locator("//div[text()='Sauce Labs Backpack']//button")
        self._cart_icon = page.locator("a.shopping_cart_link")
        self._filter = self.page.locator("select.product_sort_container")
        self._filter_name = page.locator("[data-test='product-sort-container']")


    @property
    def product_header(self):
        """It returns locator or selector for product header text"""
        return self._products_header

    def click_on_item_link(self):
        self._item_name.click()

    def click_burger_menu_btn(self):
        """This will click on Burger menu icon from header"""
        self._burger_menu.click()

    def click_logout(self):
        """This will click on logout"""
        self._logout_btn.click()

    def do_logout(self):
        """Logout from the sauce demo"""
        self.click_burger_menu_btn()
        self.click_logout()

    def get_add_remove_cart_locator(self, product):
        """This will return locator of Add to cart button or Remove button"""
        return self.page.locator(f"//div[text()='{product}']/ancestor::div[@class='inventory_item_label']/following-sibling::div//button")

    def click_add_to_cart_or_remove(self, product):
        self.get_add_remove_cart_locator(product).click()
        return self

    def click_cart_icon(self):
        self._cart_icon.click()
        return CartPage(self.page)

    def click_filter_sort_by_name(self, order='az'):
        self._filter.click()
        self._filter.select_option(order)