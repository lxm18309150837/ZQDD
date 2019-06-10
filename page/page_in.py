"""
1.需要管理几个页面对象,就创建几个获取页面对象的方法
"""
from base.get_driver import get_driver
from page.page_add_inter import PageAddInter
from page.page_city_inter_information import PageCityInterInformation
from page.page_local_inter_information import PageLocalInterInformation
from page.page_login import PageLogin
from page.page_order_ok import PageOrderOk
from page.page_search_client import PageSearchClient

# 定义driver


driver = get_driver()


# 建类
class PageIn():
    # 创建获取PageLogin-登录对象方法
    def page_get_pagelogin(self):
        return PageLogin(driver)

    # 创建获取PageSearchClient-(选择客户)对象方法
    def page_get_pagesearchclient(self):
        return PageSearchClient(driver)

    # 创建获取PageAddLocalInter-(选择互联网)对象方法
    def page_get_pageaddinter(self):
        return PageAddInter(driver)

    # 创建获取PageInformation-(本地互联网信息录入)对象方法
    def page_get_pagelocalinterinformation(self):
        return PageLocalInterInformation(driver)

    #创建获取PageInformation-(跨域互联网信息录入)对象方法
    def page_get_pagecityinterinformation(self):
        return PageCityInterInformation(driver)

    # 创建获取PageOrderOk-(确认订单)对象方法
    def page_get_pageorderok(self):
        return PageOrderOk(driver)
