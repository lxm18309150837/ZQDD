"""
    新建公共方法
    1.找元素
    2.输入方法
    3.点击元素
"""
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


# 新建类
class Base():
    def __init__(self, driver):
        self.driver = driver

    # 封装查找元素方法
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 封装输入方法
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 封装点击方法
    def base_click(self, loc):
        sleep(2)
        self.base_find_element(loc).click()

    # frame
    def base_frame(self):
        sleep(2)
        iframe = self.driver.find_elements_by_tag_name("iframe")[0]
        self.driver.switch_to_frame(iframe)

    # 下拉框选择
    def base_select(self, loc, sel):
        select_ele = self.base_find_element(loc)
        select = Select(select_ele)
        select.select_by_visible_text(sel)
