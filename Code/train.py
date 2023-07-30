# -*- coding: utf-8 -*-
import numpy as np
import tensorflow._api.v2.compat.v1 as tf
import loadData
import time
import os
import defines
from tensorflow import keras

tf.compat.v1.disable_eager_execution()
def one_hot(label, num_class):
    label = np.array(label)
    num_label = label.shape[0]
    index = np.arange(num_label) * num_class
    out = np.zeros((num_label, num_class))
    out.flat[index + label.ravel()] = 1
    return out


def model(input_tensor, hidden_size, output_size):
    with tf.variable_scope("Dense"):
        '''tensor1 = tf.layers.dense(inputs=input1,
                                  units=hidden_size,
                                  activation=tf.nn.relu)
        tensor2 = tf.layers.dense(inputs=tensor1, units=1)'''
        layer1 = tf.layers.dense(inputs=input_tensor,
                                 units=hidden_size,
                                 activation=tf.nn.relu,
                                 kernel_regularizer=tf.keras.regularizers.l2(0.01))
        drop1 = tf.layers.dropout(inputs=layer1, rate=0.2)
        layer2 = tf.layers.dense(inputs=drop1,
                                 units=hidden_size,
                                 activation=tf.nn.relu,
                                 kernel_regularizer=tf.keras.regularizers.l2(0.01))
        drop2 = tf.layers.dropout(inputs=layer2, rate=0.2)
        layer3 = tf.layers.dense(inputs=drop2,
                                 units=hidden_size,
                                 activation=tf.nn.relu,
                                 kernel_regularizer=tf.keras.regularizers.l2(0.01))
        drop3 = tf.layers.dropout(inputs=layer3, rate=0.2)
        layer = tf.layers.dense(inputs=drop3, units=output_size)
    return layer


def create_model(input_size, hidden_size, output_size):
    model = keras.Sequential([
        keras.layers.Dense(input_shape=(input_size, ),
                           units=hidden_size,
                           activation='relu',
                           kernel_regularizer=tf.keras.regularizers.l2(0.01)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(units=hidden_size,
                           activation=tf.nn.relu,
                           kernel_regularizer=tf.keras.regularizers.l2(0.01)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(output_size)
    ])
    # model.compile(loss="mean_squared_error", optimizer=keras.optimizers.SGD(0.001), metrics=['accuracy'])
    model.compile(optimizer='adam', loss='mse', metrics=['mse'])
    return model


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


def train(rootPath, name, epoch):
    start = time.time()
    lr = 0.0001
    hidden_size = 256
    batch_size = 512
    train_num = 1000000
    iterations = 100000
    max_pre1 = 0
    max_pre5 = 0
    max_pre10 = 0
    max_pre100 = 0
    path = os.path.join(rootPath, name)
    before_file = os.path.join(path, 'before_data.txt')
    after_file = os.path.join(path, 'after_data.txt')
    label_file = os.path.join(path, 'label.txt')
    X, seq_len_X, max_x, min_x = loadData.before_func.get(name)(before_file)
    Y, seq_len_Y, max_y, min_y = loadData.after_func.get(name)(after_file)
    # X_original = loadData.return_before(X, max_x, min_x)
    Y_original = loadData.return_before(Y, max_y, min_y)
    # Y_original = Y
    Y = np.array(Y)
    Label = loadData.load_label(label_file)
    embed_X = X.shape[1]
    embed_Y = Y.shape[1]
    print(X.shape, Y.shape)
    x_train = X[0:train_num]
    x_test = X[train_num:]

    y_train = Y[0:train_num]
    y_test = Y[train_num:]
    # y_original_train = Y_original[0:train_num]
    y_original_test = Y_original[train_num:]
    y_len_test = seq_len_Y[train_num:]

    # label_train = Label[0:train_num]
    label_test = Label[train_num:]
    print(np.shape(x_train),np.shape(y_train))
    Model = create_model(input_size=embed_X, hidden_size=hidden_size, output_size=embed_Y)
    # Model.summary()
    Model.fit(x_train, y_train, batch_size, epochs=epoch)

    Model.evaluate(x_test, y_test, batch_size)
    Model.save(f'./model/{name}.hdf5')

    '''data = np.array([[100, int(tn100), int(fn100)],
                        [10, int(tn10), int(fn10)],
                        [5, int(tn5), int(fn5)],
                        [1, int(tn1), int(fn1)]])
    np.savetxt(path + '1_data.txt', data)
    np.savetxt(path + '1.txt', test_out)'''


if __name__ == '__main__':
    rootPath = defines.TM_PATH
    for i, name in enumerate(defines.TM):
        print(i + 1, name.value)
        train(rootPath, name.value, 4)
