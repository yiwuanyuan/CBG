#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : main.py
# Author: Wangyuan
# Date  : 2019/3/13

import requests
import urllib.request
import json
import random
import pandas
import time, datetime
from urllib import parse
import os
from twilio.rest import Client

url = "https://xy2.cbg.163.com/cgi-bin/show_login.py?act=show_login&server_id=72&server_name=%E5%89%91%E8%83%86%E7%90%B4%E5%BF%83&area_name=%E4%BA%BA%E7%95%8C%20&area_id=4"
# 4仙忽视混
ipList = ['118.24.61.22:3128',
          '39.137.69.10:80',
          '39.137.69.10:8080',
          '82.194.235.142:8080',
          '39.137.69.8:8080',
          '39.137.69.8:80',
          '39.137.69.7:80',
          '39.137.69.7:8080',
          '39.137.107.98:80',
          '39.137.107.98:8080',
          '111.26.9.26:80',
          '101.4.136.34:80',
          '101.4.136.34:81',
          '101.4.136.34:8080',
          '39.137.77.67:8080', ''
                               '39.137.77.66:80',
          '39.137.77.67:80',
          '39.137.77.66:8080',
          '120.198.230.15:8080',
          '193.112.113.26:1080',
          '159.138.20.247:80',
          '119.28.203.242:8000',
          '138.117.4.45:80',
          '45.113.69.177:1080',
          '49.51.193.134:1080',
          '49.51.195.24:1080',
          '49.51.70.42:1080',
          '49.51.68.122:1080',
          '49.51.193.128:1080',
          '14.142.122.134:8080',
          '159.138.22.112:80',
          '171.255.192.118:808',
          '223.96.95.229:3128',
          '119.28.87.177:808',
          '159.138.21.170:80',
          '93.190.139.155:8080',
          '134.119.205.246:808',
          '134.119.205.253:808',
          '39.137.69.6:8080']
user_agent_list = [
    "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
    "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "wangyuan_dhtwo@163.com"  # 用户名
mail_pass = "wang31415926"  # 授权密码，非登录密码

sender = 'wangyuan_dhtwo@163.com'  # 发件人邮箱(最好写全, 不然会失败)
receivers = ['wangyuan_mail@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


def sendEmail(title, content):
    mail_content = str(content)
    message = MIMEText(mail_content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()


def url_timestamp():
    int2week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    int2month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    now = datetime.datetime.now()
    otherTime = now.strftime("%H:%M:%S")
    month = int(now.strftime("%m")) - 1
    week = int(now.weekday())
    day = now.strftime("%d")
    year = now.strftime("%Y")
    timestamp = int2week[week] + ' ' + int2month[month] + ' ' + day + ' ' + year + ' ' + otherTime

    url_timestamp = parse.quote(timestamp) + '%20GMT%2B0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)'
    return url_timestamp


def send_SMS(msg):
    account_sid = 'ACa4c01dddc037244a6bbdc4c629a2923d'
    auth_token = 'b44fff6661d2e633ae536d4f60e17b55'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=str(msg),
        from_='+13343452980',
        to='+8613145155669'
    )
    print('成功发送短信')


class getContent:
    def __init__(self, url):
        self.url = url

    # 使用requests.get获取知乎首页的内容
    def content(self):
        User_Agent = random.choice(user_agent_list)
        Random_proxy = random.choice(ipList)
        url = self.url
        headers = {
            'User-Agent': User_Agent
        }
        request = urllib.request.Request(url=url, headers=headers)
        proxy = {
            'http': Random_proxy
        }
        # 创建代理Handler对象
        proxy_handler = urllib.request.ProxyHandler(proxy)
        # 以Handler对象为参数创建Opener对象
        opener = urllib.request.build_opener(proxy_handler)
        # 将Opener安装为全局
        urllib.request.install_opener(opener)
        response = urllib.request.urlopen(request)
        # page_source = response.read()
        page_source = response.read().decode('utf-8')
        params = json.loads(page_source)
        return params


def get_more_info():
    random_num = url_timestamp()
    res = getContent(
        'https://xy2.cbg.163.com/cgi-bin/search.py?act=overall_search_xianqi&page=1&server_type=3&equip_level=4&price_min=10000&price_max=100000000&basic_attr=%7B%22jiaqiangpilixiaoguo%22%3A22%7D&special_skill_logic=and&random=' + random_num)
    # res = getContent(
    #     'https://xy2.cbg.163.com/cgi-bin/search.py?act=overall_search_xianqi&page=1&server_type=3&equip_level=4&price_min=10000&price_max=100000000&special_skill_logic=and&random=' + random_num)
    content = res.content()
    total_page = content['paging']['total_pages']
    total_msg = []
    for i in range(1, total_page + 1):
        every_page_info = getContent(
            'https://xy2.cbg.163.com/cgi-bin/search.py?act=overall_search_xianqi&page=' + str(
                i) + '&server_type=3&equip_level=4&price_min=10000&price_max=100000000&basic_attr=%7B%22jiaqiangpilixiaoguo%22%3A22%7D&special_skill_logic=and&random=' + random_num).content()

        if type(every_page_info) == dict:
            if 'msg' in every_page_info:
                total_msg = every_page_info['msg'] + total_msg

    sale_num = len(total_msg)
    total_price = 0
    price_arr = []

    for i in total_msg:
        price_arr.append(i['price'] / 100)
        total_price = total_price + i['price'] / 100
    average_price = (total_price - max(price_arr)) / (sale_num - 1)
    df = pandas.DataFrame(total_msg)

    low_price_eid = str(df[df['price'] == df['price'].min()]['eid']).split()[1]
    low_price_sid = str(df[df['price'] == df['price'].min()]['serverid']).split()[1]

    if not len(df[df['server_name'] == '傲雪凌霜']['price']) == 0:
        #
        server_price = df[df['server_name'] == '傲雪凌霜']['price']
        server_price_min = df[df['server_name'] == '傲雪凌霜']['price'].min()
        # 选定服务器最低价
        selected_server_min = int(server_price_min) / 100

    low_price_url = 'https://xy2.cbg.163.com/equip?s=' + low_price_sid + '&eid=' + low_price_eid + '&o&view_loc=overall_search'

    print('在售的数量为:' + str(sale_num))
    print('在售的平均价格(去掉一个最高价)为:' + str(int(average_price)))
    print('在售的最低价格为:' + str(min(price_arr)))
    print('在售的最低价格的链接为:' + low_price_url)
    print('傲雪凌霜在售的最低价格:' + str(selected_server_min))
    if not low_price_url == str(selected_server_min):
        print('加上10%跨服费后:', float(min(price_arr) * 1.1))

    now = datetime.datetime.now()
    otherStyleTime = now.strftime("%Y_%m_%d_%H_%M")
    excel_Time = now.strftime("%H:%M:%S")
    excel_Date = now.strftime("%Y/%m/%d")

    return_info = [{
        'sale_num': sale_num,
        'average_price': average_price,
        'min_prince': min(price_arr),
        'Date': excel_Date,
        'time': excel_Time,
        'eid': low_price_eid,
        'url': low_price_url

    }, df]

    return return_info


def always_search():
    info_gather = []
    min_prince = 0
    list_num = 0
    average_price = 0

    while True:
        info = get_more_info()
        every_info = info[0]
        if min_prince == 0:
            min_prince = every_info['min_prince']
        else:
            # print(every_info['min_prince'], min_prince, every_info['min_prince'] < min_prince)
            if every_info['min_prince'] < min_prince:
                min_prince = every_info['min_prince']
                now_send = datetime.datetime.now()
                Mail_title = '新的低价' + now_send.strftime("%Y_%m_%d_%H_%M")
                sendEmail(Mail_title, '有新的低价' + str(every_info['min_prince']) + '\n' +str(every_info['url']))

        df = pandas.DataFrame(every_info, index=[0])
        if os.path.isfile('大力仙器龙族仙器走势图.xlsx'):
            df1 = pandas.read_excel('大力仙器龙族仙器走势图.xlsx')
            res = df1.append(df)
        else:
            res = df

        if list_num == 0 or not list_num == info[0]['sale_num'] or not average_price == info[0][
            'average_price']:
            result_df = info[1]
            result_df.pop('other_info')
            result_df.pop('areaid')
            result_df.pop('can_cross_buy')
            result_df.pop('equip_type_desc')
            result_df.pop('min_buy_level')
            result_df.pop('min_buyer_level')
            result_df.pop('serverid')
            result_df.pop('zhui_jia_attr')
            result_df.pop('equip_type')
            result_df.pop('equip_level')
            result_df.pop('game_ordersn')
            result_df.pop('kindid')
            result_df.pop('lianhua_attr')
            result_df.pop('suit_require')
            result_df.pop('equip_face_img')

            now = datetime.datetime.now()
            otherStyleTime = now.strftime("%Y_%m_%d_%H_%M")

            result_df.to_excel('大力仙器' + otherStyleTime + '.xlsx')
            average_price = info[0]['average_price']
            list_num = info[0]['sale_num']
            res.to_excel('大力仙器龙族仙器走势图.xlsx')

        time.sleep(60)


if __name__ == '__main__':
    always_search()
