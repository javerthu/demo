import turtle as t
import time
def drawgap():
    t.pu()
    t.fd(5)
def drawline(draw):
    drawgap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawgap()
    t.right(90)
def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    t.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    t.right(180)
    t.penup() #为下个数码管开始标识位置
    t.fd(20)
def drawdata(data):#data为日期，格式为’%Y-%m=%d+'
    t.pencolor('red')
    for i in data:
        if i == '-':
            t.write('年',font=('Arial',18,'normal'))
            t.pencolor('green')
            t.fd(40)
        elif i == '=':
            t.write('月',font=('Arial',18,'normal'))
            t.pencolor('blue')
            t.fd(40)
        elif i == '+':
            t.write('日',font=('Arial',18,'normal'))
        else:
            drawdigit(eval(i))
def main():
    t.hideturtle()
    t.speed(1000)
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(2)
    drawdata(time.strftime('%Y-%m=%d+',time.gmtime()))
    t.done()
main()
