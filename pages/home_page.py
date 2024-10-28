import time
from selenium.webdriver.common.by import By
from utils.webdriver_setup import Driver


class NavigationPage(Driver):
    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get("http://localhost/opencart/")
        time.sleep(3)

    def go_to_all_desktops(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/a").click()
        time.sleep(3)

    def go_to_all_laptops(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[2]/div/a").click()
        time.sleep(3)

    def go_to_all_components(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/a").click()
        time.sleep(3)

    def go_to_tablet(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[4]/a").click()
        time.sleep(3)

    def go_to_software(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[5]/a").click()
        time.sleep(3)

    def go_to_phones(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[6]/a").click()
        time.sleep(3)

    def go_to_cameras(self, driver):
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[7]/a").click()
        time.sleep(3)