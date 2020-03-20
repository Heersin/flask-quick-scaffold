from pyecharts import options as opts
from pyecharts.charts import Parallel, Liquid, HeatMap
from pyecharts.faker import Faker
import random

parallel_axis = [
    {"dim":0, "name":"A"},
    {"dim":1, "name":"B"},
    {"dim":2, "name":"C"},
    {
        "dim":3,
        "name":"Score",
        "type":"category",
        "data":["Excellent", "Good", "OK", "Bad"],
    },
]

parallel_data = [[12.99, 100, 82, "Good"],[9.99, 80, 77, "OK"],[20,120,60, "Excellent"]]
# init_opts=opts.InitOpts(width="800px",height="300px")
parallel = Parallel(init_opts=opts.InitOpts(width="800px",height="300px"))
parallel.add_schema(parallel_axis)
parallel.add(
    series_name="Related Indexes",
    data=parallel_data,
    linestyle_opts=opts.LineStyleOpts(width=4, opacity=0.5)
)


liquid = Liquid(init_opts=opts.InitOpts(width="300px",height="300px"))
liquid.add("liquid", [0.6,0.7,0.3])
liquid.set_global_opts(title_opts=opts.TitleOpts(title="Basic Example"))


heatmap_data = [[i, j, random.randint(0, 50)] for i in range(7) for j in range(7)]
heatmap = HeatMap()
heatmap.add_xaxis(Faker.week)
heatmap.add_yaxis(
    "相关表",
    Faker.week,
    heatmap_data,
    label_opts=opts.LabelOpts(is_show=True, position="inside"),
)

heatmap.set_global_opts(
        title_opts=opts.TitleOpts(title="HeatMap-Label 显示"),
        visualmap_opts=opts.VisualMapOpts(),
)

