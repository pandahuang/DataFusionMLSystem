import random
def TrainSetSelection(label_data_g, label_data_b, train_good_num, train_bad_num):
    train_data = []
    for data in label_data_g[:train_good_num]:
        train_data.append(data)
    for data in label_data_b[:train_bad_num]:
        train_data.append(data)
    random.shuffle(train_data)
    return train_data