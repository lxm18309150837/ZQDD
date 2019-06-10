"""
    每一步操作为单独的方法
"""
import page
from base.base import Base


# 创建类名
class PageLogin(Base):
    # 点击用户名登录
    def page_click_usr_login(self):
        self.base_click(page.loc_usr_btn)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.loc_username, username)

    # 输入密码
    def page_input_password(self, password):
        self.base_input(page.loc_password, password)

    # 输入验证码
    def page_input_code(self, code):
        self.base_input(page.loc_code, code)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.loc_btn)

    # 封装整体登录
    def page_login(self, username, password, code):
        self.page_click_usr_login()
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_input_code(code)
        self.page_click_login_btn()
