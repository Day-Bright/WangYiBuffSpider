# coding=utf-8

import json
import requests
import time
import DrawPriceCurve

url = "https://buff.163.com/api/market/goods/price_history/buff"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Cookie': '_ntes_nnid=487b76e0a8d34fe0ab2dfefc3dc75fc2,1622040656010; _ntes_nuid=487b76e0a8d34fe0ab2dfefc3dc75fc2; vinfo_n_f_l_n3=d663b59207e8fa5a.1.0.1622873739675.0.1622873826619; Qs_lvt_382223=1623155426; Qs_pv_382223=4491720422195489000; _ga_C6TGHFPQ1H=GS1.1.1623155426.1.0.1623156006.0; Device-Id=r6AffQVttkdhf0UFC8n3; _ga=GA1.2.302472162.1623155426; _gid=GA1.2.1622359838.1630133184; game=csgo; Locale-Supported=zh-Hans; _gat_gtag_UA_109989484_1=1; NTES_YD_SESS=K0YK.X.yrn1fjZ7aHX8spSBwuZYd6i4OpZ.AtVg2t6JcUGQvUZBPoCZIJMmjhQaFw8D7IgP5fXubJ1t1Q9XlqrAN2hHqAeUZoSvZVPKgfZixaG5Z9F_LbMHgT_rnq7XD5ecKKwggl32BCKAuZr8mj0AFSo5NyQJAdBJPV4Sb84Xz1vdJixkTFyWweSekVak1Zq7nrSyUJjbRA9WBXGm5dadETFcbaU2wjzTC5ony7AdSj; S_INFO=1630159705|0|3&80##|13777321762; P_INFO=13777321762|1630159705|1|netease_buff|00&99|zhj&1628699183&netease_buff#zhj&330600#10#0#0|&0|null|13777321762; remember_me=U1091635307|vjPbOmbFvEUXcnCdANukLzqTbiJFsboA; session=1-FpQyW8UMC5qpNz4L36a6ef8xnuherusz2IA3Kth1gWLK2044696371; csrf_token=IjY0ODNiOGI5NjQ2NGM5M2QyMjcxYWUzZjQyYzI4NmQ3YjAyZDA4ZTAi.FAvU4w.Mw89bLtnbWGD16h0bz925djbr7E'
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
