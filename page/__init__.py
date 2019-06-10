from selenium.webdriver.common.by import By

"""以下为"""
loc_usr_btn = By.XPATH, "//*[text()='用户名登录']"
loc_username = By.ID, "userCode"
loc_password = By.ID, "password"
loc_code = By.XPATH, "//div[@class='ant-col-18']/input"
loc_btn = By.XPATH, "//div[@class='ant-tabs-content ant-tabs-content-animated ant-tabs-top-content']/div[2]/form/div[4]/button"
loc_click_order = By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div/div/div[2]/ul/li[2]/div/div"
loc_business_btn = By.XPATH, "//*[@id='DD0002$Menu']/li[1]/a"
loc_client_code = By.XPATH, "//*[@name='groupId']"
loc_search_btn = By.XPATH, "//form[@id='customerCondition']/../div/button[1]"
loc_client = By.XPATH, "//*[@title='5151051200403300377']/../td[1]/input"
loc_next = By.XPATH, "//button[text()='下一步：选择商品']"
loc_right_shopping_cart = By.XPATH, "//div[@class='cartBtn']"
loc_clear = By.XPATH, "//i[@class='iconfont icon-saoba']"
loc_clear_ok = By.XPATH, "//*[@class='modal-body isShowAlertModalBody']/../div[3]/button[1]"
loc_fixed_inter = By.XPATH, "//span[text()='固网商品']"
loc_special_inter = By.XPATH, "//span[text()='专线商品']"
loc_inter_01 = By.XPATH, "//span[text()='互联网专线商品']"
loc_inter_02 = By.XPATH, "//span[@title='互联网专线商品']/../../div[@class='goods-list']"
loc_port_width = By.XPATH, "//li[@title='8MBPS     ']"
loc_routing_protocol = By.XPATH, "//li[@title='BGP    ']"
loc_penetration_mode = By.XPATH, "//li[@title='国内穿透']"
loc_join_hierarchy = By.XPATH, "//li[@title='城域网接入层']"
loc_business_hierarchy = By.XPATH, "//li[@title='金牌']"
loc_join_shopping_cart = By.XPATH, "//*[contains(text(),'加入购物车')]"
loc_join_ok = By.XPATH, "//button[@class='btn btn-warning' and @style='display:inline-blcok' and text()='确定']"
loc_next_information = By.XPATH, "//button[text()='下一步：信息录入']"
loc_finfish_time01 = By.XPATH, "//input[@name='0-rg_00000004-ORD10012']"
loc_finfish_time02 = By.XPATH, "//*[text()='全程要求完成时间:']"
loc_edit_btn = By.XPATH, "//*[text()='编辑']"
loc_address02 = By.XPATH, "//*[@class='cityInputBg']"
loc_province = By.XPATH, "//*[@id='goodsListForm-0']/div[2]/div[2]/div/div[8]/div/div[2]/div[2]/ul/li[4]"
loc_city = By.XPATH, "//*[@id='goodsListForm-0']/div[2]/div[2]/div/div[8]/div/div[2]/div[2]/ul/li[8]"
loc_area = By.XPATH, "//*[@id='goodsListForm-0']/div[2]/div[2]/div/div[8]/div/div[2]/div[2]/ul/li[3]"
loc_address01 = By.XPATH, "//input[@name='0-rg_00000030-2_0000211']"
loc_select01 = By.XPATH, "//select[@name='0-rg_00000030-2_0000047']"
loc_address_count = By.XPATH, "//input[@name='0-rg_00000030-2_0000193']"
loc_as = By.XPATH, "//input[@name='0-rg_00000030-2_0000157']"
loc_save_btn = By.XPATH, "//button[@class='btn btn-primary'and text()='保存']"
loc_save_ok = By.XPATH, "//button[@class='btn btn-warning'and text()='确定']"
loc_people01 = By.XPATH, "//*[@id='otherMessage']/div[2]/div[2]/div[2]/div[1]/div[1]/div/div/div/div/div"
loc_people02 = By.XPATH, "//a[text()='公众直销渠道']/../.."
loc_people03 = By.XPATH, "//span[text()='广州市鸟巢电子科技有限公司'and @code_value='51b0n74']"
loc_people04 = By.XPATH, "//span[text()='广州市鸟巢电子科技有限公司'and @code_value='5102279443']"
loc_people_information = By.XPATH, "//*[@id='otherMessage']/div[2]/div[2]/div[1]/ul/li[2]"
loc_name =By.XPATH, "//input[@name='1-rg_00000019-CONTACT']"
loc_phone = By.XPATH, "//input[@name='1-rg_00000019-CONTACT_PHONE']"
loc_next01 = By.XPATH, "//button[text()='下一步：订单提交']"
loc_order_ok = By.XPATH, "//button[@class='btn btn-warning'and text()='确定']"
loc_text = By.XPATH, "//div[@class = 'proBuyOrder']"
loc_ok1 = By.XPATH, "//button[@class='btn btn-warning inforationOkBtn'and text()='确定']"