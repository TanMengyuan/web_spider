#   巴黎世家+鞋 1500元
#   MK女包+中号 800元【需要重做】
#   LV围巾 2500元
#   Supreme联名卫衣 1500元
#   gucci+女包 3000元【需要重做】
#
#



import requests
import re
from selenium import webdriver
import time
import xlwt


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        # print(r.text)
        return r.text
    except:
        return ""

def getHTMLText_by_selenium(url):
    drive = webdriver.Chrome()
    drive.get(url)
    time.sleep(1)
    html = drive.page_source
    drive.quit()

    return html


def getScore(url):
    res = []
    html = getHTMLText_by_selenium('https:' + url)
    pattern = r'//rate.taobao.com/user-rate-.*.htm'
    score_url = re.findall(pattern, html)[0]
    score_html = getHTMLText('https:' + score_url)
    score_pattern = r'\d\.\d*分'
    score = re.findall(score_pattern, score_html)
    if 'taobao.com' in url:
        res = score[::2]
    elif 'tmall.com' in url:
        res = score[3::2]

    return res

def parsePage(ilt, html):
    try:
        plt = re.findall(r'"view_price":"[\d\.]*"',html)
        tlt = re.findall(r'"raw_title":".*?"',html)
        ult = re.findall(r'"detail_url":".*?"', html)
        llt = re.findall(r'"item_loc":".*?"', html)
        slt = re.findall(r'"view_sales":"\d*人付款"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            detail_url = eval(ult[i].split(':')[1])
            loc = eval(llt[i].split(':')[1])
            sale = eval(slt[i].split(':')[1])
            ilt.append([price, title, detail_url, loc, sale])
    except:
        print("")

def printGoodsList(ilt):
    data = []
    tplt = "{:4}\t{:8}\t{:8}\t{:8}\t{:8}"
    # print(tplt.format("序号","价格","名称","产地","销量"))
    count = 0
    for g in ilt:
        price = float(g[0])
        if price < 3000:
            score = []
            # score_str = ' '.join(score)
            count = count + 1
            # print(tplt.format(count, g[0], g[1], g[3], g[4]))
            if len(score) >= 3:
                data.append([count, g[0], g[1], g[3], g[4][:-3], score[0], score[1], score[2]])
            else:
                data.append([count, g[0], g[1], g[3], g[4][:-3]])

    return data


def main():
    goods = 'gucci+女包'
    depth = 10
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            print(url)
            # html = getHTMLText_by_selenium(url)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    save_data = printGoodsList(infoList)
    print(save_data)
    if save_data:
        save_path = r'E:\sola\NJUPT\Temp\data_' + goods + '.xls'
        f = xlwt.Workbook()
        sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
        for i in range(len(save_data)):
            for j in range(len(save_data[i])):
                sheet1.write(i + 1, j, save_data[i][j])
        f.save(save_path)
        print('save successful on ', save_path)

if __name__ == '__main__':
    main()