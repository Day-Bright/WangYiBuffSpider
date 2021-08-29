# coding=utf-8

import json
import random

import requests
import time
import DrawPriceCurve
import USER_AGENT


def get_response(goods_id):
    url = "https://buff.163.com/api/market/goods/price_history/buff"
    headers = {
        'User-Agent': random.choice(USER_AGENT.user_agent_list),
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://buff.163.com/goods/{goods_id}'.format(goods_id=goods_id),
        'Cookie': 'xxx'
    }
    millis = int(round(time.time() * 1000))
    param = {
        'game': 'csgo',
        'goods_id': goods_id,
        'currency': 'CNY',
        'days': '30',
        '_': millis
    }
    response = requests.get(url=url, params=param, headers=headers).json()
    return response


if __name__ == "__main__":
    with open(r'C:\Users\Me\Desktop\BuffSpider\items_id\Pass.json', 'r', encoding='utf-8') as f:
        goods_dict = json.load(f)
    for key, value in goods_dict.items():
        response = get_response(goods_id=key)
        d = DrawPriceCurve.DrawPriceCurve(response, value)
        d.draw()

