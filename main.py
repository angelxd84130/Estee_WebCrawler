import json
import time
import schedule
import textSearch as t
import goodSearch as g
from datetime import datetime
day = 1
fileName = "data.json"

def dailyLoad():
    goodList = t.getGoodId()
    global fileName
    print("update time: ", datetime.fromtimestamp(g.getTimeStamp()))

    try:
         with open(fileName, 'r+', encoding='utf8') as f:
            jsonList = json.load(f)
            f.close()
    except:
        jsonList = []

    with open(fileName, "w+", encoding='utf8') as f:
        for id in goodList:
            goodSet = g.getGoodDesc(int(id))
            jsonList.append(goodSet)
        print("len:", len(jsonList))
        f.write(json.dumps(jsonList, indent=4, ensure_ascii=False))
        f.close()

def day_update():
    global day
    print("finish:", day)
    day += 1

if __name__ == '__main__':
    schedule.every().day.at("12:00").do(dailyLoad)
    schedule.every().day.at("15:00").do(dailyLoad)
    schedule.every().day.at("18:00").do(dailyLoad)
    while True:
        schedule.run_pending()
        time.sleep(1)




