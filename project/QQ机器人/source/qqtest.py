#该程序存在bug


#1、引入模块
from qqbot import QQBot
#QQBot就是一个qq登陆的实例
bot = QQBot()#实例化一个qq实例
bot.Login()#进行登陆，执行这条命令，系统会弹出一个二维码，我们扫码登陆即可
#使用脚本来查看用户和群
user_list = bot.List('buddy')#获得所有的用户
for user in user_list:
    print(user)
group_list = bot.List('group')#获取所有的群
for group in group_list:
    if group == '不仅仅喇叭':
        #发送消息
        bot.SendTo(group,'大家好，这是王海云的机器人')
        #print(group)
bot.Stop()#退出qq