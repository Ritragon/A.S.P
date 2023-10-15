from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import math

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Alex")
    browser.find_element(By.NAME, "lastname").send_keys("Serious")
    browser.find_element(By.NAME, "email").send_keys("des@git.com")
    file_path = os.path.join(os.path.abspath(os.path.dirname('__file__')), "magnet_tor.txt")
    browser.find_element(By.NAME, 'file').send_keys(file_path)
    button = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]")

    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла