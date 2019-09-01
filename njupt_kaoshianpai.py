import requests
from bs4 import BeautifulSoup
import re
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr))

def send_email(sending_text):
    from_addr = '1017010333@njupt.edu.cn'
    password = 'asd_19941016'
    # 输入SMTP服务器地址:
    smtp_server = 'mail.njupt.edu.cn'
    # 输入收件人地址:
    to_addr = '1017010333@njupt.edu.cn'

    msg = MIMEText('The new url is: ' + sending_text, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'Tmy_Spider <%s>' % from_addr)
    msg['To'] = _format_addr(u'Tmy <%s>' % to_addr)
    msg['Subject'] = Header(u'The website is update.', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

try:
    with open('G:/tmp/z.txt') as Read:   # /home/wxm/zjc/z.txt      G:/tmp/z.txt
        count = int(Read.read())
except:
    count = -1
url = 'http://pg.njupt.edu.cn/2018/0508/c1049a126867/page.htm'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
r = requests.get(url, headers=headers)
r.encoding = 'utf-8'
# r.encoding = r.apparent_encoding
text = str(r.text)
print(text)
pattern = re.compile('月')
# pattern = re.compile('\d+</span><span style="font-family:宋体;font-size:16px;mso-bidi-font-family:宋体;mso-font-kerning:0px;">月<span lang="EN-US">\d+</span>日')
time_new = re.findall(pattern, text)
# print(time_new)
count_new = len(time_new)
print(count_new)
if count_new != count:
    # print('changed.')
    count_save = count_new
    with open('G:/tmp/z.txt', 'w') as Write:
        Write.write(str(count_save))
    # send_email(url)