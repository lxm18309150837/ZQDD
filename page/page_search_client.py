from time import sleep

import page
from base.base import Base


class PageSearchClient(Base):
    # 点击订单受理
    def page_click_order(self):
        sleep(5)
        self.base_click(page.loc_click_order)

    # 点击业务受理
    def page_click_business(self):
        self.base_click(page.loc_business_btn)

    # 切换frame到选择客户页
    def page_frame(self):
        self.base_frame()

    # 输入客户编号
    def page_input_client_code(self, code):
        self.base_input(page.loc_client_code, code)

    # 点击查询按钮
    def page_click_search_btn(self):
        self.base_click(page.loc_search_btn)

    # 点击选择客户
    def page_click_client(self):
        self.base_click(page.loc_client)

    # 点击下一步选择商品
    def page_click_next_btn(self):
        self.base_click(page.loc_next)

    #封装整体选择客户方法
    def page_search_client(self,code):
        self.page_click_order()
        self.page_click_business()
        self.page_frame()
        self.page_input_client_code(code)
        self.page_click_search_btn()
        self.page_click_client()
        self.page_click_next_btn()
