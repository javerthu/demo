'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,  2**31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

链接：https://leetcode-cn.com/problems/reverse-integer
'''
x = input('输入一个整数:')
if str(x)[0] == '-': #判断是否是正数
    reverse_x = '-' + str(x)[1::][::-1]
else:
    reverse_x = str(x)[::-1]
if (-2) ** 31 < int(reverse_x) < (2 ** 31) - 1: #判断反转后的数是否超出范围了
    print(int(reverse_x))
else:
    print(int(0))

#letcode模板
# class Solution:
#     def reverse(self, x: int) -> int:
#         if str(x)[0] == '-':
#             reverse_x = '-' + str(x)[1::][::-1]
#         else:
#             reverse_x = str(x)[::-1]
#         if (-2)**31 < int(reverse_x) < (2**31)-1:
#             return(int(reverse_x))
#         else:
#             return int(0)