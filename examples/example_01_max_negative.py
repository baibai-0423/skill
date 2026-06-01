"""
T01: 找最大值初始化错误
预期问题: max=0 在全负数列表时返回错误结果
"""


def find_max(lst):
    max = 0
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max


# 测试用例：全负数列表
nums = [-5, -2, -10]
print(find_max(nums))  # 错误输出: 0，期望: -2
