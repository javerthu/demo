#jindutiao
import time
scale=10
print("------执行开始------")
start=time.perf_counter()
for i in range(scale+1):
    a="*"*i
    b="."*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    print('\r{:.^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end='')
    time.sleep(0.1)
input('回车退出')
