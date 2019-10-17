import random
def getinputs():
    a=eval(input('A选手能力(0-1):'))
    b=eval(input('B选手能力(0-1):'))
    n=eval(input('模拟多少次比赛:'))
    return a,b,n

def printSummary(aw,bw):
    n=aw+bw
    print('共模拟比赛{}场'.format(n))
    print('A选手获胜{}场,胜率{:.4f}'.format(aw,aw/n))
    print('B选手获胜{}场,胜率{:.4f}'.format(bw,bw/n))

def gameOver(a,b):
    return a==15 or b==15

def simgame(proA,proB):
    sA = 0
    sB = 0
    serving = 'A'
    while not gameOver(sA,sB):
        if serving == 'A':
            if random.random() < proA:
                sA += 1
            else:
                serving = 'B'
        else :
            if random.random() < proB:
                sB += 1
            else:
                serving = 'A'
    return sA,sB

def simNgame(a,b,n):
    aw=0
    bw=0
    for i in range(n):
        sA,sB=simgame(a,b)
        if sA > sB:
            aw = aw+1
        else:
            bw = bw+1
    return aw,bw

def main():
    a,b,n=getinputs()
    for i in (a,b):
        if i>1:
            a=y     
    aw,bw=simNgame(a,b,n)
    printSummary(aw,bw)
try:
    main()
except:
    print('输入错误,不会看提示吗蠢逼')
input("回车退出 ")
