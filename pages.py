from selenium.webdriver.common.by import By

# NOTE: Page object for the sample tests only.
# Locators and methods for the remaining tests are kept private.


class UrbanRoutesPage:
    # --- LOCATORS ---
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
    SUPPORTIVE_PLAN_LOCATOR = (By.XPATH, '//div[contains(@class, "tcard") and .//div[text()="Supportive"]]')

    # Phone Locators
    PHONE_FIELD_BUTTON_LOCATOR = (By.XPATH, '//div[@class="np-text" and text()="Phone number"]')
    PHONE_INPUT_LOCATOR = (By.ID, 'phone')
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Next"]')
    CONFIRMATION_CODE_INPUT_LOCATOR = (By.ID, 'code')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Confirm"]')
    PHONE_NUMBER_LABEL_LOCATOR = (By.XPATH, '//div[@class="np-text"]')

    # Requirements Locators (Blanket & Handkerchiefs)
    BLANKET_SLIDER_LOCATOR = (By.XPATH,
                              '//div[contains(text(), "Blanket and handkerchiefs")]/following-sibling::div//span[@class="slider round"]')
    BLANKET_CHECKBOX_LOCATOR = (By.XPATH,
                                '//div[contains(text(), "Blanket and handkerchiefs")]/following-sibling::div//input')

    def __init__(self, driver):
        self.driver = driver

    # --- METHODS (Page Actions) ---
    def enter_from_location(self, from_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def get_from_location(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute('value')

    def get_to_location(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute('value')

    def click_call_a_taxi_button(self):
        self.driver.find_element(*self.CALL_TAXI_BUTTON_LOCATOR).click()

    def select_supportive_plan(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR).click()

    def is_supportive_plan_selected(self):
        card = self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR)
        card_class = card.get_attribute("class")
        return "active" in card_class or "selected" in card_class

    # Phone Methods
    def click_phone_field(self):
        self.driver.find_element(*self.PHONE_FIELD_BUTTON_LOCATOR).click()

    def enter_phone_number(self, phone):
        self.driver.find_element(*self.PHONE_INPUT_LOCATOR).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

    def enter_confirmation_code(self, code):
        self.driver.find_element(*self.CONFIRMATION_CODE_INPUT_LOCATOR).send_keys(code)

    def click_confirm_button(self):
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    def get_phone_number_text(self):
        return self.driver.find_element(*self.PHONE_NUMBER_LABEL_LOCATOR).text

    # Blanket & Handkerchiefs Methods
    def toggle_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_SLIDER_LOCATOR).click()

    def is_blanket_selected(self):
        checkbox = self.driver.find_element(*self.BLANKET_CHECKBOX_LOCATOR)
        return checkbox.get_property('checked')
