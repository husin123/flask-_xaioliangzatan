from collections import Counter

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot


def read_csv():
    data = pd.read_csv(
        'D:/Code/xaioliangzatan/selm/bosszhipin/data/result.csv')
    # 单单薪资分布
    salary = list(data['薪资'])
    salary_frequency = Counter(salary)
    print(salary_frequency)
    # draw_pie(salary_frequency, '薪资分布')
    # 保存图
    # make_snapshot(snapshot, draw_pie(
    #     salary_frequency, '薪资分布').render(), '薪资分布'+".png")
    # 单单工作年限分布
    work_years = list(data['工作年限'])
    work_years_frequency = Counter(work_years)
    print(work_years_frequency)
    draw_pie(work_years_frequency, '年限分布')
    # 薪资加工作年限分布
    salary_and_years = [salary[i]+work_years[i] for i in range(len(salary))]
    salary_and_years_frequency = Counter(salary_and_years)
    print(salary_and_years_frequency)
    # draw_pie(salary_and_years_frequency, '薪资年限分布')


def draw_pie(data, name):
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(data.keys(), data.values())],
            radius="55%",  # 直径
            center=["50%", "56%"],  # 中心位置
            label_opts=opts.LabelOpts(
                is_show=False, position="center"),  # is_show是否展示数值
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title=name, pos_top="13", pos_left="1%"),  # 标题位置
            legend_opts=opts.LegendOpts(
                orient="vertical", pos_top="25%", pos_left="8%"),  # 图例位置
        )
        # 数值表现形式，这里是百分比
        .set_series_opts(label_opts=opts.LabelOpts(formatter="size{b}: {d}%"))
        .render("年限分布.html")
    )
    return c


if __name__ == '__main__':
    read_csv()
