#生成自我评价图
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
radar_labels = np.array(['学习能力','开源热爱',\
                         'Geek','适应能力',\
                         '沟通能力','创新能力'])
data = np.array([[0.85,],
                 [0.95,],
                 [0.80,],
                 [0.80,],
                 [0.80,],
                 [0.75,]])
data_labels = ('胡钊华',)
angles = np.linspace(0,2*np.pi,6,endpoint=False)
data = np.concatenate((data,[data[0]]))
angles = np.concatenate((angles,[angles[0]]))
fig = plt.figure(facecolor='white')
plt.subplot(111,polar=True)
plt.plot(angles,data,'o-',linewidth=1,alpha=0.2)
plt.fill(angles,data,alpha=0.25)
plt.thetagrids(angles*180/np.pi,radar_labels)
plt.figtext(0.52,0.95,'自我评价',ha='center',size=20)
legend = plt.legend(data_labels,loc=(0.94,0.80),labelspacing=0.1)
plt.setp(legend.get_texts(),fontsize='large')
plt.grid(True)
plt.savefig('E:/python/file/holland_radar.jpg')
plt.show()