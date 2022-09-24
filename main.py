import pymongo
import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm
from flask import Flask
from flask import request
import json
from cunghoangdao1 import hoang_dao
from get_imotion import get_imotion
from thoitiet import getWeather
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
start_col = 7
mydb = myclient["SmartTourist"]
print(myclient.list_database_names())
collist = mydb.list_collection_names()
print(collist)
input_api = {
    "image": "",  # picture
    "color": "",  # RED, YELLOW, SKYBLUE, GREEN, PINK, PURPLE,BROWN, ORANGE
    "weather": "",# ["clear sky","shower rain", "rain","thunder storm","few clouds","snow","scattered cloud","broken cloud"]
    "temperature":"",#nhiet do
    "day_or_night": "",  # MORNING, NIGHT, MORNING_A_NIGHT
    "day_of_birth": ""  # 24/3
}

data = pd.DataFrame()
mycol = mydb["dataDestination"]
index = 0
for x in mycol.find(): # ko query điều kiện nào và lấy tất cả các field
    # xs = x
    m = pd.DataFrame(x,index=[index])
    index+=1
    data = pd.concat([data,m], axis=0)
data.dropna(inplace=True)
for col in data.columns[start_col:]:
    data[col] = data[col].astype(float)
    print(col)
print("col")
api_string = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0,
              1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1]


def get_cosin(x):
    cos_sim = dot(api_string, x)/(norm(api_string)*norm(x))
    return cos_sim


def get_top_sim(top: int, api_string):
    api_string = api_string
    data["result"] = data[data.columns[start_col:]].apply(get_cosin, axis=1)
    k = data.sort_values("result", ascending=False).head(top)[['ID', 'Name', 'ADDRESS', 'ADDRESS_LINK','IMG2']].to_json(orient = "records",force_ascii = False)
    return k


# get_top_sim(10,api_string)
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method == 'POST':
        body = json.loads(request.data)
        # print(body)
        # print(type(body))
        dict = {}
        for col in data.columns[start_col:]:
            # print(col)
            dict[col] = 0
        thoitiet = getWeather(body["weather"],body["temperature"])
        for tt in thoitiet:
            dict[tt] = 1
        
        dict[body["day_or_night"]] = 1
        date_of_birth = body["day_of_birth"].split("/")
        print(date_of_birth)
        chd = hoang_dao(int(date_of_birth[0]),int(date_of_birth[1]))
        dict[chd]= 1
        print(chd)
        print(dict)
        emote = get_imotion(body["image"])
        dict["ANY_TIME"] = 1
        dict[emote] = 1
        dict["MORNING_A_NIGHT"] = 1
        print(list(dict.values()))
        lst_binary = list(dict.values())
        output = get_top_sim(10,lst_binary)
        return output


if __name__ == '__main__':
    app.run(debug=True)
