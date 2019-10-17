#二半法找数精确度太高了吧
def b(x):
    b = 1
    for i in range(365):
        if i % 7 in [0,6]:
            b = b*(1-0.01)
        else:
            b = b*(1+x)
    return b
a=1*(1+0.01)**365

x = 0.01
y = 0.1
for i in range(1000):
    z = (x+y)/2
    if b(z) > a :
        if b(( z )-0.00000000000001) < a:
            print('{}'.format(z))
            break
        else:
            y = z
    else:
        x = z
