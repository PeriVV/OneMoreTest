import numpy as np
import random
import os
import defines
train_num = 1000000


def calculate_Coverage(dataSet):
    # dataSet: input,output,label,line coverage
    random.shuffle(dataSet)
    size = len(dataSet)
    total_line = set()
    for i in range(0, size):
        line_info = dataSet[i][3]
        line_info = line_info.strip(' ')
        lst = line_info.split(' ')
        num = len(lst)
        for j in range(0, num):
            total_line.add(float(lst[j]))
        dataSet[i].append(num)
    # Data: input,output,label,line coverage,flag
    max_num = 10000
    idx = 0
    while True:
        flag = 0
        dataSet = sorted(dataSet, key=lambda x: -x[4])
        nums = dataSet[idx][3].strip(' ').split(' ')
        for num in nums:
            if float(num) in total_line:
                total_line.remove(float(num))
        dataSet[idx][4] = max_num
        max_num -= 1
        idx += 1
        for i in range(idx, len(dataSet)):
            lst = dataSet[i][3].strip(' ').split(' ')
            dataSet[i][4] = 0
            for num in lst:
                if (float(num) in total_line):
                    dataSet[i][4] += 1
                    flag = 1
        if not flag:
            break
    res = dataSet[0:idx]
    rest = dataSet[idx:]
    random.shuffle(rest)
    res += rest
    return res


def load_file(path):
    input_file = os.path.join(path, 'before_data.txt')
    output_file = os.path.join(path, 'after_data.txt')
    label_file = os.path.join(path, 'label.txt')
    line = os.path.join(path, 'line_coverage.txt')
    coverage_in = os.path.join(path, 'coverage_input.txt')
    coverage_out = os.path.join(path, 'coverage_output.txt')
    coverage_label = os.path.join(path, 'coverage_label.txt')
    coverage_line = os.path.join(path, 'coverage_line.txt')
    # read original file
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'r')
    label_f = open(label_file, 'r')
    coverage_f = open(line, 'r')
    in_line = in_f.readline().strip('\n')
    out_line = out_f.readline().strip('\n')
    label_line = label_f.readline().strip('\n')
    line_line = coverage_f.readline().strip('\n')
    dataSet = []
    Data = []
    while in_line and out_line and label_file and line_line:
        dataSet.append([in_line, out_line, label_line, line_line])
        in_line = in_f.readline().strip('\n')
        out_line = out_f.readline().strip('\n')
        label_line = label_f.readline().strip('\n')
        line_line = coverage_f.readline().strip('\n')
    in_f.close()
    out_f.close()
    label_f.close()
    coverage_f.close()
    dataSet = dataSet[train_num:]
    # according to coverage, sort the dataSet
    Data = calculate_Coverage(dataSet)
    # write coverage file
    Data = np.array(Data)
    in_f = open(coverage_in, 'w')
    out_f = open(coverage_out, 'w')
    label_f = open(coverage_label, 'w')
    coverage_f = open(coverage_line, 'w')
    for i in range(0, len(Data)):
        in_f.write(Data[i, 0] + '\n')
        out_f.write(Data[i, 1] + '\n')
        label_f.write(Data[i, 2] + '\n')
        coverage_f.write(Data[i, 3] + '\n')
    in_f.close()
    out_f.close()
    label_f.close()
    coverage_f.close()
    return ''


if __name__ == '__main__':
    path = os.path.join(defines.TM_PATH, defines.TM.TM16_path.value)
    load_file(path)
