def replace_repeated_chars(s, k):
    # 结果字符串初始化为空
    result = []
    # 创建一个集合，用于存储滑动窗口中的字符
    seen = set()

    # 遍历字符串中的每个字符及其索引
    for i, char in enumerate(s):
        # 如果字符在滑动窗口（集合）中，替换为'-'
        if char in seen:
            result.append('-')
        else:
            result.append(char)
            seen.add(char)

        # 如果滑动窗口的大小达到k，从集合中移除最早添加的字符
        if i >= k:
            seen.remove(s[i - k])

    # 将结果列表转换为字符串并返回
    return ''.join(result)


# 测试函数
input_str1 = "abcdefaxc"
k1 = 10
print(replace_repeated_chars(input_str1, k1))  # abcdef-x-

input_str2 = "abcdefaxcqwertba"
k2 = 10
print(replace_repeated_chars(input_str2, k2))  # abcdef-x-qw-rtb-