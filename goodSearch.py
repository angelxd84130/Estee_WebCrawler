from bs4 import BeautifulSoup
import json
from urllib import request
from datetime import datetime
import time
import re

global timestamp

def getParm(goodId) -> str:
    url = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code="\
          + str(goodId) \
          + "&Area=search&mdiv=403&oid=3_2&cid=index&kw=%E9%9B%85%E8%A9%A9%E8%98%AD%E9%BB%9B"

    return url


def loadPage(goodId=9486768) -> json:
    url = getParm(goodId)
    #print(url)
    resp = request.urlopen(url)
    html = resp.read()
    soup = BeautifulSoup(html, "html.parser")
    return soup


def goodPrice(soup) -> dict:
    prices = soup.select('.prdPrice')[0]
    priceDict = {}
    for li in prices.find_all('li'):
        l = li.text
        key = re.findall("([\D]+)([\d,]+)", l)[0][0]
        value = int(re.findall("([\D]+)([\d,]+)", l)[0][1].replace(',', ''))
        priceDict[key] = value

    return priceDict

def getConmbo(soup) -> str:
    cTime = soup.find_all('ul', {'class': 'ineventArea'})[0]
    for li in cTime.find_all('li'):
        cStr = li.text.split()
        break
    return cStr[0]

def getTimeStamp() -> int:
    timestamp = int(time.time())
    #print("Date time object:", datetime.fromtimestamp(timestamp))
    return timestamp

def getGoodType(soup) -> str:
    goodRoot = ''
    root = soup.find_all('div', {'class': 'bt770class'})[0]
    for li in root.find_all('li'):
        if goodRoot != '':
            goodRoot += '\\'
        goodRoot += li.text
    return goodRoot

def getGoodInfo(soup) -> str:
    info = []
    root = soup.find_all('ul', {'class': 'categoryActivityInfo gmclass'})[0]
    i = 0
    for li in root.find_all('li'):
        if i > 0:
            info.append(li.text)
        i += 1
    return str(info)

def getGoodDesc(goodID) -> json:
    soup = loadPage(goodID)
    timestamp = getTimeStamp()
    Dec = {}
    try:
        Dec['品牌'] = soup.find_all('meta', {'property': 'product:brand'})[0]['content']
    except:
        pass
    try:
        Dec['產品編號'] = soup.find_all('meta', {'property': 'product:retailer_item_id'})[0]['content']
    except:
        pass
    try:
        Dec['產品名'] = soup.find_all('meta', {'property': 'og:title'})[0]['content']
    except:
        pass
    try:
        Dec['產品系列'] = getGoodType(soup)
    except:
        pass
    try:
        Dec['優惠期間'] = getConmbo(soup)
    except:
        pass
    try:
        Dec['產品描述'] = getGoodInfo(soup)
    except:
        pass
    try:
        Dec['所有價格'] = goodPrice(soup)
    except:
        pass
    try:
        Dec['資料更新時間'] = str(datetime.fromtimestamp(timestamp))
    except:
        pass
    return Dec
    #Dec['容量']
    #print('產品特色:')
    #print('產品規格:')
    #print('產品圖片路徑')

#print(getGoodDesc(goodID=9486768))
