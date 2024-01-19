import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Specify the browser (chrome/firefox)",
    )


@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")
    if isinstance(browser, list):
        browser = browser[0]

    if browser == "chromium":
        chrome_driver_path = (
            r"C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
        )

        service = Service(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        print("Launching chrome browser.........")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        raise ValueError(f"Invalid browser: {browser}")
    yield driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption(
        "--custom-browser",
        action="store",
        default="chromium",
        choices=["chromium", "firefox", "webkit"],
        help="Specify the browser (chromium, firefox, or webkit) for testing",
    )


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# @pytest.fixture()
# def chrome_driver():
#     chrome = "C:\\Program Files (x86)\\chromedriver_win32\\chromedriver.exe"
#     service = Service(executable_path=chrome)
#     driver = webdriver.Chrome(service=service)
#     return driver


########### pytest HTML Report ################


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {
        "Tester": "Amar",
        "Project Name": "Hybrid Framework Practice",
    }
    # config.metadata["Project Name"] = "nop Commerce"
    # config.metadata["Module Name"] = "Customers"
    # config.metadata["Tester"] = "Kashif"


# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
