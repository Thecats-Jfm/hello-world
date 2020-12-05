import datetime
c=input('请输入您的姓名：')
print()
print('年轻的勇者'+str(c)+',欢迎来到失落的密境，挑战之塔。挑战之塔旨在考察试炼者\
对东方遥远国度亚夏的风物和对同样来自东方的神奇秘术，拼音的掌握，试炼将随机给出亚夏\
任意一个省，直辖市，自治区或特殊行政区的名字，而试炼者需要给出该城市的拼音\
并用数字表明声调，如给出‘上海’，则标准答案为‘shang4 hai3’。挑战之塔层数无限\
每一层有三重试炼，只有完成三道试炼才能进入下一层，如果如果准备好开始试炼，请按y键开始。')
print()
d=input('开始试炼请按Y键，退出试炼请按其他键：')
if d.lower()=='y':
    while True:
        e=0
        f=0
        if e==0:
            mytime1=datetime.datetime.now()
        if e==2:
            mytime2=datetime.datetime.now()
        delay=mytime2-mytime1
        g=delay.seconds+delay.microseconds/1000000
        英雄榜=[]
        print()
        b=str(b)
        if e<3:
            h=input('试炼开始，这是第一道题'+str(b)+',请作答：')
            if str(b) == str('内蒙古') or str(b) == str('西藏') or str(b) ==str( '重庆') :
                if str(h)==m[str(b)]:
                    print('恭喜你！答对了！即将开始下一道试炼！')
                    print()
                    e=e+1
                    f=f+1
                else:
                    print('真遗憾！试炼没有想象的那么简单,你本应输入'+str(b)+',下一道试炼请仔细思考，审慎作答。')
                    e=e+1
            else:
                if str(h) == str(p.get_pinyin(str(b), '', tone_marks='numbers')):
                    print('恭喜你！答对了！即将开始下一道试炼！')
                    e=e+1
                    f=f+1
                else:
                    print('真遗憾！试炼没有想象的那么简单,你本应输入'+str(b)+',下一道试炼请仔细思考，审慎作答。')
                    e=e+1
        if e==3:
            print('恭喜你，闯过了三关的年轻人，你只用了'+str(g)+'s便以答对'+str(f)+'道题的好成绩通过试炼，针不戳！')
            print()
            if f==3:
                print('年轻人，你凭借真正的实力过关斩将，来到了这里！属于你的史诗已被录入挑战之塔英雄榜！')
                英雄榜.append(g)
                英雄榜_arrange = sorted(kkk)
                英雄榜_arrange.insert(0,'英雄榜榜首:'+str(c)+'取得了最好成绩,用时')
                if g==min(英雄榜):
                    print('恭喜'+str(c)+'醉斩千山，弹剑作歌，夺得英雄榜榜首！')
            else:
                print('年轻人，你的潜力远不止于此，须得好生练习。')
            print()
            for time in kkk:
                print(time,sep='\n')
                break
            print()
            i=input('年轻人，你已经通过了这一层的挑战之塔，如果你想要进入下一层的话，请按y；如果你想要退出，请按其他键:')
            if i.lower()=='y':
                print()
                print('年轻人！准备好了吗？欢迎进入下一层试炼！')
                continue
            else:
                print()
                print('年轻人，相信你在挑战之塔中收获不少，可暂时退出，好生领悟修炼。')
                break
else:
    print()
    print('年轻人，莫灰心！吾辈须养一往无前之锐气，汝尚需修炼心境！')
print()
print('年轻人，挑战之塔永远矗立在阴影之地，我们来日再回！')
