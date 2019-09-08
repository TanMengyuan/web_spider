"""
@version: python3.7
@author: ‘mengyuantan‘
@contact: tanmy1016@126.com
@time: 2019/9/8 11:50
"""

import requests
from bs4 import BeautifulSoup

prefix = "http://njupt.91job.org.cn"
major_url = "http://njupt.91job.org.cn/campus/index?city=&page="  # + page number
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "PHPSESSID2=qrr03rf5a25o40a529voft7hr4; __jsluid_h=9a16310c6f2a327e660971cbbfb2100e; "
              "UM_distinctid=16d0456ff534ff-0f8021f99cea6c-38607701-1fa400-16d0456ff54df7; "
              "CNZZDATA1254751961=98819749-1567733000-http%253A%252F%252Fnjupt.91job.gov.cn%252F%7C1567912547",
    "DNT": "1",
    "Host": "njupt.91job.org.cn",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/76.0.3809.100 Safari/537.36 "
}


def run():
    page_num = 12
    for page in range(1, page_num + 1):
        response = requests.get(url=major_url + str(page), headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')
        for each in soup.find_all("a", attrs={"target": "_blank"}):
            href = each.get("href")
            if href != "http://job.njupt.edu.cn/html/":
                whole_url = prefix + href
                title = each.get_text()
                with open("CompanyCollection.txt", "a") as f:
                    f.write(title + "\n")
                    f.write(whole_url + "\n")
                    f.write("\n")


if __name__ == '__main__':
    run()
