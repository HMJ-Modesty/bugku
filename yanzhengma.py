import ddddocr
import pytesseract
import requests
from PIL import Image
from collections import defaultdict
from urllib.request import urlretrieve
import urllib.request

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
}
url="https://ctf.bugku.com/captcha.html"


url1 = "https://ctf.bugku.com/login"

def ddddorc_deal(img):
    orc = ddddocr.DdddOcr()
    with open(img, 'rb+') as fp:
        img_bytes = fp.read()
    res = orc.classification(img_bytes)
    return res

def checkin(headers):
    a = requests.post("https://ctf.bugku.com/login",data = data, headers=headers, verify=False, timeout=40)
    info = requests.get("https://ctf.bugku.com/user/checkin", headers=headers, verify=False, timeout=40).text.split(
        '<h3 class="m-t-30">')[1].split('</')[0]
    print(info.strip())
user = "MODESTY"
password = "zxcasdqwe123ZXC"


headers1 = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
    "username": user,
    "password": password,
    "vcode": ddddorc_deal("img.png"),
    "autologin":"1",
   # "cookie": "Hm_lvt_97426e6b69219bfb34f8a3a1058dc596=1667379873,1667394440,1667396393,1667461689; think_lang=zh-cn; PHPSESSID=39e4833e15729ca3684ad8047478f1d5; autoLogin=k9kO6NcQ13o2hQQsxG98rnS9Z0dSe7yDRq2JSwqMjN4RCuAQkGMdGTGaWMD8%2B3gx5kq7vHH6Ov%2BSm5FeMLqI2bhsHlNJEnv%2BAAFPA68gkkgEZCJ8rNMb1BfiNg2WsgXqUgludbEVzG2n; X-CSRF-TOKEN=d86ce30dd470abf39d2f4e8e55933ae9; Hm_lpvt_97426e6b69219bfb34f8a3a1058dc596=1667461689"
}

# headers1={
#     Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
#     Accept-Encoding: gzip, deflate, br
#     Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
#     Connection: keep-alive
#     Cookie: think_lang=zh-cn; PHPSESSID=85a824e877863e2d51bf2bfd0c3ddbf2; X-CSRF-TOKEN=a14552af84128ff138e85e85665bfd4f; autoLogin=k9oJu9Ibi3s2hQQsxG98rnS9Z0dSe7yDR6WKRQeMjN4RCuAQkGMdGTGaWMD8%2B3gx7Ua%2FsHv9bKKUmZ5aOrzbjrtlSFQfSC2uB1ZLX61zkE8EZCJ8rNMb1BfiNg2WsgXqUgludbEVzG2n
#     Host: ctf.bugku.com
#     Referer: https://ctf.bugku.com/login.html
#     sec-ch-ua: "Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
#     sec-ch-ua-mobile: ?0
#     sec-ch-ua-platform: "Windows"
#     Sec-Fetch-Dest: document
#     Sec-Fetch-Mode: navigate
#     Sec-Fetch-Site: same-origin
#     Sec-Fetch-User: ?1
# }

data = {
    "username": user,
    "password": password,
    "vcode": ddddorc_deal("img.png"),
}
urlretrieve(url, "img.png")

checkin(headers1)



