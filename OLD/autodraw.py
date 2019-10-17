import turtle as t
t.title('自动绘轨')
t.setup(900,600,300,300)
t.pu()
t.bk(200)
t.pendown()
t.pensize(5)

datals=[]
f=open('E:/python/file/autodraw.txt',encoding='utf-8')
for line in f:
    line = line.replace('\n','')
    a = line.encode('utf-8').decode('utf-8-sig')#去除\ufeff str转list编码错误
    datals.append(list(map(eval,a.split(','))))#在python中,map() 生成的是迭代器不是list， 你可以在map前加上list，即list(map())
f.close()

for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][4])
    t.fd(datals[i][0])
    if datals[i][1]== True :
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
t.hideturtle()
