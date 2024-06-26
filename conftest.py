import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ru or eng or other")


@pytest.fixture(scope="function")
def driver(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = Options()
        options.set_preference("intl.accept_languages", language)
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print(f"\nquit {browser_name} browser..")
    driver.quit()


@pytest.fixture(scope="session")
def load_config():
    with open('../config.json', 'r') as conf:
        config = json.load(conf)
        yield config
