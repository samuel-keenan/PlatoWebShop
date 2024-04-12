from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = {

#locators for the Billing Details section
        "first name": "//input[@id='billing_first_name']",
        "last name": "//input[@id='billing_last_name']",
        "company name": "//input[@id='billing_company']",
        "street address": "//input[@id='billing_address_1']",
        "unit number": "//input[@id='billing_address_2']",
        "city": "//input[@id='billing_city']",
        "province": "",
        "postal code": "//input[@id='billing_postcode']",
        "phone": "//input[@id='billing_phone']",
        "email": "//input[@id='billing_email']",
        "order notes": "//textarea[@id='order_comments']",
#locators for the Order Tails
        "credit card number": "//input[@id='sandbox_creditcard-card-number']",
        "expiry": "//input[@id='sandbox_creditcard-card-expiry']",
        "card code": "//input[@id='sandbox_creditcard-card-cvc']",
        "place order": "//button[@id='place_order']"

    }