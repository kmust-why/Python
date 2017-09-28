from qqbot import QQBot
import qqbot
#写自动回复
#自动回复部分我们需要调用一个监听的方法
@qqbot.QQBotSlot
def onQQMessage(bot,contact,member,content):
    """
    :param bot:  qq对象
    :param contact: 发信人
    :param member: 发消息的对象，支队群组有作用
    :param content: 内容
    """
    if content == "-hello":
        bot.SendTo(contact,"你也好啊,/龇牙")
    elif "@ME" in content and "签到" in content:
        """
            当满足此条件就
            判断该成员是否已经签到过 调用数据库查看用户的信息 判断条件 签到时间
            进行签到
                签到时间 当前时间
                签到次数 +1
                签到积分 +2
            你已经签到多少天，积分多少
        """
        bot.SendTo(contact, "/菜刀 咋地了？")
    elif "@ME" in content and "兑换" in content:
        """
            返回资源列表
        """
        bot.SendTo(contact,"/菜刀 咋地了？")

if __name__ == "__main__":
    qqbot.RunBot()