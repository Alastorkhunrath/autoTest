import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from loguru import logger



@pytest.fixture(scope="session")
def browser():
    option = Options()
    option.add_argument("--start-maximized")
    service = Service()
    driver = webdriver.Edge(service=service, options=option)
    logger.info("Browser opened")
    yield driver
    logger.info("Browser closing")
    driver.quit()