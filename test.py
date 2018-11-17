import requests
import random

no = '201626810405'
pwd = '810405'

url_login = "http://tp.zjutjh.com/zjut/firstVote/index.jsp"
url_select="http://tp.zjutjh.com/zjut/login"

session = requests.session()
response=session.get(url_login,allow_redirects=False)
cookies=tuple(response.cookies.get_dict().values())[0]

print(cookies)
form_data = {
    'no': no,
    'password': pwd
}
#cookies='JSESSIONID=113DEAB06F1018BBD59D5C52E71302CF'
headers = {
    'Cookie':'JSESSIONID='+str(cookies),
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
    'Cache-Control': "max-age=0",
    'Connection': "keep-alive",
    'Content-Length': "31",
    'Content-Type': "application/x-www-form-urlencoded",
    'Host': "tp.zjutjh.com",
    'Origin': "http://tp.zjutjh.com",
    'Referer': "http://tp.zjutjh.com/zjut/firstVote/index.jsp",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
}
r = session.post(url=url_select, data=form_data, headers=headers)
print(r.text)
