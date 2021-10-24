from playwright.sync_api import Page

class BasePage(object):
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "http://shyedhu-shop-react-app.s3-website-us-west-2.amazonaws.com"