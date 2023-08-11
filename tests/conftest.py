import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def setup_browser():

    browser.config.driver_name = 'firefox'
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 768
    browser.config.window_width = 1024
    browser.config.timeout = 2000.0

    yield

    browser.quit()