#BMI
import time
try:
    h,w=eval(input('身高m,体重kg:'))
    s=time.perf_counter()
    bmi=w/pow(h,2)
    print('BMI数值为:{:.2f}'.format(bmi))
    who,nat='',''
    if bmi<18.5:
        who,nat='偏瘦','偏瘦'
    elif 18.5<=bmi<24:
        who,nat='正常','正常'
    elif 24<=bmi<25:
        who,nat='正常','偏胖'
    elif 25<=bmi<28:
        who,nat='偏胖','偏胖'
    elif 28<=bmi<30:
        who,nat='偏胖','肥胖'
    else :
        who,nat='肥胖','肥胖'
    time.sleep(0.1)
    dur=time.perf_counter()-s
    print('BMI指标为:国际{},国内{}'.format(who,nat))
    print('{:.2f}s'.format(dur))
except:
    print('输入错误')
    
