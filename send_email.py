import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "wangyuan_dhtwo@163.com"  # 用户名
mail_pass = "wang31415926"  # 授权密码，非登录密码

sender = 'wangyuan_dhtwo@163.com'  # 发件人邮箱(最好写全, 不然会失败)
receivers = ['wangyuan_mail@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# content = '聪明的，你告诉我，我们的日子为什么一去不复返呢？'
# title = '匆匆'  # 邮件主题

def sendEmail(title,content):

    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
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

if __name__ == '__main__':
    message = '''在售的数量为:90
在售的平均价格(去掉一个最高价)为:5022
在售的最低价格为:3850.0
在售的最低价格的链接为:https://xy2.cbg.163.com/equip?s=331&eid=201909041100213-331-JNXZUH1F4D9J&o&view_loc=overall_search
傲雪凌霜在售的最低价格:4499.0
加上10%跨服费后: 4235.0
3850.0 3850.0 False'''
    sendEmail('test1',message)
        # receiver = '***'
        # send_email2(mail_host, mail_user, mail_pass, receiver, title, content)