import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_can_add_book_to_basket(browser):
    browser.get(link)

    # time.sleep(30)  # раскомментируйте для визуальной проверки языка кнопки

    # Ожидаем появления кнопки "Добавить в корзину"
    add_to_basket_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.btn-add-to-basket")
        )
    )

    assert add_to_basket_btn.is_displayed(), \
        "Кнопка добавления в корзину не найдена на странице товара"
