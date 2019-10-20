s = 'asdqweauhwiuq'

def gen(s, n):
    for i in range(0, n*3, 3):
        yield s[i], s[i+1], s[i+2]
for i in gen(s, 2):
    print(i)