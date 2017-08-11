from Data import FileNameDef

def FeatureSetting(path_feature, label_data_g, label_data_b):
    with open(path_feature) as fopen:
        lines = fopen.readlines()
        for line in lines:
            ip_features = line.strip().split('\t', 1)
            if label_data_b.has_key(ip_features[0]):
                label_data_b[ip_features[0]] = ip_features[1] + "\t" + label_data_b.get(ip_features[0])
            if label_data_g.has_key(ip_features[0]):
                label_data_g[ip_features[0]] = ip_features[1] + "\t" + label_data_g.get(ip_features[0])
    return (label_data_g, label_data_b)

import random
def DataRandom(label_data_dict):
    label_data_list = []
    print "Random stage..."
    for k,v in label_data_dict.iteritems():
        data_line = k + "\t" + v
        label_data_list.append(data_line)
    random.shuffle(label_data_list)
    return label_data_list

def LabelDataConsistant(label_data_g, label_data_b):
    label_data_g_list = DataRandom(label_data_g)
    label_data_b_list = DataRandom(label_data_b)
    with open(FileNameDef.PATH_LABELED_DATA_GOOD, "w") as fopen1, open(FileNameDef.PATH_LABELED_DATA_BAD, "w") as fopen2:
        for data_g in label_data_g_list:
            fopen1.write(data_g + "\n")
        for data_b in label_data_b_list:
            fopen2.write(data_b + "\n")
    print "label data consist done, positive num is %d, negative num is %d..."%(len(label_data_g), len(label_data_b))
    return (label_data_g_list, label_data_b_list)

def Labelling(path_good, path_bad, path_feature):
    label_data_g = {}
    label_data_b = {}
    with open(path_good) as fopen:
        lines = fopen.readlines()
        for line in lines:
            label_data_g[line.strip().split("\t", 1)[0]] = "0"
    with open(path_bad) as fopen:
        lines = fopen.readlines()
        for line in lines:
            label_data_b[line.strip().split("\t", 1)[0]] = "1"
    label_data_g, label_data_b = FeatureSetting(path_feature, label_data_g, label_data_b)
    label_data_g_list, label_data_b_list = LabelDataConsistant(label_data_g, label_data_b)

    return (label_data_g_list, label_data_b_list)
