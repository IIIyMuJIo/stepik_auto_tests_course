from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    import math

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    number = browser.find_element(By.ID, "input_value")
    x = number.text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()