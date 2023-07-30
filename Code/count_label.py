import numpy as np
import Coverage
import daikon
import random
import defines
import os
# random:(1100000,)
# coverage: (100000,)
# daikon: (100000,)

number = 10
Daikon_Test = 'daikon_label.txt'
Coverage_Test = 'coverage_label.txt'
Random_Test = 'label.txt'
num_dict = {Daikon_Test: 0, Coverage_Test: 0, Random_Test: 1000000}


def count_num(filename, rootPath, idx, begin_num):
    top_1 = 0
    top_5 = 0
    top_10 = 0
    top_100 = 0
    for i in range(0, number):
        labelSet = []
        # Coverage
        Coverage.load_file(rootPath)
        # Daikon
        # daikon
        # daikon.main(rootPath, idx)
        with open(filename, 'r') as f:
            line = f.readline()
            while line:
                arr = line.split()
                label = [int(x) for x in arr]
                labelSet.append(label)
                line = f.readline()
        DataSet = labelSet[begin_num:]
        # random
        random.shuffle(DataSet)
        DataSet = np.array(DataSet)
        top_1 += 1 - np.sum(DataSet[0])
        top_5 += 5 - np.sum(DataSet[0:5])
        top_10 += 10 - np.sum(DataSet[0:10])
        top_100 += 100 - np.sum(DataSet[0:100])
    ave_1 = float(top_1) / number
    ave_10 = float(top_10) / number
    ave_100 = float(top_100) / number
    print('{}, {}, {}'.format(ave_1, ave_10, ave_100))
    print('---------------------')
    return ave_1, ave_10, ave_100


idx = [11, 13, 16, 18, 19, 20, 21, 22, 23]
if __name__ == '__main__':
    filename = Random_Test
    top_1, top_10, top_100 = 0, 0, 0
    cnt = 0
    for i, name in enumerate(defines.TM):
        path = os.path.join(defines.TM_PATH, name.value)
        file_path = os.path.join(path, filename)
        if i + 1 in idx:
            print(i + 1, file_path)
            a, b, c = count_num(file_path, path, i + 1, num_dict[filename])
            top_1 += a
            top_10 += b
            top_100 += c
            cnt += 1
    top_1 /= cnt
    top_10 /= cnt
    top_100 /= cnt
    # for i in range(4, 10):
