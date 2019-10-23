s = 'asdqweauhwiuq'

def gen(s, n):
    for i in range(0, n*3, 3):
        yield s[i], s[i+1], s[i+2]
for i in gen(s, 2):
    print(i)
#试了一下字典输入
s = [[1,2,3],[4,5,66],[7,8,9]]
N = ['name', 'addr', 'age']
# for i in s:
#     for i in range(len(i)):
#     N[i] = s[i]
#     print
d = {}
for i in s:
    for n in range(len(i)):
        d[N[n]] = i[n]
    print(d)