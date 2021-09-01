# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import pymongo


class BuffPipeline:

    """
    写入csv文件

    df = None

    def open_spider(self, spider):
        goods_dict = {'goods_id': '',
                      'goods_name': '',
                      'steam_price_cny(¥)': '',
                      'steam_price($)': '',
                      'buff_price(¥)': ''}
        BuffPipeline.df = pd.DataFrame(goods_dict, index=[0])
        BuffPipeline.df.to_csv(r"C:\Users\Me\Desktop\BuffSpider\goods_price.csv", index=False, encoding='utf_8_sig',
                               mode='w')

    def process_item(self, item, spider):
        BuffPipeline.df = pd.DataFrame(dict(item), index=[0])
        BuffPipeline.df.to_csv(r"C:\Users\Me\Desktop\BuffSpider\goods_price.csv", index=False, encoding='utf_8_sig',
                               mode='a', na_rep='null', header=False)
        return item

    """

    """
    
    写入MongoDB
    
    def __init__(self):
        super().__init__()
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["test"]
        self.col = db["price"]

    def process_item(self, item, spider):
        print(item)
        self.col.insert_one(dict(item))
        return item
    
    """
