from selenium.webdriver.common.by import By

first_name_loc = (By.CSS_SELECTOR, "#firstname")
last_name_loc = (By.CSS_SELECTOR, "#lastname")
email_field_loc = (By.CSS_SELECTOR, '#email_address')
password_field_loc = (By.ID, 'password')
password_confirm_loc = (By.CSS_SELECTOR, "#password-confirmation")
button_create_an_account_loc = (By.CSS_SELECTOR, '.primary')
error_locator_loc = (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')

