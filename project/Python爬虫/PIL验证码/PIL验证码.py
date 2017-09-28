#coding:utf-8
import random #随机数模块，可以生成随机数
from PIL import Image,ImageDraw,ImageFont,ImageFilter

#Image 负责处理图片
#ImageDraw 负责处理画笔
#ImageFont 负责处理字体
#ImageFilter 负责处理滤镜

#生成验证码的步骤
#1.定义一张图片
#第一个参数表示采用RGB颜色模式，第二个参数表示图片的大小，第三个表示具体图片的颜色
img = Image.new('RGB',(150,50),(255,255,255))

#2.创建画笔
draw = ImageDraw.Draw(img) #表明该画笔是该图片的
#绘制线条和点
#先生成线条
for i in range(random.randint(1,10)):
    draw.line(
        [
            (random.randint(1,150),random.randint(1,150)),#每条线有两个点构成，每个点考x,y来确定位置
            (random.randint(1,150),random.randint(1,150))
        ],
        fill = (0,0,0) #定义线条的颜色为黑色
    )

#绘制点
for i in range(1000):
    draw.point(
        [
            random.randint(1,150), #x坐标
            random.randint(1, 150) #y坐标
        ],
        fill = (0,0,0)
    )

#绘制文字
#1.文字是随机产生的
#2.文字的个数是一定的
    #1.定义要生成的随机数的字母和数字
fontList = list('abcdefgABCDEFG')
#random.sample()是在指定的列表中随机的取出指定个数的元素
c_chars = ' '.join(random.sample(fontList,5))
#绘制文字
#需要先定制字体
font = ImageFont.truetype('simsun.ttc',24)
draw.text((5,5),c_chars,font=font,fill='green')
#第一个参数表示文字的位置距离上和左的距离
#第二个参数表示文字的内容
#第三个参数表示字体
#第四个参数表示字的颜色

#先定义扭曲的参数
params = [1 - float(random.randint(1,2)) / 100,
    0,
    0,
    0,

    1 - float(random.randint(1,2)) / 100,
    float(random.randint(1,2)) / 500,
    0.001,
    float(random.randint(1, 2)) / 500,

]
#使用滤镜
img = img.transform((150,50),Image.PERSPECTIVE,params)
#进行图片的扭曲
img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
img.show() #显示图片

