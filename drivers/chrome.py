from selenium import webdriver
from selenium.webdriver.common.service import Service


class Chrome:
    @staticmethod
    def get_driver():
        chrome = "./drivers/chromedriver.exe"
        service = Service(executable_path=chrome)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
