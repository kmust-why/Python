import random


print('这是一个猜数字的小游戏，游戏规则是系统给出一个0-9的数字，自己才输入一个，如果三次以内猜中，则赢，否则就输了。')
ls = []
s = random.randint(0,9)
#print('随机数：%d' %s)
for count in range(9):
        number = int(input('请输入0-9中的一个数字：\n'))
        ls.append(number)
        #print(ls)
        
        if count == 8:
                while s in ls:
                        s = random.randint(0,9)
                        #print('重新生成的随机数：%d' %s)
                print('你输了，正确答案是%d' %s)
        else:                
                print('你猜错了，还剩下%d次机会。' %(8-count))
                                
                
