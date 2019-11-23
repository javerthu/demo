'''
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
六种特殊情况
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

'''

#s 为输入的罗马字符串
def romanToInt(s):
    a = s.replace('CM','N').replace('CD','F').replace('XC','J')\
        .replace('XL','S').replace('IX','n').replace('IV','f') #将六种特殊情况用一个字定义的字母标识
    d = {}
    for i in a:
        d[i] = d.get(i,0) + 1 #字典没有i键则创建d[i]为1，有则i键的值加1，以此来计算各个标识符号出现多少次
    num = d.get('I',0)*1 + d.get('V',0)*5 + d.get('X',0)*10 + d.get('L',0)*50 + \
        d.get('C',0)*100 + d.get('D',0)*500 + d.get('M',0)*1000 + d.get('N',0)*900 + \
        d.get('F',0)*400 + d.get('J',0)*90 + d.get('S',0)*40 + d.get('n',0)*9 + \
        d.get('f',0)*4  #将各个标识符的数量乘以对应标识符的值然后相加则完成该算法题
    return num
s = input('输入罗马字符串:')
print(romanToInt(s))