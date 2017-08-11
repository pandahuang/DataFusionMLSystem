from Data import FileNameDef

def TsFeatureGeneration(path_feature_ts_o = FileNameDef.PATH_ALLFEATURE_TS_ORIGIONAL, path_feature_ts = FileNameDef.PATH_ALLFEATURE_TS):
    feature_ts_o_dict = {}
    with open(path_feature_ts_o) as fopen:
        lines = fopen.readlines()
    for line in lines:
        feature_ts_o_dict[line.strip().split(' ')[0]] = FloatTranslation(line.strip().split(' ')[1:])
    feature_ts_dict = LocalStatistic(feature_ts_o_dict)
    with open(path_feature_ts, "w") as fopen:
        for k, v in feature_ts_dict.iteritems():
            fopen.write(k + "\t" + StringTranslation(v) + "\n")
    print "Ts Feature Generation Done..."

def FloatTranslation(feature_list):
    float_list = []
    for data in feature_list:
        float_list.append(float(data))
    return float_list

def StringTranslation(feature_list):
    feature_str = ""
    for pos in range(len(feature_list)):
        if pos == 0:
            feature_str = str(feature_list[pos])
        else:
            feature_str = feature_str + "\t" + str(feature_list[pos])
    return feature_str

import numpy as np

def LocalStatistic(feature_dict):
    local_statistic_dict = {}
    global_mean = GlobalStatistic(feature_dict)
    for k, v in feature_dict.iteritems():
        array_list = np.array(v)
        statistic_list = [array_list.max(), array_list.min(), array_list.mean(), array_list.var(), Num_Counter(v, 0), Num_Counter(v, array_list.mean()), Num_Counter(v, global_mean)]
        local_statistic_dict[k] = statistic_list
    return local_statistic_dict

def GlobalStatistic(feature_dict):
    total_sum = 0
    no_zero_num = 0
    for k, v in feature_dict.iteritems():
        total_sum = total_sum + np.array(v).sum()
        no_zero_num = no_zero_num + Num_Counter(v, 0)
    return float(total_sum)/no_zero_num

def Similarity(feature_dict):
    pass

def Num_Counter(feature_list, num):
    counter = 0
    for data in feature_list:
        if data > num:
            counter += 1
    return counter

def E(feature_dict):
    pass

def F(feature_dict):
    pass

if __name__=="__main__":
   pass