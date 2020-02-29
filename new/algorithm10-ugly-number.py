'''
编写一个程序判断给定的数是否为丑数。
丑数就是只包含质因数 2, 3, 5 的正整数。
示例 1:
输入: 6
输出: true
解释: 6 = 2 × 3

示例 2:
输入: 8
输出: true
解释: 8 = 2 × 2 × 2

示例 3:
输入: 14
输出: false
解释: 14 不是丑数，因为它包含了另外一个质因数 7。
说明：

1是丑数。
输入不会超过 32 位有符号整数的范围: [−231,  231 − 1]。
'''
num = int(input('输入整数:'))
if num <= 0:
    print(False)

while num > 2:
    if num / 5 > int(num / 5) and num / 3 > int(num / 3) and num / 2 > int(num / 2):
        print(False)
    else:
        if num / 5 == int(num / 5):
            num = num / 5
        elif num / 3 == int(num / 3):
            num = num / 3
        else:
            num = num / 2
if num <= 2:
    print(True)





#letcode模板
# class Solution:
#     def isUgly(self, num: int) -> bool:
#         if num<=0:
#             return False
#
#         while num > 2:
#             if num / 5 > int(num / 5) and num / 3 > int(num / 3) and num / 2 > int(num / 2):
#                 return False
#             else:
#                 if num / 5 == int(num / 5):
#                     num = num / 5
#                 elif num / 3 == int(num / 3):
#                     num = num / 3
#                 else:
#                     num = num / 2
#         if num <= 2:
#             return True