import requests
import json
import pandas as pd
import numpy as np


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


url = "https://disclosure.edinet-fsa.go.jp/api/v1/documents.json?date=2019-04-01&type=2"
js = get_json_from_url(url)
df = pd.DataFrame(data=js['results'])
print(f"Loaded data into dataframe : {len(df)}")

print(f"Asset management one info:\n{df.loc[df.filerName == 'アセットマネジメントＯｎｅ株式会社', ['fundCode', 'docID', 'docDescription']]}")
