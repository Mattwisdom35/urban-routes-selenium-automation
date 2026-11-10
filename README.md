# Urban Routes – UI Test Automation (Python + Selenium)

Automated end-to-end UI tests for **Urban Routes**, a taxi-ordering web application, built during the TripleTen Quality Assurance program.

The suite walks through the full ride-ordering flow — from entering a route to the "searching for a car" screen — and checks that each step behaves as expected.

## Tech stack

- Python 3
- Selenium WebDriver 4.25
- pytest 8.3
- Page Object Model (POM) design pattern
- Chrome DevTools performance logs (to read the SMS confirmation code)

## Project structure

| File | Purpose |
| --- | --- |
| `main.py` | Test class `TestUrbanRoutes` with the sample test cases |
| `pages.py` | `UrbanRoutesPage` page object: locators and page actions |
| `data.py` | Test data (URL, addresses, phone, card, driver message) |
| `helpers.py` | Utilities: server availability check and SMS code retrieval |
| `requirements.txt` | Python dependencies |

## Test cases

The full suite has 8 tests. This repository includes 4 of them as a sample.

| # | Test | What it verifies | In this repo |
| --- | --- | --- | --- |
| 1 | `test_set_route` | "From" and "To" addresses are entered and shown correctly | Yes |
| 2 | `test_select_supportive_plan` | The Supportive tariff can be selected | Yes |
| 3 | `test_fill_phone_number` | Phone number is added and confirmed with the SMS code | Yes |
| 4 | `test_add_credit_card` | A payment card can be linked | Private |
| 5 | `test_comment_for_driver` | A message for the driver is saved | Private |
| 6 | `test_order_blanket_and_handkerchiefs` | The "Blanket and handkerchiefs" option can be turned on | Yes |
| 7 | `test_order_two_ice_creams` | Two ice creams can be added to the order | Private |
| 8 | `test_car_search_modal_appears` | The car search window appears after ordering | Private |

> **Note:** Only part of the solution is published, so that the answer key of an active course project stays private. The full code is available on request.

## How to run

1. Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/Mattwisdom35/urban-routes-selenium-automation.git
   cd urban-routes-selenium-automation
   pip install -r requirements.txt
   ```
2. Start a fresh Urban Routes server and put its URL in `data.py` (`urban_routes_url`).
3. Run the tests:
   ```bash
   pytest main.py -v
   ```

> Note: The Urban Routes test server is provided by TripleTen and its URL changes for each session.

## Author

**Hikmet Osmancik** – Junior QA Engineer
[LinkedIn](https://www.linkedin.com/in/hikmet-osmancik-7938552865665658485/)
