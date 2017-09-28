import turtle

# 设置颜色
def set_color(color):
    # 设置画笔的颜色
    t.pencolor(color)
    # 设置填充的颜色
    t.fillcolor(color)
    t.hideturtle()  # 隐藏箭头

# 指定画笔的位置
def set_pen(x, y):
    # 将画笔抬起来，不会有线条
    t.penup()
    # 跳到指定坐标
    t.goto(x, y)
    # 将画笔放下来，又会有线条
    t.pendown()
    t.setheading(0)

# x,y是长方形左下角的那个点
def rect(x, y, width, height, color):
    set_color(color)
    set_pen(x, y)
    t.setheading(90)  # 箭头向上
    # 开始填充
    t.begin_fill()
    for i in range(2):
        # 向前走，单位是像素
        t.forward(height)
        # 向右转，单位是角度
        t.right(90)
        t.forward(width)
        t.right(90)
    # 结束填充
    t.end_fill()

# pixel表示一个像素点的大小
# space表示两个像素点之间的距离
def dot(x, y):
    t.pencolor('black')
    # 指定画笔的粗细
    t.pensize(2)
    t.goto(x, y)
    t.begin_fill()
    # 画圆函数
    t.circle(4)
    t.end_fill()

def line_chart(x, y, color, temps, pixel, space, offset):
    set_color(color)
    x = x + offset
    y1 = y + temps[0] * pixel
    set_pen(x, y1)
    dot(x, y1)
    for i, j in enumerate(temps[1:]):
        x1 = x + (i + 1) * space
        y1 = y + j * pixel
        # t.goto(x1,y1)
        dot(x1, y1)

# 画柱状图
def bar_chart(x, y, color, temps, width=500, height=300, space=30):
    axises_wh(x, y, width, height)
    bg_rluer(x, y, width, height)
    n = len(temps)
    # 求出柱子的宽度
    w = (width - (n + 1) * space) / n
    # 求出最高温度
    m = max(temps)
    # 求出温度的高度的比例
    pixel = height * 0.95 / m
    for i, j in enumerate(temps):
        h = j * pixel
        x1 = x + space + (w + space) * i
        if j > 30:
            color = 'red'
        elif 25 < j < 31:
            color = 'blue'
        elif 20 < j < 26:
            color = 'yellow'
        else:
            color = 'green'
        rect(x1, y, w, h, color)
    color = 'red'
    s = space + w
    offset = space + w / 2
    line_chart(x, y, color, temps, pixel, s, offset)

# 画坐标轴
def axises_wh(x, y, width, height):
    set_color('grey')
    set_pen(x, y)
    t.goto(x + width, y)
    set_pen(x, y)
    t.goto(x, y + height)
    set_pen(x, y)


# 画背景标尺
def bg_rluer(x, y, width, height):
    set_color('grey')
    set_pen(x, y)
    height = height / 7
    for i in range(6):
        y1 = y + height * (i + 1)
        set_pen(x, y1)
        t.forward(width)

 # temps里面存放的是一周的天气温度
temps = [16, 17, 22, 30, 21, 27, 24]
# 创建一个turtle对象
t = turtle.Turtle()
# 调节画笔的速度，为0表示最快
t.speed(0)
# rect(-200,-200,400,300,'blue')
# line_chart(0,0,'red',temps,10,20)
bar_chart(-150, -200, 'blue', temps)

# 最后一定要写，否则会报错
turtle.done()
