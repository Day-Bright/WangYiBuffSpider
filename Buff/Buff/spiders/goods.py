import random
import scrapy
import json
import time
from Buff.items import BuffItem
import USER_AGENT


class GoodsSpider(scrapy.Spider):
    with open(r'C:\Users\Me\Desktop\BuffSpider\items_id\Pass.json', 'r', encoding='utf-8') as f:
        goods_dict = json.load(f)
    name = 'goods'

    # allowed_domains = ['www.x.com']
    # start_urls = [
    #     'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=779203&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&_=1629125513211']

    def start_requests(self):
        millis = int(round(time.time() * 1000))
        for goods_id in GoodsSpider.goods_dict:
            headers = {
                'User-Agent': random.choice(USER_AGENT.user_agent_list),
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'zh-CN',
                'Accept-Encoding': 'gzip, deflate, br',
                'X-Requested-With': 'XMLHttpRequest',
                'referer': 'https://buff.163.com/goods/{goods_id}'.format(goods_id=goods_id)
            }
            url = "https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id={goods_id}&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&_={millis}".format(
                goods_id=goods_id, millis=millis)
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                headers=headers,
            )

    def parse(self, response):
        item = BuffItem()
        goods_data = json.loads(response.body)
        goods_id = list(goods_data['data']['goods_infos'].keys())[0]
        goods_name = goods_data['data']['goods_infos'][goods_id]['name']  # 物品名称
        steam_price_cny = float(goods_data['data']['goods_infos'][goods_id]['steam_price_cny'])  # steam价格RMB
        steam_price = float(goods_data['data']['goods_infos'][goods_id]['steam_price'])  # steam价格美元
        buff_price = float(goods_data['data']['items'][0]['price'])  # buff底价
        item['goods_id'] = goods_id
        item['goods_name'] = goods_name
        item['steam_price_cny'] = steam_price_cny
        item['steam_price'] = steam_price
        item['buff_price'] = buff_price
        yield item
