from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ваш код, который заполняет обязательные поля
    button = WebDriverWait(browser, 15).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()
    x_numb = calc(browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text)
    browser.find_element(By.CSS_SELECTOR, "input#answer.form-control").send_keys(x_numb)
    # Отправляем заполненную форму
    browser.find_element(By.ID, "solve").click()
    print(browser.switch_to.alert.text)
    browser.switch_to.alert.accept()



finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
