import random


print('这是一个猜数字的小游戏，游戏规则是系统给出一个0-9的数字，自己才输入一个，如果三次以内猜中，则赢，否则就输了。')
s = random.randint(0,9)
for count in range(0,3):
        number = int(input('请输入0-9中的一个数字：\n'))
        if number == s:
                print('恭喜你猜对了')
                break #跳出循环
        else:
                if count == 2:
                        print('你输了，正确答案是%d' %s)
                else:
                        if number > s:
                                print('你猜错了，你猜的数字大了，还剩下%d次机会。' %(2-count))
                        else:
                                print('你猜错了，你猜的数字小了，还剩下%d次机会。' %(2-count))
                
