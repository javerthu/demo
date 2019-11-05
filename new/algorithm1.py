s = eval(input('输入正整数n'))
n = 0
l = 0
def sa(s,n,l):
    m = []
    for i in range(l, s):
        n = n + i
        m.append(i)
        if n == s:
            m.append('成功')
            return m
            break
        elif n > s:
            break

if s%2 == 0: #判断奇偶加快运行效率
    a = int(s/3)
else:
    a = int(s/2)

for i in range(int(a)):
    l = l +1
    if sa(s, n, l):
        print(sa(s, n, l))
