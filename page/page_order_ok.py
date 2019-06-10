import page
from base.base import Base


class PageOrderOk(Base):
    # 下滑到底部
    def page_scroll05(self):
        js5 = "window.scrollTo(0,1000)"
        self.driver.execute_script(js5)

    # 点击确定
    def page_click_order_ok(self):
        self.base_click(page.loc_order_ok)

    def get_text(self):
        ele = self.base_find_element(page.loc_text).text
        context = ele.split(":")[1]
        print(context)

    def page_click_ok1(self):
        self.base_click(page.loc_ok1)

    # 封装总体
    def page_order_ok(self):
        self.page_scroll05()
        self.page_click_order_ok()
        self.get_text()
        self.page_click_ok1()
