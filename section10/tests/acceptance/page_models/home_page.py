from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_models.base_page import BasePage


class HomePage(BasePage):

    @property
    def url(self):
        return super(HomePage, self).url + '/'


    @property
    def blog_link(self):
        return self.driver.find_elemt(*HomePageLocators.NAVIGATION_LINK)





