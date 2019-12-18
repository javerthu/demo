'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

链接：https://leetcode-cn.com/problems/palindrome-number
'''

x = input('输入一个整数:')
s = str(x)[::-1]
if s == str(x):
    print('是回文')
else:
    print('不是回文')

#letcode模板
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s = str(x)[::-1]
#         if s == str(x):
#             return True
#         else:
#             return False