from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # Нажать на кнопку
    browser.find_element(By.TAG_NAME, "button").click()

    # Принять confirm
    alert = browser.switch_to.alert
    alert.accept()

    # Считать x и посчитать ответ
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # Ввести ответ и отправить форму
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.TAG_NAME, "button").click()

    # Получить число из alert
    result = browser.switch_to.alert.text
    print(result)
    print(result.split(": ")[-1])  # только число для Stepik

finally:
    browser.quit()
