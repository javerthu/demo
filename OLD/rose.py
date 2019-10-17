import turtle as t
#曲线函数
def DCurve(n,r,d=1):
    for i in range(n):
        t.left(d)
        t.circle(r,abs(d))

s=0.2
t.setup(450*5*s,750*5*s)
t.pencolor('black')
t.fillcolor('red')
t.speed(1000)
t.penup()
t.goto(0,900*s)
t.pendown()

#花朵绘制
t.begin_fill()
t.circle(200*s,30)
DCurve(60,50*s)
t.circle(200*s,30)
DCurve(4,100*s)
t.circle(200*s,50)
DCurve(50,50*s)
t.circle(350*s,65)
DCurve(40,70*s)
t.circle(150*s,50)
DCurve(20,50*s,-1)
t.circle(400*s,60)
DCurve(18,50*s)
t.fd(250*s)
t.right(150)
t.circle(-500*s,15)
t.left(140)
t.circle(550*s,110)
t.left(27)
t.circle(650*s,100)
t.left(130)
t.circle(-300*s,20)
t.right(123)
t.circle(220*s,57)
t.end_fill()

#花枝绘制
t.left(120)
t.fd(280*s)
t.left(115)
t.circle(300*s,33)
t.left(180)
t.circle(-300*s,33)
DCurve(70,225*s,-1)
t.circle(350*s,104)
t.left(90)
t.circle(200*s,105)
t.circle(-500*s,63)
t.penup()
t.goto(170*s,-30*s)
t.pendown()
t.left(160)
DCurve(20,2500*s)
DCurve(220,250*s,-1)

#绿叶绘制
t.fillcolor('green')
t.penup()
t.goto(670*s,-180*s)
t.pendown()
t.right(140)
t.begin_fill()
t.circle(300*s,120)
t.left(60)
t.circle(300*s,120)
t.end_fill()
t.penup()
t.goto(180*s,-550*s)
t.pendown()
t.right(85)
t.circle(600*s,40)


#另一个绿叶绘制
t.penup()
t.goto(-150*s,-1000*s)
t.pendown()
t.right(120)
t.begin_fill()
t.circle(300*s,115)
t.left(75)
t.circle(300*s,100)
t.end_fill()
t.penup()
t.goto(430*s,-1070*s)
t.pendown()
t.right(30)
t.circle(-600*s,35)
t.hideturtle
t.done()


















