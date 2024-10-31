import time
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    # Navigate to the login page
    def go_to_login(self, email, password):
        """Natvigate to the login page."""
        self.driver.get("http://localhost/opencart/")
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[2]/a").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button").click()
        time.sleep(5)
    # click on logout
    def logout(self):
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[5]/a").click()
        time.sleep(5)

    # get error message
    def get_error_message(self):
        return self.driver.find_element(By.XPATH, "/html/body/div").text