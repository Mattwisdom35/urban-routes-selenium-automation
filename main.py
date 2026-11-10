import time
import data
import helpers
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pages import UrbanRoutesPage

# NOTE: This is a sample of the test suite (4 of 8 tests).
# The full solution is kept private because it is an active TripleTen course project.


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # 1. Check if the server is up and reachable
        if not helpers.is_url_reachable(data.urban_routes_url):
            raise Exception("Urban Routes server is not reachable. Please check the URL.")

        # 2. Enable Chrome performance logs to retrieve the SMS code
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}

        # 3. Initialize the driver and maximize the window
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    # 1. Set Route Test
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)

        address_from = data.address_from
        address_to = data.address_to

        page.enter_from_location(address_from)
        page.enter_to_location(address_to)

        assert page.get_from_location() == address_from, f"Expected {address_from}, got {page.get_from_location()}"
        assert page.get_to_location() == address_to, f"Expected {address_to}, got {page.get_to_location()}"

    # 2. Select Supportive Tariff Test
    def test_select_supportive_plan(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)

        page.enter_from_location(data.address_from)
        page.enter_to_location(data.address_to)
        time.sleep(1)

        page.click_call_a_taxi_button()
        time.sleep(1)

        page.select_supportive_plan()
        time.sleep(1)

        assert page.is_supportive_plan_selected() == True, "Supportive plan is not selected!"

    # 3. Fill Phone Number & SMS Verification Test
    def test_fill_phone_number(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)

        page.enter_from_location(data.address_from)
        page.enter_to_location(data.address_to)
        time.sleep(1)
        page.click_call_a_taxi_button()
        time.sleep(1)
        page.select_supportive_plan()
        time.sleep(1)

        page.click_phone_field()
        time.sleep(1)
        page.enter_phone_number(data.phone_number)
        time.sleep(1)
        page.click_next_button()
        time.sleep(1)

        code = helpers.retrieve_phone_code(self.driver)
        page.enter_confirmation_code(code)
        time.sleep(1)
        page.click_confirm_button()
        time.sleep(1)

        assert data.phone_number in page.get_phone_number_text(), f"Expected {data.phone_number} in {page.get_phone_number_text()}"

    # 4. Order Blanket and Handkerchiefs Test
    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)

        page.enter_from_location(data.address_from)
        page.enter_to_location(data.address_to)
        time.sleep(1)
        page.click_call_a_taxi_button()
        time.sleep(1)
        page.select_supportive_plan()
        time.sleep(1)

        page.toggle_blanket_and_handkerchiefs()
        assert page.is_blanket_selected() == True

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver.quit()
