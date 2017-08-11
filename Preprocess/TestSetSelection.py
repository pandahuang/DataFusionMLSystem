import random
def TestSetSelection(label_data_g, label_data_b, test_good_num, test_bad_num):
    test_data = []
    for data in label_data_g[test_good_num:]:
        test_data.append(data)
    for data in label_data_b[test_bad_num:]:
        test_data.append(data)
    random.shuffle(test_data)
    return test_data