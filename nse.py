import requests
import json
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'bm_sv=921CF32228FDB8F51295014D72A8D25C~YAAQ3YosMf8KWTWQAQAA1gcfThhaZpDRSwKMWvy9JIZUcgpwvAMB9yibl19sGDcC1cnLiYvjuHJo8JBEFA2I+GFcxyLn2dwfHJn43+3xqq8DWogcQt4m8ThkUSD97sor8T8AIoufT2payYIOOS243mAzvlkiJpDsEZEiucL8IMoHNuK50X4meEAqzQMQOx0Ju4rlY3AQVM52Zxlv2x8qa4XYhkzWqp65ArnqnXA5bbcMsB1cFv71uqw4tLlQykVZcuyu~1'
    }
url = 'https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O'
r = requests.get(url, headers=headers)
data = r.json()
# db = json.load(data)
db = pd.DataFrame(data["data"])

print(db[["symbol","pChange","change", "totalTradedVolume"]])
