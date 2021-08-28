import json
from pylab import *


class DrawPriceCurve(object):
    font = {
        'fontsize': 50,
        'fontweight': 'bold',
        'verticalalignment': 'center',
        'horizontalalignment': 'center',
    }

    def __init__(self, price_dict):
        self.price_dict = price_dict

    def unix(self, timestamp_int):
        timestamp = int(timestamp_int / 1000)
        time_local = time.localtime(timestamp)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        return dt[5:-9]

    def draw(self):
        price_history_list = self.price_dict['data']['price_history']
        time_list = []
        price_list = []
        for i in range(len(price_history_list)):
            date = self.unix(price_history_list[i][0])
            price_list.append(price_history_list[i][1])
            if date != self.unix(price_history_list[i - 1][0]):
                time_list.append(date)
            else:
                time_list.append('')

        mpl.rcParams['font.sans-serif'] = ['SimHei']
        x = range(len(time_list))
        plt.figure(figsize=(50, 20))
        plt.plot(x, price_list, marker='o', mec='r', mfc='w', label='价格折线', linewidth=5)
        plt.legend()  # 让图例生效
        plt.xticks(x, time_list, color='blue', rotation=60, size=30, weight='bold')  # size=30, weight='bold'
        plt.yticks(size=30, weight='bold')
        plt.margins(0.02, 0.02)  # 设置x,y轴边距
        plt.subplots_adjust(bottom=0.15)
        plt.xlabel("time", DrawPriceCurve.font)  # X轴标签
        plt.ylabel("price", DrawPriceCurve.font)  # Y轴标签
        plt.title("价格折线图", DrawPriceCurve.font)  # 标题
        plt.show()


if __name__ == "__main__":
    price_dict = {'code': 'OK', 'data': {'currency': '人民币', 'currency_symbol': '¥', 'days': 30,
                                         'price_history': [[1627495200000, 7030.0], [1627520400000, 7150.0],
                                                           [1627545600000, 7750.0], [1627563600000, 7030.0],
                                                           [1627578000000, 7020.0], [1627581600000, 7030.0],
                                                           [1627599600000, 7020.0], [1627617600000, 7200.0],
                                                           [1627657200000, 7689.0], [1627761600000, 7000.0],
                                                           [1627797600000, 7000.0], [1627804800000, 7000.0],
                                                           [1627815600000, 6900.0], [1627844400000, 7200.0],
                                                           [1627869600000, 7000.0], [1627887600000, 7000.0],
                                                           [1627902000000, 7200.0], [1627905600000, 7199.0],
                                                           [1627912800000, 7000.0], [1627956000000, 7000.0],
                                                           [1627963200000, 7490.0], [1627966800000, 6720.0],
                                                           [1627984800000, 7000.0], [1627995600000, 7000.0],
                                                           [1628013600000, 6700.0], [1628060400000, 8666.0],
                                                           [1628125200000, 6980.0], [1628143200000, 6999.5],
                                                           [1628146800000, 6600.0], [1628157600000, 7000.0],
                                                           [1628233200000, 6620.0], [1628236800000, 6610.0],
                                                           [1628251200000, 6999.0], [1628308800000, 6999.0],
                                                           [1628337600000, 7214.75], [1628344800000, 6995.0],
                                                           [1628359200000, 6946.5], [1628402400000, 7300.0],
                                                           [1628413200000, 6670.0], [1628438400000, 6650.0],
                                                           [1628474400000, 7749.83], [1628492400000, 7001.14],
                                                           [1628503200000, 6700.0], [1628510400000, 6770.0],
                                                           [1628532000000, 7000.0], [1628560800000, 6820.0],
                                                           [1628571600000, 6820.0], [1628593200000, 7025.0],
                                                           [1628607600000, 7040.0], [1628650800000, 6750.0],
                                                           [1628668800000, 7980.0], [1628676000000, 7650.0],
                                                           [1628679600000, 7135.36], [1628686800000, 6870.0],
                                                           [1628694000000, 7000.0], [1628740800000, 6850.0],
                                                           [1628758800000, 6830.0], [1628769600000, 6830.0],
                                                           [1628805600000, 7050.0], [1628841600000, 7350.0],
                                                           [1628845200000, 7100.0], [1628877600000, 6900.0],
                                                           [1628967600000, 6919.0], [1628985600000, 6920.0],
                                                           [1629007200000, 7474.5], [1629014400000, 6930.0],
                                                           [1629036000000, 7000.0], [1629039600000, 6950.0],
                                                           [1629046800000, 7100.0], [1629050400000, 6950.0],
                                                           [1629100800000, 7188.0], [1629108000000, 6900.0],
                                                           [1629111600000, 7289.5], [1629115200000, 7030.0],
                                                           [1629118800000, 7658.33], [1629205200000, 6988.0],
                                                           [1629219600000, 7000.0], [1629259200000, 6860.0],
                                                           [1629270000000, 6900.0], [1629280800000, 6700.0],
                                                           [1629291600000, 6900.0], [1629302400000, 7111.0],
                                                           [1629417600000, 6810.0], [1629446400000, 6850.0],
                                                           [1629453600000, 12508.0], [1629468000000, 6850.0],
                                                           [1629482400000, 6850.0], [1629518400000, 6840.0],
                                                           [1629554400000, 7294.0], [1629633600000, 8040.0],
                                                           [1629637200000, 6955.0], [1629644400000, 8000.0],
                                                           [1629774000000, 7100.0], [1629788400000, 8222.0],
                                                           [1629792000000, 7000.0], [1629878400000, 6760.0],
                                                           [1629885600000, 6780.0], [1629903600000, 6600.0],
                                                           [1629946800000, 6700.0], [1629993600000, 7000.0],
                                                           [1630004400000, 6700.0], [1630047600000, 6575.0],
                                                           [1630051200000, 8300.0], [1630072800000, 7066.0],
                                                           [1630080000000, 6814.59], [1630123200000, 6680.0],
                                                           [1630126800000, 6570.0], [1630152000000, 6560.0]],
                                         'price_type': 'BUFF价格', 'steam_price_currency': '美元'}, 'msg': None}
    d = DrawPriceCurve(price_dict)
    d.draw()