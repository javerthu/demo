import requests
import re
import bs4
from bs4 import BeautifulSoup
demo ='''
<tbody class="hidden_zhpm" style="text-align:center;">

<tr class="alt"><td>1</td>
<td><div align="left">清华大学</div></td>
<td>北京市</td><td>95.9</td><td class="hidden-xs need-hidden indicator5">100.0</td><td class="hidden-xs need-hidden indicator6"  style="display:none;">97.90%</td><td class="hidden-xs need-hidden indicator7"  style="display:none;">37342</td><td class="hidden-xs need-hidden indicator8"  style="display:none;">1.298</td><td class="hidden-xs need-hidden indicator9"  style="display:none;">1177</td><td class="hidden-xs need-hidden indicator10"  style="display:none;">109</td><td class="hidden-xs need-hidden indicator11"  style="display:none;">1137711</td><td class="hidden-xs need-hidden indicator12"  style="display:none;">1187</td><td class="hidden-xs need-hidden indicator13"  style="display:none;">593522</td></tr>
<tr><td>310</td>
<td><div align="left">德州学院</div></td>
<td>山东省</td><td>21.5</td><td class="hidden-xs need-hidden indicator5">15.3</td><td class="hidden-xs need-hidden indicator6" style="display:none;">87.86%</td><td class="hidden-xs need-hidden indicator7" style="display:none;">614</td><td class="hidden-xs need-hidden indicator8" style="display:none;">0.502</td><td class="hidden-xs need-hidden indicator9" style="display:none;">3</td><td class="hidden-xs need-hidden indicator10" style="display:none;"></td><td class="hidden-xs need-hidden indicator11" style="display:none;">966</td><td class="hidden-xs need-hidden indicator12" style="display:none;">2</td><td class="hidden-xs need-hidden indicator13" style="display:none;">0</td></tr>
</tbody>

'''
inf = []
soup = BeautifulSoup(demo,'html.parser')
for i in soup.tbody.children:
    if isinstance(i,bs4.element.Tag):
        s = i('td')
        inf.append([s[0].string,s[1].string,s[2].string])
tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'
print(tplt.format('排名','学习名称','省份',chr(12288)))
for i in inf:
    print(tplt.format(i[0],i[1],i[2],chr(12288)))

f=open('test.txt','w+')
f.write(str(soup))
f.seek(0)
print(f.readline())
f.close()

