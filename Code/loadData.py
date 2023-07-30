from datetime import datetime

import numpy as np


def embeding(data, embed_size):
    result = []
    for X in data:
        tmp = np.array([np.concatenate([x, [0] * (embed_size - len(x))]) if len(x) < embed_size else x for x in X])
        result.append(tmp)
    return result


def normalization_array(data):
    max_num = -1e10
    min_num = 1e10

    for line in data:
        max_num = max(max_num, max(line))
        min_num = min(min_num, min(line))
    # print(max_num,min_num)
    out = []
    for line in data:
        epsilon = 1e-8  # 非零的很小数
        temp = [(x - min_num) / (max_num - min_num + epsilon) for x in line]
        out.append(temp)
    return out, max_num, min_num


def normalization_seq(data):
    max_num = -1e10
    min_num = 1e10

    for line in data:
        for word in line:
            max_num = max(max_num, max(word))
            min_num = min(min_num, min(word))
    words = []
    out = []
    for line in data:
        words = []
        for word in line:
            temp = [(x - min_num) / (max_num - min_num) for x in word]
            words.append(temp)
        out.append(words)
    return out


def padding_array(X, max_len, padding=0):
    return np.array([np.concatenate([x, [padding] * (max_len - len(x))]) if len(x) < max_len else x for x in X])


def padding_sequence(X, max_len, embed_size, padding=0):
    return np.array(
        [np.concatenate([x, [[padding] * embed_size] * (max_len - len(x))]) if len(x) < max_len else x for x in X])


def return_before(dataSet, max_num, min_num):
    out = []
    out = np.round(dataSet * (max_num - min_num) + min_num)
    '''for line in dataSet:
        temp = [round(x * (max_num - min_num)) + min_num for x in line]
        out.append(temp)'''
    return out


def load_array(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            words = line.split()
            data = [float(x) if x != 'NaN' else np.nan if x != 'Infinity' else np.inf for x in words]
            dataSet.append(data)
            line = f.readline()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], -1)
    return dataSet, seq_len, Max, Min


def load_array_split(filename, spliter):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            words = line.strip().split(spliter)
            data = [float(x) if len(x) > 0 else 0 for x in words]

            dataSet.append(data)
            line = f.readline()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], -1)
    return dataSet, seq_len, Max, Min


def load_data(filename):
    dataSet = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line != "":
                if line == "null":
                    dataSet.append([0])  # 将"null"值替换为0，可以根据需要进行修改
                else:
                    try:
                        dataSet.append([int(line)])
                    except ValueError:
                        ascii_val = [ord(char) for char in line]
                        dataSet.append(ascii_val)
        # 归一化
        dataSet, max_num, min_num = normalization_array(dataSet)

        # 填充
        max_len = max(len(x) for x in dataSet)  # 获取最大长度
        dataSet = padding_sequence(dataSet, max_len, embed_size=1)

        # 构建返回格式
        seq_len = [len(x) for x in dataSet]
        dataSet = np.array(dataSet)
        Max = np.array([max_num])  # 最大值，以数组形式存储
        Min = np.array([min_num])  # 最小值，以数组形式存储

        return dataSet, seq_len, Max, Min


def load_sequence(filename):
    dataSet = []

    with open(filename, 'r') as f:
        line = f.readline().strip()
        while line:
            data = [ord(x) for x in list(line)]
            dataSet.append(data)
            line = f.readline().strip()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)

    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], max_len)

    return dataSet, seq_len, Max, Min


def load_sequence_split(filename, spliter):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline().strip()
        lst = line.split(spliter)
        line = ' '.join(lst)
        while line:
            data = [ord(x) for x in list(line)]
            dataSet.append(data)
            line = f.readline().strip()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)

    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], max_len)
    return dataSet, seq_len, Max, Min


def load_label(filename):
    labelSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            arr = line.split()
            label = [int(x) for x in arr]
            labelSet.append(label)
            line = f.readline()
    labelSet = np.array(labelSet)
    labelSet = labelSet.reshape(labelSet.shape[0], 1)
    return labelSet


def normalization_dimention(dataSet):
    maxs = np.max(dataSet, axis=0)
    mins = np.min(dataSet, axis=0)
    out = []
    for line in dataSet:
        temp = []
        for j in range(len(line)):
            if maxs[j] == mins[j]:
                num = (line[j] - mins[j]) / 1
            else:
                num = (line[j] - mins[j]) / (maxs[j] - mins[j])
            temp.append(num)
        out.append(temp)
    return out, maxs, mins


def load_before_time14(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            data = []
            words = line.split('#')
            data.append(int(words[0]))
            nums = words[1].split('-')
            for x in nums:
                if x != '':
                    data.append(int(x))
            dataSet.append(data)
            line = f.readline()

    # normalization
    # dataSet = normalization_dimention(dataSet)
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    # dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], max_len)
    return dataSet, seq_len, Max, Min


def load_after_time14(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            data = []
            nums = line.split('-')
            for x in nums:
                if x != '':
                    data.append(int(x))
            dataSet.append(data)
            line = f.readline()

    # normalization
    # dataSet = normalization_dimention(dataSet)
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    # dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], max_len)
    return dataSet, seq_len, Max, Min


def preprocess_datetime2(date_string):
    # 解析日期字符串
    date_object = datetime.strptime(date_string, "%a %b %d %H:%M:%S %Z %Y")
    # 将日期时间转换为数值类型（例如，Unix时间戳）
    timestamp = date_object.timestamp()
    return timestamp


def load_after_jacksondatabind_87(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            data = []
            date_string = line
            # 预处理日期时间
            timestamp = preprocess_datetime2(date_string)
            data.append(timestamp)
            dataSet.append(data)
            line = f.readline()

    # 归一化
    dataSet, Max, Min = normalization_array(dataSet)

    # padding
    max_len = max(len(x) for x in dataSet)
    # dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], max_len)

    return dataSet, seq_len, Max, Min


def load_data_time3(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            words = line.split('#')
            data = [int(x) for x in words]
            dataSet.append(data)
            line = f.readline()

    # normalization
    dataSet, Maxs, Mins = normalization_dimention(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], max_len)
    return dataSet, seq_len, Maxs, Mins


def load_data_mockito6(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            words = line.split()
            if words[0] != 'null':
                data = [int(x) for x in words]
            else:
                for word in words:
                    data = [ord(x) for x in list(word)]
            dataSet.append(data)
            line = f.readline()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], -1)
    return dataSet, seq_len, Max, Min


def load_data_math15(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            words = line.split()
            if words[0] != 'Infinity':
                data = [float(x) for x in words]
            else:
                data = [0]
            dataSet.append(data)
            line = f.readline()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], -1)
    return dataSet, seq_len, Max, Min


def load_data_exp_time7(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            words = line.split()
            data = [float(word) for word in words]
            dataSet.append(data)
            line = f.readline()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], -1)
    return dataSet, seq_len, Max, Min


def load_data_compress40(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            words = line.split('#')
            lst = words[0].split()
            data = [int(x) for x in lst]
            data.append(int(words[1]))
            dataSet.append(data)
            line = f.readline()

    # normalization
    dataSet, Max, Min = normalization_array(dataSet)
    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], max_len)
    return dataSet, seq_len, Max, Min


def load_classification(filename):
    dataSet = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            data = []
            if line == 'true\n':
                data.append(1)
            else:
                data.append(0)
            dataSet.append(data)
            line = f.readline()
    # normalization
    dataSet, Max, Min = normalization_array(dataSet)

    # padding
    max_len = max(len(x) for x in dataSet)
    dataSet = padding_array(dataSet, max_len)
    # mask
    seq_len = [len(x) for x in dataSet]
    dataSet = np.array(dataSet)
    dataSet = dataSet.reshape(dataSet.shape[0], max_len)
    return dataSet, seq_len, Max, Min


def load_M1_before(filename):
    X, seq_len_X, max_x, min_x = load_sequence(filename)
    return X, seq_len_X, max_x, min_x


def load_M1_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M2_before(filename):
    X, seq_len_X, max_x, min_x = load_array(filename)
    return X, seq_len_X, max_x, min_x


def load_M2_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M3_before(filename):
    X, seq_len_X, max_x, min_x = load_sequence(filename)
    return X, seq_len_X, max_x, min_x


def load_M3_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M4_before(filename):
    X, seq_len_X, max_x, min_x = load_data_time3(filename)
    return X, seq_len_X, max_x, min_x


def load_M4_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M5_before(filename):
    X, seq_len_X, max_x, min_x = load_data_time3(filename)
    return X, seq_len_X, max_x, min_x


def load_M5_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M6_before(filename):
    X, seq_len_X, max_x, min_x = load_data_time3(filename)
    return X, seq_len_X, max_x, min_x


def load_M6_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M7_before(filename):
    X, seq_len_X, max_x, min_x = load_data_time3(filename)
    return X, seq_len_X, max_x, min_x


def load_M7_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M8_before(filename):
    X, seq_len_X, max_x, min_x = load_data_time3(filename)
    return X, seq_len_X, max_x, min_x


def load_M8_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M9_before(filename):
    X, seq_len_X, max_x, min_x = load_before_time14(filename)
    return X, seq_len_X, max_x, min_x


def load_M9_after(filename):
    Y, seq_len_Y, max_y, min_y = load_after_time14(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M10_before(filename):
    X, seq_len_X, max_x, min_x = load_before_time14(filename)
    return X, seq_len_X, max_x, min_x


def load_M10_after(filename):
    Y, seq_len_Y, max_y, min_y = load_after_time14(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M11_before(filename):
    X, seq_len_X, max_x, min_x = load_sequence(filename)
    return X, seq_len_X, max_x, min_x


def load_M11_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M12_before(filename):
    X, seq_len_X, max_x, min_x = load_array(filename)
    return X, seq_len_X, max_x, min_x


def load_M12_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M13_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M13_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M14_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M14_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M15_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M15_after(filename):
    Y, seq_len_Y, max_y, min_y = load_classification(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M16_before(filename):
    X, seq_len_X, max_x, min_x = load_sequence(filename)
    return X, seq_len_X, max_x, min_x


def load_M16_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M17_before(filename):
    X, seq_len_X, max_x, min_x = load_data_mockito6(filename)
    return X, seq_len_X, max_x, min_x


def load_M17_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M18_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M18_after(filename):
    Y, seq_len_Y, max_y, min_y = load_classification(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M19_before(filename):
    X, seq_len_X, max_x, min_x = load_data_math15(filename)
    return X, seq_len_X, max_x, min_x


def load_M19_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M20_before(filename):
    X, seq_len_X, max_x, min_x = load_sequence(filename)
    return X, seq_len_X, max_x, min_x


def load_M20_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M21_before(filename):
    X, seq_len_X, max_x, min_x = load_sequence(filename)
    return X, seq_len_X, max_x, min_x


def load_M21_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M22_before(filename):
    X, seq_len_X, max_x, min_x = load_data(filename)
    return X, seq_len_X, max_x, min_x


def load_M22_after(filename):
    Y, seq_len_Y, max_y, min_y = load_data(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M23_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M23_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M24_before(filename):
    X, seq_len_X, max_x, min_x = load_sequence(filename)
    return X, seq_len_X, max_x, min_x


def load_M24_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M25_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M25_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M26_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_M26_after(filename):
    Y, seq_len_Y, max_y, min_y = load_classification(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M27_before(filename):
    Y, seq_len_Y, max_y, min_y = load_data(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M27_after(filename):
    Y, seq_len_Y, max_y, min_y = load_data(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M28_before(filename):
    Y, seq_len_Y, max_y, min_y = load_data(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M28_after(filename):
    Y, seq_len_Y, max_y, min_y = load_data(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M29_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_M29_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M30_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_M30_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M31_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M31_after(filename):
    Y, seq_len_Y, max_y, min_y = load_classification(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M32_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M32_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M33_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_M33_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M34_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M34_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M35_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '%')
    return Y, seq_len_Y, max_y, min_y


def load_M35_after(filename):
    Y, seq_len_Y, max_y, min_y = load_classification(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M36_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M36_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M37_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_M37_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M39_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M39_after(filename):
    Y, seq_len_Y, max_y, min_y = load_classification(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M40_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M40_after(filename):
    Y, seq_len_Y, max_y, min_y = load_data(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M41_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_M41_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M42_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M42_after(filename):
    Y, seq_len_Y, max_y, min_y = load_data(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M43_before(filename):
    Y, seq_len_Y, max_y, min_y = load_data(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M43_after(filename):
    Y, seq_len_Y, max_y, min_y = load_data(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M44_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_M44_after(filename):
    Y, seq_len_Y, max_y, min_y = load_data(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M45_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M45_after(filename):
    Y, seq_len_Y, max_y, min_y = load_data(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M46_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M46_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M47_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M47_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M48_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M48_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M49_before(filename):
    Y, seq_len_Y, max_y, min_y = load_data(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M49_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M50_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M50_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M51_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M51_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M52_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_M52_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M53_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M53_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M54_before(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence_split(filename, '$')
    return Y, seq_len_Y, max_y, min_y


def load_M54_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M55_before(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M55_after(filename):
    Y, seq_len_Y, max_y, min_y = load_array(filename)
    return Y, seq_len_Y, max_y, min_y

def load_M56_before(filename):
    Y, seq_len_Y, max_y, min_y = load_data(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M56_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y

def load_M57_before(filename):
    Y, seq_len_Y, max_y, min_y = load_data(filename)
    return Y, seq_len_Y, max_y, min_y


def load_M57_after(filename):
    Y, seq_len_Y, max_y, min_y = load_sequence(filename)
    return Y, seq_len_Y, max_y, min_y


before_func = {
    # TM
    'jacksoncore_6': load_M1_before,
    'compress_30': load_M2_before,
    'csv_14': load_M3_before,
    'time_3_addYears': load_M4_before,
    'time_3_addMonths': load_M5_before,
    'time_3_addWeeks': load_M6_before,
    'time_3_addDays': load_M7_before,
    'time_3_add': load_M8_before,
    'time_14_minusMonths': load_M9_before,
    'time_14_plusMonths': load_M10_before,
    'csv_3': load_M11_before,
    'lang_21': load_M12_before,
    'io_18': load_M13_before,
    'shiro_web_3': load_M14_before,
    'johnzon_core_2': load_M15_before,
    'compress_39': load_M16_before,
    'mockito_6': load_M17_before,
    'geometry_core_3': load_M18_before,
    'math_15': load_M19_before,
    'codec_15': load_M20_before,
    'codec_3': load_M21_before,
    'compress_40': load_M22_before,
    'io_25': load_M23_before,
    'compress_50': load_M24_before,
    'math_24': load_M25_before,
    'io_13': load_M26_before,
    'cli_34': load_M27_before,
    'codec_12': load_M28_before,
    'codec_14': load_M29_before,
    'suncalc_1': load_M30_before,
    'compress_6': load_M31_before,
    'coveralls_maven_plugin_6': load_M32_before,
    'math_26': load_M33_before,
    'math_5': load_M34_before,
    'drools_model_compiler_1': load_M35_before,
    'gson_9': load_M36_before,
    'hivemall_core_1': load_M37_before,
    'io_8': load_M39_before,
    'io_2': load_M40_before,
    'vault_core_1': load_M41_before,
    'jacksoncore_12': load_M42_before,
    'jacksoncore_28': load_M43_before,
    'jacksondatabind_101': load_M44_before,
    'jacksondatabind_12': load_M45_before,
    'jacksondatabind_56': load_M46_before,
    'jacksondatabind_87': load_M47_before,
    'jacksondatabind_30': load_M48_before,
    'jacksondatabind_31': load_M49_before,
    'jacksonxml_1': load_M50_before,
    'jacksonxml_2': load_M51_before,
    'james_mime4j_core_6': load_M52_before,
    'james_mime4j_core_7': load_M53_before,
    'james_mime4j_core_8': load_M54_before,
    'math_8': load_M56_before,
    'math_9': load_M57_before

}

after_func = {
    # TM
    'jacksoncore_6': load_M1_after,
    'compress_30': load_M2_after,
    'csv_14': load_M3_after,
    'time_3_addYears': load_M4_after,
    'time_3_addMonths': load_M5_after,
    'time_3_addWeeks': load_M6_after,
    'time_3_addDays': load_M7_after,
    'time_3_add': load_M8_after,
    'time_14_minusMonths': load_M9_after,
    'time_14_plusMonths': load_M10_after,
    'csv_3': load_M11_after,
    'lang_21': load_M12_after,
    'io_18': load_M13_after,
    'shiro_web_3': load_M14_after,
    'johnzon_core_2': load_M15_after,
    'compress_39': load_M16_after,
    'mockito_6': load_M17_after,
    'geometry_core_3': load_M18_after,
    'math_15': load_M19_after,
    'codec_15': load_M20_after,
    'codec_3': load_M21_after,
    'compress_40': load_M22_after,
    'io_25': load_M23_after,
    'compress_50': load_M24_after,
    'math_24': load_M25_after,
    'io_13': load_M26_after,
    'cli_34': load_M27_after,
    'codec_12': load_M28_after,
    'codec_14': load_M29_after,
    'suncalc_1': load_M30_after,
    'compress_6': load_M31_after,
    'coveralls_maven_plugin_6': load_M32_after,
    'math_26': load_M33_after,
    'math_5': load_M34_after,
    'drools_model_compiler_1': load_M35_after,
    'gson_9': load_M36_after,
    'hivemall_core_1': load_M37_after,
    'io_8': load_M39_after,
    'io_2': load_M40_after,
    'vault_core_1': load_M41_after,
    'jacksoncore_12': load_M42_after,
    'jacksoncore_28': load_M43_after,
    'jacksondatabind_101': load_M44_after,
    'jacksondatabind_12': load_M45_after,
    'jacksondatabind_56': load_M46_after,
    'jacksondatabind_87': load_M47_after,
    'jacksondatabind_30': load_M48_after,
    'jacksondatabind_31': load_M49_after,
    'jacksonxml_1': load_M50_after,
    'jacksonxml_2': load_M51_after,
    'james_mime4j_core_6': load_M52_after,
    'james_mime4j_core_7': load_M53_after,
    'james_mime4j_core_8': load_M54_after,
    'math_8': load_M56_after,
    'math_9': load_M57_after

}
