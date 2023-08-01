import os
import random

import defines


def count_zeros(file_path, num_lines):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 去除空行和换行符
    lines = [line.strip() for line in lines if line.strip()]

    # 打乱数据
    random.shuffle(lines)

    # 获取最后num_lines行数据并计算0的数量
    last_lines = lines[-num_lines:]
    zeros_count = last_lines.count('0')

    return zeros_count


def calculate_average_zeros(file_path, num_lines, iterations):
    total_zeros = 0

    for _ in range(iterations):
        zeros_count = count_zeros(file_path, num_lines)
        total_zeros += zeros_count

    average_zeros = total_zeros / iterations

    return average_zeros


rootPath = defines.TM_PATH
for i, name in enumerate(defines.TM):
    print(i + 1, name.value)
    path = os.path.join(rootPath, name.value)
    file_path = os.path.join(path, 'label.txt')  # 数据文件路径
    iterations = 100  # 迭代次数

    # 计算最后100条数据中0的数量的平均值
    num_lines = 100
    average_zeros_100 = calculate_average_zeros(file_path, num_lines, iterations)
    print(f"最后{num_lines}条数据中的平均值：{average_zeros_100}")

    # 计算最后10条数据中0的数量的平均值
    num_lines = 10
    average_zeros_10 = calculate_average_zeros(file_path, num_lines, iterations)
    print(f"最后{num_lines}条数据中的平均值：{average_zeros_10}")

    # 计算最后1条数据中0的数量的平均值
    num_lines = 1
    average_zeros_1 = calculate_average_zeros(file_path, num_lines, iterations)
    print(f"最后{num_lines}条数据中的平均值：{average_zeros_1}")
