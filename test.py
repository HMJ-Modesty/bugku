import ddddocr
import pytesseract
import requests
from PIL import Image
from collections import defaultdict
from urllib.request import urlretrieve
import urllib.request

url="https://ctf.bugku.com/captcha.html"
url1 = "https://ctf.bugku.com/login/check.html"

def ddddorc_deal(img):
    orc = ddddocr.DdddOcr()
    with open(img, 'rb+') as fp:
        img_bytes = fp.read()
    res = orc.classification(img_bytes)
    return res

def checkin(headers):
    a = requests.post("https://ctf.bugku.com/login",payload, headers=headers, verify=False, timeout=40)
    info = requests.get("https://ctf.bugku.com/user/checkin", headers=headers, verify=False, timeout=40).text.split(
        '<h3 class="m-t-30">')[1].split('</')[0]
    print(info.strip())

user = "MODESTY"
password = "zxcasdqwe123ZXC"


headers1={
    "Cookie": "Hm_lvt_97426e6b69219bfb34f8a3a1058dc596=1667379873,1667394440,1667396393,1667461689; think_lang=zh-cn; PHPSESSID=39e4833e15729ca3684ad8047478f1d5; X-CSRF-TOKEN=93d7f17e249c6f9f302bb6c7ff738dab; Hm_lpvt_97426e6b69219bfb34f8a3a1058dc596=1667483754",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Csrf-Token": "a6f8349b888fdfd18a8513f5efbc3c2b",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "65",
    "Origin": "https://ctf.bugku.com",
    "Referer": "https://ctf.bugku.com/login",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "ors",
    "Sec-Fetch-Site": "same-origin",
    "Te": "trailers",
    "Connection": "close"
}

payload = {
    "username": user,
    "password": password,
    "vcode": ddddorc_deal("img.png"),
    "autologin":"1"
}

urlretrieve(url, "img.png")

# checkin(headers1)
bugkuSession = requests.session()
print(bugkuSession)

p = bugkuSession.post(url1, payload, headers1, timeout=40)
cookies = bugkuSession.get(url1).cookies.get_dict()

print(p.headers)
print(p.cookies)
print(bugkuSession)


