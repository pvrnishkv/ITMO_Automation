from selenium import webdriver
from selenium.webdriver.common.by import By

def search():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.CSS_SELECTOR, '#user-name')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    submit = driver.find_element(By.CSS_SELECTOR, '#login-button')

    if username is None or password is None or submit is None:
        print('Элементы не найдены')
    else:
        print('Элементы найдены')

