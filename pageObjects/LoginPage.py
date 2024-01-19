from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    logout_text = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setemail(self, username):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(username)

    def setpassword(self, Password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(Password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
