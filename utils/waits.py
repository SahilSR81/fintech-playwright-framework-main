from playwright.sync_api import expect


class WaitUtils:

    @staticmethod
    def wait_for_visible(locator):
        expect(locator).to_be_visible()

    @staticmethod
    def wait_for_url(page, partial_url):
        expect(page).to_have_url(partial_url)