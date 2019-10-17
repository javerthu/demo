def num():
    nums=[]
    inumstr=input('输入数字(回车退出)：')
    while inumstr != '':
        nums.append(eval(inumstr))
        inumstr=input('输入数字(回车退出)：')
    return nums


def mean(numbers): #算平均值
    s=0.0
    for num in numbers:
        s = s+num
    return s/len(numbers)

def dev(numbers,mean):#方差计算
    sdev=0.0
    for num in numbers:
        sdev = sdev+(num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)

def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 ==0:
        med = (numbers[size//2-1]+numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

n=num()
m=mean(n)
print('平均值:{},方差:{:.2f},中位数:{}.'.format(m,dev(n,m),median(n)))

