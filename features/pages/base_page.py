class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.implicit_wait = 15

base_url = "http://18.225.209.250:8203/"