a = ""
b=0
q=eval(input('输入:'))
if q>int(q):
    q=q+1
else:
    q=q
for i in range(int(q),10000):
    for num in range(2,i):
        if (i%num==0):
            break
    else:
        b = b+1
        if b>5:
            break
        a += "{},".format(i)
print(a[:-1])
