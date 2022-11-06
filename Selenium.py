from selenium import webdriver
import ddddocr
import time
import re

from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

edge_options = EdgeOptions()
edge_options.use_chromium = True
# 设置无界面模式，也可以添加其它设置
edge_options.add_argument('headless')
# 规避被检测到的风险
edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])


driver = Edge(options=edge_options)


# driver = webdriver.Edge()


def ddddorc_deal(img):
    orc = ddddocr.DdddOcr()
    with open(img, 'rb+') as fp:
        img_bytes = fp.read()
    res = orc.classification(img_bytes)
    return res


def log_in(username, password):
    print("登录账户:{}".format(username))
    url = "https://ctf.bugku.com/login.html"
    driver.get(url)
    driver.find_element_by_id('vcode').screenshot("code.png")
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('vcode').send_keys(ddddorc_deal("code.png"))
    driver.find_element_by_id('login').click()
    time.sleep(10)
    driver.get("https://ctf.bugku.com/user/checkin")
    text = driver.page_source.split('<h3 class="m-t-30">')[1].split('</')[0]
    print(text)
    result = re.findall("请登录", text)
    if result == ['请登录']:
        print("登录失败！！！正在重新登录！！！")
        log_in(username, password)
    time.sleep(10)
    driver.get("https://ctf.bugku.com/logout.html")
    time.sleep(3)
    print("退出登录")


if __name__ == "__main__":
    log_in("账号", "密码")
    driver.quit()


