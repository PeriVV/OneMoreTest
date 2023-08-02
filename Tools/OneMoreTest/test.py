import os
import time

import numpy as np
from tensorflow import keras

import defines
import loadData


def calculate_dis_seq(y_pred, y_true, seq_length):
    # 最小编辑距离，字符不匹配就+1
    distance = 0
    max_dis = 0
    min_dis = 1000
    match_num = 0
    cnt = 0
    lst = []
    for i in range(0, len(y_pred)):
        length = seq_length[i]
        lt_pred = np.array(y_pred[i][0:length])
        lt_true = np.array(y_true[i][0:length])
        edit_dis = sum(lt_pred != lt_true) / (length * 2)
        if edit_dis <= 0.05:
            match_num += 1
        elif cnt < 10:
            lst.append((i, lt_pred, lt_true))
            cnt += 1
        dis = float(pow(edit_dis, 2))
        max_dis = max(dis, max_dis)
        min_dis = min(dis, min_dis)
        distance += dis
    distance /= len(y_pred)
    match_rate = match_num / len(y_pred)
    # print(lst)
    return distance, match_rate, max_dis, min_dis


def calculate_dis_array(y_pred, y_true, arr_length):
    # 计算每个样本的每个参数之间的差值取平均值
    distance = 0
    match_num = 0
    Sum = 0
    for i in range(0, len(y_pred)):
        tmp = 0
        length = arr_length[i]
        Sum += length
        for j in range(0, len(y_pred[i])):
            if j >= length:
                break
            if y_true[i][j] == 0:
                array_dis = abs(y_pred[i][j] - y_true[i][j])
            else:
                array_dis = abs((y_pred[i][j] - y_true[i][j]) / y_true[i][j])
            if array_dis <= 0.05:
                match_num += 1
            tmp += array_dis
        distance += tmp / length
    distance /= len(y_pred)
    match_rate = match_num / Sum
    return distance, match_rate


def test(rootpath, name, dataset):
    modelpath = os.path.join(rootpath, 'model', name + '.hdf5')
    model = keras.models.load_model(modelpath)
    model.summary()

    train_num = 1000000
    batch_size = 512
    max_pre1 = 0
    max_pre3 = 0
    max_pre5 = 0
    max_pre10 = 0
    max_pre100 = 0
    path = os.path.join(rootPath, dataset, name)
    before_file = os.path.join(path, 'before_data.txt')
    after_file = os.path.join(path, 'after_data.txt')
    label_file = os.path.join(path, 'label.txt')
    X, seq_len_X, max_x, min_x = loadData.before_func.get(name)(before_file)
    Y, seq_len_Y, max_y, min_y = loadData.after_func.get(name)(after_file)
    with open(after_file, 'r') as f:
        Y_orin = f.readlines()
    with open(before_file, 'r') as f:
        X_orin = f.readlines()
    with open(label_file, 'r') as f:
        Label = f.readlines()

    # X_original = loadData.return_before(X, max_x, min_x)
    Y_original = loadData.return_before(Y, max_y, min_y)
    Y = np.array(Y)
    Label = loadData.load_label(label_file)
    embed_X = X.shape[1]
    embed_Y = Y.shape[1]
    print(X.shape, Y.shape)
    x_test = X[train_num:]
    y_true = Y[train_num:]
    label_test = Label[train_num:]
    y_original_test = Y_original[train_num:]
    y_len_test = seq_len_Y[train_num:]

    # label_train = Label[0:train_num]
    # model.evaluate(x_test, y_true, batch_size)
    print(np.shape(x_test))
    y_pred = model.predict(x_test)
    dis = np.mean(np.square(y_pred - y_true), axis=1)
    print(dis[0])
    # dis = tf.reduce_mean(tf.square(y_pred - y_true), axis=1, keep_dims=False)
    loss_index = np.argsort(dis)
    samples_index = loss_index[-1 * int(100):]
    samples_index = samples_index[::-1]
    label_output = []
    for j in range(len(samples_index)):
        label_output.append(label_test[samples_index[j]])
    fn100 = np.sum(label_output)  # 判断为负样本，判断错误
    tn100 = 100 - fn100  # 判断为负样本，判断正确
    max_pre100 = max(max_pre100, tn100)

    # top-10
    samples_index = loss_index[-1 * int(10):]
    samples_index = samples_index[::-1]
    label_output = []
    for j in range(len(samples_index)):
        label_output.append(label_test[samples_index[j]])
    fn10 = np.sum(label_output)  # 判断为负样本，判断错误
    tn10 = 10 - fn10  # 判断为负样本，判断正确
    max_pre10 = max(max_pre10, tn10)

    # top-3
    samples_index = loss_index[-1 * int(3):]
    samples_index = samples_index[::-1]
    label_output = []
    for j in range(len(samples_index)):
        label_output.append(label_test[samples_index[j]])
    fn3 = np.sum(label_output)  # 判断为负样本，判断错误
    tn3 = 3 - fn3  # 判断为负样本，判断正确
    max_pre3 = max(max_pre3, tn3)

    # top-5
    samples_index = loss_index[-1 * int(5):]
    samples_index = samples_index[::-1]
    label_output = []
    for j in range(len(samples_index)):
        label_output.append(label_test[samples_index[j]])
    fn5 = np.sum(label_output)  # 判断为负样本，判断错误
    tn5 = 5 - fn5  # 判断为负样本，判断正确
    max_pre5 = max(max_pre5, tn5)

    # top-1
    samples_index = loss_index[-1:]
    if label_test[samples_index] == 1:
        fn1 = 1
    else:
        fn1 = 0
    tn1 = 1 - fn1
    max_pre1 = max(max_pre1, tn1)
    print(
        'tn100: %.1f  fn100: %.1f  tn10:%.1f  fn10:%.1f  tn5:%.1f  fn5:%.1f  tn3:%.1f  fn3:%.1f  tn1:%.1f  max_pre100: %.1f  max_pre10:%.1f  max_pre5:%.1f  max_pre3:%.1f  max_pre1:%.1f'
        % (tn100, fn100, tn10, fn10, tn5, fn5, tn3, fn3, tn1, max_pre100, max_pre10, max_pre5, max_pre3, max_pre1))

    Y_orin = np.array(Y_orin)
    X_orin = np.array(X_orin)
    Label = np.array(Label)

    top100_samples_index = loss_index[-1 * int(100):]
    top10_samples_index = loss_index[-1 * int(10):]
    top5_samples_index = loss_index[-1 * int(5):]
    top3_samples_index = loss_index[-1 * int(3):]
    top1_samples_index = loss_index[-1:]

    # 在代码末尾添加以下代码
    output_dir = os.path.join(rootPath, dataset, name)  # 输出文件夹路径
    os.makedirs(output_dir, exist_ok=True)  # 确保输出文件夹存在

    # 将打印结果到控制台的代码替换为输出到文件的代码
    with open(os.path.join(output_dir, 'top100.txt'), 'w') as f:
        f.write("Top 100 test cases:\n")
        f.write("input\toutput\n")
        for i in top100_samples_index:
            f.write(f"{X_orin[i + 1000000]}{Y_orin[i + 1000000]}{Label[i + 1000000]}")
            f.write("\n")

    with open(os.path.join(output_dir, 'top10.txt'), 'w') as f:
        f.write("Top 10 test cases:\n")
        f.write("input\toutput\n")
        for i in top10_samples_index:
            f.write(f"{X_orin[i + 1000000]}{Y_orin[i + 1000000]}{Label[i + 1000000]}")
            f.write("\n")

    with open(os.path.join(output_dir, 'top5.txt'), 'w') as f:
        f.write("Top 5 test cases:\n")
        f.write("input\toutput\n")
        for i in top5_samples_index:
            f.write(f"{X_orin[i + 1000000]}{Y_orin[i + 1000000]}{Label[i + 1000000]}")
            f.write("\n")

    with open(os.path.join(output_dir, 'top3.txt'), 'w') as f:
        f.write("Top 3 test cases:\n")
        f.write("input\toutput\n")
        for i in top3_samples_index:
            f.write(f"{X_orin[i + 1000000]}{Y_orin[i + 1000000]}{Label[i + 1000000]}")
            f.write("\n")

    with open(os.path.join(output_dir, 'top1.txt'), 'w') as f:
        f.write("Top 1 test case:\n")
        f.write("input\toutput\n")
        for i in top1_samples_index:
            f.write(f"{X_orin[i + 1000000]}{Y_orin[i + 1000000]}{Label[i + 1000000]}")
            f.write("\n")

if __name__ == '__main__':
    start = time.perf_counter()
    rootPath = os.path.abspath('.')
    print(rootPath)
    for i, name in enumerate(defines.TM):
        print('----------------------------------' + name.value + '----------------------------------')
        test(rootPath, name.value, 'TM')
    end = time.perf_counter()
    elapsed_time = end - start
    print("Elapsed time:", elapsed_time, "seconds")