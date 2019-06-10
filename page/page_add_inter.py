from time import sleep

import page
from base.base import Base


class PageAddInter(Base):

    # 点击右上角购物车
    def page_click_right_shopping_cart(self):
        self.base_click(page.loc_right_shopping_cart)

    # 点击扫把清空
    def page_click_clear(self):
        self.base_click(page.loc_clear)

    # 点击确定清扫
    def page_click_clear_ok(self):
        self.base_click(page.loc_clear_ok)

    # 点击固网商品
    def page_click_fixed_inter(self):
        self.base_click(page.loc_fixed_inter)

    # 点击专线商品
    def page_click_special_inter(self):
        self.base_click(page.loc_special_inter)

    # 点击互联网专线商品
    def page_click_inter_01(self):
        self.base_click(page.loc_inter_01)

    # 点击框内互联网专线商品
    def page_click_inter_02(self):
        self.base_click(page.loc_inter_02)

    # 选择点击端口带宽
    def page_click_port_width(self):
        self.base_click(page.loc_port_width)

    # 点击路由协议
    def page_click_routing_protocol(self):
        self.base_click(page.loc_routing_protocol)

    # 下滑页面
    def page_scroll01(self):
        js1 = "window.scrollTo(0,400)"
        self.driver.execute_script(js1)

    # 点击穿透模式
    def page_click_penetration_mode(self):
        self.base_click(page.loc_penetration_mode)

    # 点击接入层级
    def page_click_join_hierarchy(self):
        self.base_click(page.loc_join_hierarchy)

    # 点击业务等级
    def page_click_business_hierarchy(self):
        self.base_click(page.loc_business_hierarchy)

    # 点击加入购物车
    def page_click_join_shopping_cart(self):
        self.base_click(page.loc_join_shopping_cart)

    # 点击确定
    def page_click_join_ok(self):
        sleep(2)
        self.base_click(page.loc_join_ok)

    # 点击下一步信息录入
    def page_click_next_information(self):
        self.base_click(page.loc_next_information)

    # 封装整体选商品
    def page_add_inter(self):
        self.page_click_right_shopping_cart()
        self.page_click_clear()
        self.page_click_clear_ok()
        self.page_click_fixed_inter()
        self.page_click_special_inter()
        self.page_click_inter_01()
        self.page_click_inter_02()
        self.page_click_port_width()
        self.page_click_routing_protocol()
        self.page_scroll01()
        self.page_click_penetration_mode()
        self.page_click_join_hierarchy()
        self.page_click_business_hierarchy()
        self.page_click_join_shopping_cart()
        self.page_click_join_ok()
        self.page_click_next_information()
