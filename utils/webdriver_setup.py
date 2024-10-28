import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

class Driver:
    @pytest.fixture(scope="function")
    def driver(self):
        """Set up Edge WebDriver with custom options."""
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=options)
        driver.maximize_window()
        yield driver
        driver.quit()