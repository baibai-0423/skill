"""
T02: 嵌套循环效率问题
预期问题: O(n²) 时间复杂度，可用 set 优化至 O(n)
"""


def find_duplicates(data):
    duplicates = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j] and data[i] not in duplicates:
                duplicates.append(data[i])
    return duplicates


# 测试用例
nums = [1, 2, 3, 2, 4, 3, 5]
print(find_duplicates(nums))  # 输出: [2, 3]
