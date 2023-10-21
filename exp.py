import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 14).until(EC.text_to_be_present_in_element((By.ID, "price"), text_="$100"))
    browser.find_element(By.ID, "book").click()
    import math

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    number = browser.find_element(By.ID, "input_value")
    x = number.text
    y = calc(x)
    button = browser.find_element(By.ID, "answer")
    button.send_keys(y)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(5)
    browser.quit()
