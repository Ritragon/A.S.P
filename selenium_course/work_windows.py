from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(3)
    nw = browser.window_handles[1]
    browser.switch_to.window(nw)
    x = calc(browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text)
    browser.find_element(By.CSS_SELECTOR, "input#answer.form-control").send_keys(x)
    browser.find_element(By.TAG_NAME, "button").click()
    print(browser.switch_to.alert.text)
    browser.switch_to.alert.accept()

finally:
    browser.quit()
