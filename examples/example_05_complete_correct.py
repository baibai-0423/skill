"""
T05: 完全正确的代码
预期: 无 Critical/Warning，可能有少量 Suggestion
"""


def calculate_average(numbers):
    """计算列表平均值

    Args:
        numbers: 数字列表

    Returns:
        平均值，空列表返回0.0
    """
    if not numbers:
        return 0.0

    total = sum(numbers)
    count = len(numbers)
    return total / count


# 测试用例
data = [10, 20, 30, 40, 50]
result = calculate_average(data)
print(f"平均值: {result}")  # 输出: 平均值: 30.0
