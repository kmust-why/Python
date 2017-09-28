from flask import Flask
from flask import request
from xml.etree import ElementTree as ET
from flask import render_template
#from face import getFaceInfo

app = Flask(__name__)

@app.route('/')#表示定义首页的路由
def index():#处理首页的请求
    return 'hello world.'

@app.route('/wx',methods=['GET','POST'])
def wx():
    if request.method == 'GET':
        echostr = request.args.get('echostr')#接受用户get请求的数据
        #return '1'
        return echostr
    else:
        data = request.get_data()#获取请求的数据包
        xml = ET.fromstring(data)
        #xml = ET.tostring(data)
        ToUserName = xml.findtext('.//ToUserName')
        FromUserName = xml.findtext('.//FromUserName')
        CreateTime = xml.findtext('.//CreateTime')
        MsgType = xml.findtext('.//MsgType')
        Content = xml.findtext('.//Content')
        MsgId = xml.findtext('.//MsgId')
        #print(ToUserName,FromUserName,CreateTime,MsgType,Content,MsgId)

        if MsgType == 'text':
            res = 0
            if '+' in Content:
                numbers = Content.split('+')
                for number in numbers:
                    res += int(number)
            #print(data)
            #return data
            return render_template('weixin.html',ToUserName=FromUserName,FromUserName=ToUserName,CreateTime=CreateTime,Content=res)
        elif MsgType == 'image':
            return render_template('weixin.html', ToUserName=FromUserName, FromUserName=ToUserName,
                                   CreateTime=CreateTime, Content='人脸识别')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)