# -*- coding: utf-8 -*-

import json
import requests
import time
import asyncio
import aiohttp
import random
import pandas as pd
import USER_AGENT

with open(r'items_id/Pass.json', 'r', encoding='utf-8') as f:
    goods_dict = json.load(f)

goods_price_list = []

for goods_id in goods_dict:
    url = "https://buff.163.com/api/market/goods/sell_order"
    headers = {
        'User-Agent': random.choice(USER_AGENT.user_agent_list),
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'referer': 'https://buff.163.com/goods/{goods_id}'.format(goods_id=goods_id)
    }
    millis = int(round(time.time() * 1000))
    param = {
        'game': 'csgo',
        'goods_id': goods_id,
        'page_num': '1',
        'sort_by': 'default',
        'mode': '',
        'allow_tradable_cooldown': '1',
        '_': millis,
    }

    goods_response = requests.get(url=url, params=param, headers=headers)
    if goods_response.content:
        goods_response = goods_response.json()
    else:
        pass
    goods_id = list(goods_response['data']['goods_infos'].keys())[0]
    goods_name = goods_response['data']['goods_infos'][goods_id]['name']  # 物品名称
    steam_price_cny = float(goods_response['data']['goods_infos'][goods_id]['steam_price_cny'])  # steam价格RMB
    steam_price = float(goods_response['data']['goods_infos'][goods_id]['steam_price'])  # steam价格美元
    buff_price = float(goods_response['data']['items'][0]['price'])  # buff底价
    price_dict = {'goods_id': goods_id,
                  'goods_name': '%s' % goods_name,
                  'steam_price_cny(¥)': '%s' % steam_price_cny,
                  'steam_price($)': '%s' % steam_price,
                  'buff_price(¥)': '%s' % buff_price
                  }

    goods_price_list.append(price_dict)

df = pd.DataFrame(goods_price_list, columns=['goods_id',
                                             'goods_name',
                                             'steam_price_cny(¥)',
                                             'steam_price($)',
                                             'buff_price(¥)'])

df.to_csv(r"C:\Users\Me\Desktop\BuffSpider\goods_price.csv", index=False, encoding='utf_8_sig', mode='a', na_rep='null')
# price_json = json.dumps(price_dict, indent=4, ensure_ascii=False, sort_keys=False, separators=(',', ':'))
# print(price_json)
# print(buff_price/steam_price_cny)
