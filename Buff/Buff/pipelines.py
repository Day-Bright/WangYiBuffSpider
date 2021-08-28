# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class BuffPipeline:
    df = None

    def open_spider(self, spider):
        goods_dict = {'goods_id': '',
                      'goods_name': '',
                      'steam_price_cny(¥)': '',
                      'steam_price($)': '',
                      'buff_price(¥)': ''}
        df = pd.DataFrame(goods_dict, index=[0])
        df.to_csv(r"C:\Users\Me\Desktop\BuffSpider\goods_price.csv", index=False, encoding='utf_8_sig', mode='w',
                  )

    def process_item(self, item, spider):
        goods_id = item['goods_id']
        goods_name = item['goods_name']
        steam_price_cny = item['steam_price_cny']
        steam_price = item['steam_price']
        buff_price = item['buff_price']
        goods_dict = {'goods_id': goods_id,
                      'goods_name': goods_name,
                      'steam_price_cny(¥)': steam_price_cny,
                      'steam_price($)': steam_price,
                      'buff_price(¥)': buff_price}
        df = pd.DataFrame(goods_dict, index=[0])
        df.to_csv(r"C:\Users\Me\Desktop\BuffSpider\goods_price.csv", index=False, encoding='utf_8_sig', mode='a',
                  na_rep='null', header=False)
        return item
