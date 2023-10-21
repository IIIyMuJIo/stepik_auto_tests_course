from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary").click()
    wind_two = browser.window_handles[1]
    browser.switch_to.window(wind_two)
    import math

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    element_x = browser.find_element(By.ID, "input_value")
    x = element_x.text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()

    #just for test