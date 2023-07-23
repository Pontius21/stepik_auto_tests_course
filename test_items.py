from selenium.webdriver.common.by import By

def test_page_contains_add_button(browser):
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button.is_displayed()