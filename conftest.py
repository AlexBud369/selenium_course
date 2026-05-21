import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language for browser: en, ru, es, fr, etc."
    )


@pytest.fixture(scope="function")
def browser(request):
    # Получаем язык из командной строки
    language = request.config.getoption("--language")

    # Настраиваем язык браузера через опции Chrome
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": language}
    )

    print(f"\nstart browser with language: {language}")
    driver = webdriver.Chrome(options=options)

    yield driver

    print("\nquit browser..")
    driver.quit()
