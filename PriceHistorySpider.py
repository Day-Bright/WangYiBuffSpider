# coding=utf-8

import json
import requests
import time
import DrawPriceCurve

url = "https://buff.163.com/api/market/goods/price_history/buff"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Cookie': 'xxxxxxx'
}
millis = int(round(time.time() * 1000))
param = {
    'game': 'csgo',
    'goods_id': '836044',
    'currency': 'CNY',
    'days': '30',
    '_': millis
}

response = requests.get(url=url, params=param, headers=headers).json()
d = DrawPriceCurve.DrawPriceCurve(response)
d.draw()
