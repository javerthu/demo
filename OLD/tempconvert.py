#tempconvert.py

def tempstr(tem):
    if tem[-1] in ['F','f']:
        C = (eval(tem[0:-1]) - 32)/1.8
        print("转换后的温度是{:.2f}C".format(C))
    elif tem[-1] in ['C','c']:
        F = 1.8*eval(tem[0:-1]) + 32
        print("转换后的温度是{:.2f}F".format(F))
    else:
        print("输入格式错误")

tem=input("输入带有符号的温度值")
tempstr(tem)
