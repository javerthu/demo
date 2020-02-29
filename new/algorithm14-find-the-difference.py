'''
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例:
输入：
s = "abcd"
t = "abcde"
输出：e
解释：
'e' 是那个被添加的字母。

'''
s = input('s(str):')
t = input('t(str):')
ds = {}
dt = {}
for i in s:
    ds[i] = ds.get(i, 0) + 1
for i in t:
    dt[i] = dt.get(i, 0) + 1
for i in dt:
    if dt[i] != ds.get(i, 0):
        print(i)




#letcode模板
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         ds = {}
#         dt = {}
#         for i in s:
#             ds[i] = ds.get(i, 0) + 1
#         for i in t:
#             dt[i] = dt.get(i, 0) + 1
#         for i in dt:
#             if dt[i] != ds.get(i, 0):
#                 return i