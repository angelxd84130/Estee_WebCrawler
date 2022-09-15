import json
import time

import textSearch as t
import goodSearch as g

def dailyLoad():
    goodList = t.getGoodId()

    try:
        with open("output.json", 'r') as f:
            jsonList = json.loads(f.read())
            print(len(jsonList))
            f.close()
    except:
        jsonList = []

    with open("output.json", "w+", encoding='utf8') as f:

        for id in goodList:
            print(id)
            goodSet = g.getGoodDesc(int(id))
            jsonList.append(goodSet)
        print("len:", len(jsonList))
        f.write(json.dumps(jsonList, indent=4, ensure_ascii=False))
        f.close()



if __name__ == '__main__':
    i = 1
    while True:
        dailyLoad()
        time.sleep(60*30)
        print("finish:", i)



