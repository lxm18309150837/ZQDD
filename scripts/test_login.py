"""
    setup_class  teardown_class test_login
    #allure generate report/ -o report/html --clean
#将xml文件转换为html

#在线生成 -- allure serve report
"""
import sys
import os

sys.path.append(os.getcwd())
import allure
import pytest

from page.page_in import PageIn


# 建类名

class TestLogin():
    # setup_class
    def setup_class(self):
        self.login = PageIn().page_get_pagelogin()
        self.client = PageIn().page_get_pagesearchclient()
        self.inter = PageIn().page_get_pageaddinter()
        self.local_information = PageIn().page_get_pagelocalinterinformation()
        self.city_information = PageIn().page_get_pagecityinterinformation()
        self.order = PageIn().page_get_pageorderok()

    # teardown_class
    def teardown_class(self):
        self.login.driver.quit()

    @allure.step("登录-方法操作")
    @pytest.mark.parametrize("username,password,code", [("panyalin", "Xh75oN", "38282778")])
    def test_login(self, username, password, code):
        # 调用整体封装方法
        self.login.page_login(username, password, code)

    #@allure.step("选客户-方法操作")
    #@pytest.mark.parametrize("code", [("5151051200403300377")])
    #def test_search_client(self, code):
        # 调用整体选择客户方法
        #self.client.page_search_client(code)

    #@allure.step("选商品-方法操作")
    #def test_add_inter(self):
        # 调用整体选商品方法
        #self.inter.page_add_inter()

    #@allure.step("本地互联网信息录入-方法操作")
    #@pytest.mark.parametrize("time,local_address, sel, count, value, name, phone",[("2019-6-6", "装机地址", "IPv4", "22", "22", "222", "2222")])
    #def test_local_inter_information(self, time, local_address, sel, count, value, name, phone):
        #self.local_information.page_local_inter_information(time, local_address, sel, count, value, name, phone)

    #@allure.step("跨域互联网信息录入-方法操作")
    #@pytest.mark.parametrize("time, local_address, sel, count, value, name, phone", [("2019-6-6", "装机地址", "IPv4", "22", "22", "222", "2222")])
    #def test_city_inter_information(self, time, local_address, sel, count, value, name, phone):
        #self.city_information.page_city_inter_information(time, local_address, sel, count, value, name, phone)

    #@allure.step("信息预览页-方法操作")
    #def test_order_ok(self):
        #self.order.page_order_ok()

