from selenium import webdriver


def get_driver():
    driver = webdriver.Chrome()
    driver.get("http://10.124.195.138")
    driver.maximize_window()
    return driver





