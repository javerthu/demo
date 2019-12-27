'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
链接：https://leetcode-cn.com/problems/valid-palindrome
'''
import re
s = input('需要验证的字符串:')
a = re.sub(r'[^A-Za-z\d]', '', s).lower() #使用正则表达式将字符串的非字母和数字去除

print(len(a))
b = len(a) // 2 #做一个切片的标志位置，注意不能用len(a)/2会报转义的错误
if len(a) % 2 == 0: #对字符串长度做判断，因为奇偶影响半段的位置
    print(a[0:b]) #前半段的字符
    print(a[b:len(a)]) #后半段字符
    if a[0:b] == a[b:len(a)][::-1]: #比较是否相等
        print('是回文串')
    else:
        print('不是回文串')
else:
    print(a[0:b])
    print(a[b+1:len(a)][::-1])
    if a[0:b] == a[b+1:len(a)][::-1]:
        print('是回文串')
    else:
        print('不是回文串')

#letcode模板
# import re
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         a = re.sub(r'[^A-Za-z\d]', '', s).lower()
#         b = len(a) // 2
#         if len(a) % 2 == 0:
#             if a[0:b] == a[b:len(a)][::-1]:
#                 return True
#             else:
#                 return False
#         else:
#             if a[0:b] == a[b+1:len(a)][::-1]:
#                 return True
#             else:
#                 return False
