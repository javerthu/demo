'''
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指由字母组成，但不包含任何空格的字符串。
链接：https://leetcode-cn.com/problems/length-of-last-word
example:
    输入: "Hello World"
    输出: 5
'''
s = input('输入一个要测试的字符串:')
a = s.split(' ')#将要测试的字符串以空格分隔为一个列表
n = 0 #计数初值
if s:
    if a[-1]: #简单判断如果分隔出来列表最后一位有字符，则最后一个单词就是他
        print(len(a[-1]))
    else:
        for i in range(len(a)): #从最后依次循环判断是否存在有不为空
            n = n + 1 #判断下标
            if a[-n]: #如果有，则就是我们要找的最后一个单词
                print(len(a[-n]))
                break
            else:
                if n >= len(a):  #如果全部判断完都没找到不为空，则表示该字符串没单词（全是空格）
                     print(int(0))
else:
    print(int(0))


#letcode模板解决
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         a = s.split(' ')
#         n = 0
#         if s:
#             if a[-1]:
#                 return len(a[-1])
#             else:
#                 for i in range(len(a)):
#                     n = n + 1
#                     if a[-n]:
#                         return len(a[-n])
#                         break
#                     else:
#                         if n >= len(a):
#                             return int(0)
#         else:
#             return int(0)