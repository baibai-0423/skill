# 测试用例定义

## 测试策略
- 正常输入：5个（覆盖不同问题类型）
- 边界输入：1个（缺少代码）
- 对抗输入：1个（非Python代码）
- 完全正确：1个（验证无问题时的输出）

---

## T01: 常见逻辑错误 — 找最大值初始化

**文件**: `examples/example_01_max_negative.py`

**代码**:
```python
def find_max(lst):
    max = 0
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max

nums = [-5, -2, -10]
print(find_max(nums))
```

**预期发现**:
| 问题 | 严重度 | 位置 | 说明 |
|:---|:---:|:---:|:---|
| max=0初始化错误 | 🔴 Critical | 第2行 | 全负数列表返回0 |
| range(len())遍历 | 🟡 Warning | 第3行 | 可改为直接遍历 |
| max作变量名 | 🟢 Suggestion | 第2行 | 遮蔽内置函数 |

**预期输出特征**:
- 指出 `nums = [-5, -2, -10]` 会输出0而非-2
- 提供修复后的完整代码

---

## T02: 效率问题 — 嵌套循环找重复

**文件**: `examples/example_02_nested_loop.py`

**代码**:
```python
def find_duplicates(data):
    duplicates = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j] and data[i] not in duplicates:
                duplicates.append(data[i])
    return duplicates

nums = [1, 2, 3, 2, 4, 3, 5]
print(find_duplicates(nums))
```

**预期发现**:
| 问题 | 严重度 | 位置 | 说明 |
|:---|:---:|:---:|:---|
| O(n²)嵌套循环 | 🟡 Warning | 第4-5行 | 可用set优化至O(n) |
| range(len()) | 🟢 Suggestion | 第4行 | 可改为直接遍历 |
| 变量命名 | 🟢 Suggestion | 第1行 | find_duplicates可优化 |

**预期输出特征**:
- 分析时间复杂度 O(n²)
- 建议使用 `set` 或 `collections.Counter`
- 提供O(n)优化方案

---

## T03: 风格问题 — 命名与注释

**文件**: `examples/example_03_style_issues.py`

**代码**:
```python
def f(a, b):
    c = a + b
    d = c * 2
    return d

x = 5
y = 3
z = f(x, y)
print(z)
```

**预期发现**:
| 问题 | 严重度 | 位置 | 说明 |
|:---|:---:|:---:|:---|
| 函数名无意义 | 🟢 Suggestion | 第1行 | f → 如add_and_double |
| 变量名无意义 | 🟢 Suggestion | 第1-2行 | a,b,c,d → 有意义名称 |
| 缺少注释 | 🟢 Suggestion | 全部 | 添加功能说明 |
| 缺少文档字符串 | 🟢 Suggestion | 第1行 | 添加docstring |

**预期输出特征**:
- 无Critical和Warning
- 全是Suggestion级别
- 提供重构后的规范代码

---

## T04: 潜在Bug — 可变默认参数

**文件**: `examples/example_04_mutable_default.py`

**代码**:
```python
def append_item(item, lst=[]):
    lst.append(item)
    return lst

print(append_item(1))
print(append_item(2))
```

**预期发现**:
| 问题 | 严重度 | 位置 | 说明 |
|:---|:---:|:---:|:---|
| 可变默认参数 | 🟡 Warning | 第1行 | 列表会累积 |
| 缺少类型提示 | 🟢 Suggestion | 第1行 | 添加类型注解 |

**预期输出特征**:
- 指出第二次调用会返回 `[1, 2]` 而非 `[2]`
- 解释Python默认参数在定义时求值的机制
- 提供 `lst=None` 的修复方案

---

## T05: 完全正确的代码 — 验证无问题输出

**文件**: `examples/example_05_complete_correct.py`

**代码**:
```python
def calculate_average(numbers):
    """计算列表平均值"""
    if not numbers:
        return 0.0

    total = sum(numbers)
    count = len(numbers)
    return total / count

data = [10, 20, 30, 40, 50]
result = calculate_average(data)
print(f"平均值: {result}")
```

**预期发现**:
- 无Critical
- 无Warning
- 可能有1-2个Suggestion（如类型提示、异常处理）

**预期输出特征**:
- 以"🎉 代码质量良好"开头
- 给出复杂度分析
- 提供可选的进一步优化建议

---

## T06: 边界测试 — 缺少代码输入

**输入**: `"帮我看看这段代码"`

**预期输出**:
```
请粘贴您想审查的Python代码，我会从语法、逻辑、风格、效率等维度为您分析。
```

---

## T07: 边界测试 — 非Python代码

**输入**: C++代码

**预期输出**:
```
我目前只支持Python代码审查。如需审查C++代码，建议使用cppcheck或clang-tidy。
```
