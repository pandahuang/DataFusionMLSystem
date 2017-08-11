from Data import FileNameDef

def ListDetection(list_tc, list_ts, pos_num, neg_num):
    addition_data_top = []
    addition_data_bottom = []
    addition_data = []
    rest_data = []
    for (k, v) in list_tc[:pos_num]:
        if v > 0.5:
            addition_data_top.append(k)
        else:
            print "There is no available data for positive trainset..."
    for (k, v) in list_tc[-neg_num:]:
        if v <= 0.5:
            addition_data_bottom.append(k)
        else:
            print "There is no available data for negative trainset..."
    for (k, v) in list_ts[:pos_num]:
        if v > 0.5:
            addition_data_top.append(k)
        else:
            print "There is no available data for positive ts trainset..."
    for (k, v) in list_ts[-neg_num:]:
        if v <= 0.5:
            addition_data_bottom.append(k)
        else:
            print "There is no available data for negative ts trainset..."
    for (k, v) in list_tc[pos_num:-neg_num]:
        rest_data.append(k)
    for (k, v) in list_ts[pos_num:-neg_num]:
        rest_data.append(k)
    for data in list(set(addition_data_top) - (set(addition_data_top)&set(addition_data_bottom))):
        addition_data.append(data + "\t" + "1")
    for data in list(set(addition_data_bottom) - (set(addition_data_top)&set(addition_data_bottom))):
        addition_data.append(data + "\t" + "0")
    for data in list(set(addition_data_top)&set(addition_data_bottom)):
        rest_data.append(data)
    return (addition_data, list(set(rest_data)))

def TrainDataSelection(predict_data, proba_result_tc, proba_result_ts, pos_num, neg_num):
    result_dict_tc = {}
    result_dict_ts = {}
    for (pre, pro_tc, pro_ts) in zip(predict_data, proba_result_tc, proba_result_ts):
        result_dict_tc[pre[-1]] = pro_tc[1]
        result_dict_ts[pre[-1]] = pro_ts[1]
    sorted_result_dict_tc = sorted(result_dict_tc.iteritems(), key=lambda d:d[1], reverse=True)
    sorted_result_dict_ts = sorted(result_dict_ts.iteritems(), key=lambda d: d[1], reverse=True)
    addition_data, rest_data = ListDetection(sorted_result_dict_tc, sorted_result_dict_ts, pos_num, neg_num)
    return (addition_data, rest_data)

def TrainDataAddition(addition_data, path_train_data = FileNameDef.PATH_TRAIN_DATA, path_feature = FileNameDef.PATH_COMBINE_FEATURE):
    with open(path_feature) as fopen1, open(path_train_data, "a") as fopen2:
        lines1 = fopen1.readlines()
        feature_dict = {}
        for line1 in lines1:
            feature_dict[line1.strip().split('\t', 1)[0]] = line1.strip().split('\t', 1)[1]
        for data in addition_data:
            fopen2.write(data.split('\t')[0] + "\t" + feature_dict[data.split('\t')[0]] + "\t" + data.split('\t')[1] + "\n")
    print "Training set addition done..."
    pass

def PredictDataRemovement(rest_data, path_predict_data = FileNameDef.PATH_PREDICT_DATA, path_feature = FileNameDef.PATH_COMBINE_FEATURE):
    with open(path_feature) as fopen1, open(path_predict_data, "w") as fopen2:
        lines1 = fopen1.readlines()
        feature_dict = {}
        for line1 in lines1:
            feature_dict[line1.strip().split('\t', 1)[0]] = line1.strip().split('\t', 1)[1]
        for data in rest_data:
            fopen2.write(data + "\t" + feature_dict[data] + "\n")
        print "Predict set removement done..."
        pass

def DataMoving(predict_data, proba_result_tc, proba_result_ts, pos_num, neg_num):
    addition_data, rest_data = TrainDataSelection(predict_data, proba_result_tc, proba_result_ts, pos_num, neg_num)
    TrainDataAddition(addition_data)
    PredictDataRemovement(rest_data)
    return len(addition_data)

def DataRemovement(add_num, path_train_data = FileNameDef.PATH_TRAIN_DATA):
    data_lines = []
    with open(path_train_data) as fopen:
        lines = fopen.readlines()
        data_lines = [line.strip() for line in lines[:-add_num]]
    with open(path_train_data, "w") as fopen:
        for line in data_lines:
            fopen.write(line + "\n")
    print "Futile Data Removement done..."
    pass