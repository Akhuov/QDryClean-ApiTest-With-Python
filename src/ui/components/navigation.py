from playwright.sync_api import Page

class Navigation:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self, page_name: str) -> Page:
        return self.page