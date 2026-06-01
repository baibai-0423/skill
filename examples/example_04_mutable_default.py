"""
T04: 可变默认参数陷阱
预期问题: 列表默认参数会累积，多次调用共享同一列表
"""


def append_item(item, lst=[]):
    lst.append(item)
    return lst


# 测试用例：连续调用
print(append_item(1))  # 期望: [1]，实际: [1]
print(append_item(2))  # 期望: [2]，实际: [1, 2] ← 陷阱！
