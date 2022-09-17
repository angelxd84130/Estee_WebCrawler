import os, json
import pandas as pd
def getFilePass() -> list[str]:
    json_files = [pos_json for pos_json in os.listdir() if pos_json.endswith('.json')]
    return json_files

def fileMapping():
    jFiles = getFilePass()
    jsonList = []
    for j in jFiles:
        try:
             with open(j, 'r+', encoding='utf8') as f:
                content = json.load(f)
                f.close()
        except:
            content = []
        jsonList += content
        print("add file:", j,  "len:", len(jsonList))

        with open("data.json", "w+", encoding='utf8') as f:
            f.write(json.dumps(jsonList, indent=4, ensure_ascii=False))
            f.close()
        print("finish mapping")




fileMapping()