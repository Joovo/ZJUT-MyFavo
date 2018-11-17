#!usr/bin/python3

import requests
import random

url_login1 = "http://tp.zjutjh.com/zjut/firstVote/index.jsp"
url_login2="http://tp.zjutjh.com/zjut/login"
url_select="http://tp.zjutjh.com/zjut/firstVote"

def login(session, no, pwd):
    response = session.get(url_login1, allow_redirects=False)
    cookies = tuple(response.cookies.get_dict().values())[0]
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
    form_data = {
        'no': no,
        'password': pwd
    }
    r = session.post(url=url_login2, data=form_data, headers=headers)
    return session,cookies

jisuanji_teacher_no = [
    '2Xsr6kz5AC'  # XiaMing'
    , '5W9gtHj91E'  # LuJiaWei'
    , '9enDQSYl09'  # 'Caobin'
    , 'LhddiJLUWv'  # 'ChengZhenBo'
    , 'nZ8JIwMVVN'  # 'LongShengChun'
    , 'nZ8JIwMVVN'  # 'GaoFei'
]

tijunbu_teacher_no = 'B5AezwOihC'  # CaoZhuPing


def vote1(session,no,cookie):
    form_data = {
        'no': no,
        'college': '计算机科学与技术学院、软件学院'
    }
    headers = {
        'Accept': "*/*",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.89",
        'Connection': "keep-alive",
        'Content-Length': "157",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Cookie': "JSESSIONID="+str(cookie),
        'Host': "tp.zjutjh.com",
        'Origin': "http://tp.zjutjh.com",
        'Referer': "http://tp.zjutjh.com/zjut/firstVote/firstVote.jsp",
        'User-Agent': "User-Agent: Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'X-Requested-With': "XMLHttpRequest",
    }
    r = session.post(url=url_select, data=form_data, headers=headers)

def vote2(session,no,cookie):
    form_data = {
        'no':no,
        'college': '体育军训部'
    }
    headers = {
        'Accept': "*/*",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.89",
        'Connection': "keep-alive",
        'Content-Length': "157",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Cookie': "JSESSIONID="+str(cookie),
        'Host': "tp.zjutjh.com",
        'Origin': "http://tp.zjutjh.com",
        'Referer': "http://tp.zjutjh.com/zjut/firstVote/firstVote.jsp",
        'User-Agent': "User-Agent: Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        'X-Requested-With': "XMLHttpRequest",
    }
    r = session.post(url=url_select, data=form_data, headers=headers)

if __name__ == '__main__':
    for no in range(201626810101,201626811630):
        try:
            no = '201626810411'
            pwd = no[-6:]
            session=requests.session()
            session,cookies=login(session,no,pwd)
            no = jisuanji_teacher_no[random.randint(0,len(jisuanji_teacher_no)-1)]
            vote1(session,no,cookies)
            vote2(session,tijunbu_teacher_no,cookies)
        except:
            pass
