from pages.swag_labs import SwagLabs

class TestCheckSwag:
    def test_check_icon(self, browser):
        swag_labs_page = SwagLabs(browser, 'https://www.saucedemo.com/')
        swag_labs_page.visit()
        assert swag_labs_page.exist_icon()

    def test_check_username_field(self, browser):
        swag_labs_page = SwagLabs(browser, 'https://www.saucedemo.com/')
        swag_labs_page.visit()
        assert swag_labs_page.exist_username_field()

    def test_check_password_field(self, browser):
        swag_labs_page = SwagLabs(browser, 'https://www.saucedemo.com/')
        swag_labs_page.visit()
        assert swag_labs_page.exist_password_field()