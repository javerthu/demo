#
week="星期一 星期二 星期三 星期四 星期五 星期六 星期天 "
ID=input("输入:")
for i in ID:
    pos=(eval(i)-1)*4
    print(week[pos:pos+4],end="")
