'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
LETCODE题目自解
对于数列很大的nums需要很长的运行时间，也是硬着头皮完成算法的典例。。。
'''

nums = eval(input('输入列表:'))
target = eval(input('输入查询数:'))
lenth = len(nums)
try:
    for m in range(0, lenth):
        n = m #从nums列表的第一个元素开始为基本值，循环列表后的元素与之相加，没有则将基本值改为nums列表的第二元素
        c = n
        for i in nums[(n+1)::]: #nums[(n+1)::]表示从初始值后的相加，因为之前的都相加过了，没有跳出循环表示没有正确的值
            c = c + 1 #表示循环到i的下标号，作为输出打印,i也就是相加值
            start = nums[n] #基本值,n则是基本值的下标
            if start + i == target: #判断目标数字是否等于 基本值+相加值
                print([n, c])
                break
            else:
                if n == (lenth-2) and c == (lenth-1): #即循环到nums列表最后两个都无匹配值，则表示没有
                    print('木有找到')
                else:
                    continue
except:
    print('哦哦出问题了')
#letcode模板解决
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         lenth = len(nums)
#         try:
#             for m in range(0, lenth):
#                 n = m
#                 c = n
#                 for i in nums[(n+1)::]:
#                     c = c + 1
#                     start = nums[n]
#                     if start + i == target:
#                         return [n, c]
#                         break
#                     else:
#                         continue
#         except:
#             return '木有找到'