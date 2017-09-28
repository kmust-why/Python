import xlsxwriter
'''
#1、创建一个excel文件
work = xlsxwriter.Workbook('test.xlsx')
#22、创建图表
chart = work.add_chart({type,'column'})
    #column 柱状图
    #area 面积图
    #bar 条形图
    #line 折线图
    #radar 雷达图


#2、创建表格
worksheet = work.add_worksheet('why')
worksheet.insert_chart('A1',chart)
#33、添加数据
    #1）声明一个数据的容器
data = [1,3,34,56,22,11,23,33]
#3、修改内容的格式
#1）表格的格式
worksheet.set_column('A:A',20)
#2）内容的格式
bold = work.add_format({'bold':True})#定义一个内容样式
#4、写入内容
#1）写入字符
worksheet.write('A1','李四',bold)
#2）写入图片
worksheet.insert_image('A2','Python.png')
#3）写入函数
worksheet.write('A3',8,bold)
worksheet.write('A4',9,bold)
worksheet.write('A5','=SUM(A3:A4)',bold)
#关闭并且保存excel
work.close()



'''
#1、创建一个excel文件
work = xlsxwriter.Workbook('test.xlsx')
#2、创建图表
chart = work.add_chart({'type':'column'})
    #column 柱状图
    #area 面积图
    #bar 条形图
    #line 折线图
    #radar 雷达图


#3、创建表格
worksheet = work.add_worksheet('why')

#4、添加数据
    #1）声明一个数据的容器
title = 'abcdefgh'
data = [1,3,34,56,22,11,23,33]
for i,j in enumerate(title):
    point = 'A%d' %(i+1)
    worksheet.write_string(point,j)

for i,j in enumerate(data):
    point = 'B%d' %(i+1)
    worksheet.write(point,j)

#5、为图表添加数据

chart.add_series(
    {
        'categories':'=why!$a$1:$a$8',#类别标签的范围
        'values':'=why!$b$1:$b$8',#图标数据的范围
        'line':{'color':'red'},#图标线条的属性
    }
)
worksheet.insert_chart('A10',chart)
#关闭并且保存excel
work.close()