import requests
import json
from urllib import request

def getParm(curPage=1) -> (str, json):
    url = "https://apisearch.momoshop.com.tw/momoSearchCloud/moec/textSearch"

    payload = json.dumps({
        "host": "momoshop",
        "flag": "searchEngine",
        "data": {
            "specialGoodsType": "",
            "isBrandSeriesPage": False,
            "authorNo": "",
            "searchValue": "雅詩蘭黛",
            "cateCode": "",
            "cateLevel": "-1",
            "cp": "N",
            "NAM": "N",
            "first": "N",
            "freeze": "N",
            "superstore": "N",
            "tvshop": "N",
            "china": "N",
            "tomorrow": "N",
            "stockYN": "N",
            "prefere": "N",
            "threeHours": "N",
            "video": "N",
            "cycle": "N",
            "cod": "N",
            "superstorePay": "N",
            "showType": "chessboardType",
            "curPage": str(curPage),
            "priceS": "0",
            "priceE": "9999999",
            "searchType": "1",
            "reduceKeyword": "",
            "isFuzzy": "0",
            "rtnCateDatainfo": {
                "cateCode": "",
                "cateLv": "-1",
                "keyword": "雅詩蘭黛",
                "curPage": str(curPage),
                "historyDoPush": False,
                "timestamp": 1662751510278
            },
            "flag": 2018
        }
    })
    return (url, payload)


def loadPage(url, payload) -> json:

    '''
    headers = {
      'Content-Type': 'application/json',
      "Connection": "keep-alive"
    }
    response = requests.request("POST", url, headers=headers, data=payload, timeout=5000, verify=True)
    print(response.text)
    '''

    payload = str(payload)
    data = payload.encode('utf-8')
    req = request.Request(url, data=data)
    req.add_header('Content-Type', 'application/json')
    resp = request.urlopen(req)
    html = resp.read().decode()
    js = json.loads(html)
    #print(json.dumps(js, indent=4))  #  print out contents in json format
    return js


def getGoodId() -> list[str]:
    goodIdList = []
    curPage = 1
    while True:
        try:
            (url, payload) = getParm(curPage=curPage)
            js = loadPage(url, payload)
            goodInfo = js['rtnSearchData']['goodsInfoList']
            for good in goodInfo:
                goodIdList.append(good['goodsCode'])
            #print('page:', curPage, 'good #:', len(goodIdList))  #  check how many goods in total
            curPage += 1
        except:
            break
    return goodIdList


#print(getGoodId())