from time import sleep

import page
from base.base import Base


class PageCityInterInformation(Base):
    # 输入全程要求完成时间
    def page_input_finish_time(self, time):
        self.base_input(page.loc_finfish_time01, time)

    # 点击全程要求完成时间
    def page_click_finish_time(self):
        self.base_click(page.loc_finfish_time02)

    # 点击编辑
    def page_click_edit_btn(self):
        self.base_click(page.loc_edit_btn)

    # 滚动条向下滑
    def page_scroll02(self):
        js2 = "window.scrollTo(0,600)"
        self.driver.execute_script(js2)

    # 选择跨域地址
    def page_click_other_address(self):
        self.base_click(page.loc_address02)
        self.base_click(page.loc_province)
        self.base_click(page.loc_city)
        self.base_click(page.loc_area)

    # 输入装机地址
    def page_input_address01(self, local_address):
        self.base_input(page.loc_address01, local_address)

    # 点击选择ip协议版本
    def page_select01(self, sel):
        self.base_select(page.loc_select01, sel)

    # 输入ipv4地址数量
    def page_input_address_count(self, count):
        self.base_input(page.loc_address_count, count)

    # 输入AS号
    def page_input_as(self, value):
        self.base_input(page.loc_as, value)

    def page_scroll03(self):
        js3 = "window.scrollTo(0,500)"
        self.driver.execute_script(js3)

    # 点击保存
    def page_click_save_btn(self):
        self.base_click(page.loc_save_btn)

    # 点击确认保存
    def page_click_save_ok(self):
        self.base_click(page.loc_save_ok)

    # 再次下滑
    def page_scroll04(self):
        js4 = "window.scrollTo(0,700)"
        self.driver.execute_script(js4)

    # 点击发展人渠道
    def page_click_people01(self):
        self.base_click(page.loc_people01)

    # 点击渠道分类
    def page_click_people02(self):
        sleep(3)
        self.base_click(page.loc_people02)

    # 点击选择渠道
    def page_click_people03(self):
        sleep(3)
        self.base_click(page.loc_people03)

    # 点击选择发展人
    def page_click_people04(self):
        sleep(5)
        self.base_click(page.loc_people04)

    # 点击联系人信息
    def page_click_people_information(self):
        self.base_click(page.loc_people_information)

    # 输入姓名
    def page_input_name(self, name):
        self.base_input(page.loc_name, name)

    # 输入电话
    def page_input_phone(self, phone):
        self.base_input(page.loc_phone, phone)

    # 点击下一步提交
    def page_click_next(self):
        self.base_click(page.loc_next01)

    # 封装整体跨域互联网信息录入
    def page_city_inter_information(self, time, local_address, sel, count, value, name, phone):
        self.page_input_finish_time(time)
        self.page_click_finish_time()
        self.page_click_edit_btn()
        self.page_scroll02()
        self.page_click_other_address()
        self.page_input_address01(local_address)
        self.page_select01(sel)
        self.page_input_address_count(count)
        self.page_input_as(value)
        self.page_scroll03()
        self.page_click_save_btn()
        self.page_click_save_ok()
        self.page_scroll04()
        self.page_click_people01()
        self.page_click_people02()
        self.page_click_people03()
        self.page_click_people04()
        self.page_click_people_information()
        self.page_input_name(name)
        self.page_input_phone(phone)
        self.page_click_next()
