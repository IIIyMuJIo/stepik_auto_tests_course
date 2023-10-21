import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    import math

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    button = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
finally:
    time.sleep(10)
    browser.quit()
