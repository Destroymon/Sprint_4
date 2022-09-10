import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox()  # Задаем браузер
    driver.maximize_window()  # Делаем полный экран
    yield driver  # Возвращаем генератор
    driver.quit()  # Выходим с браузера :)