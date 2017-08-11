#run independent
from Data import FileNameDef

def FeatureExchange(feature):
    feature_string = ""
    features = feature.strip().split('\t')
    feature_one = features.pop(1)
    features.append(feature_one)
    feature_two = features.pop(8)
    features.insert(1, feature_two)
    for i in range(len(features)):
        if i == 0:
            feature_string = features[i]
        else:
            feature_string = feature_string + "\t" + features[i]
    return feature_string

def FeatureCombination(path_feature_tc, path_feature_ts, path_combain_feature):
    st_feature = {}
    print "st feature and ts feature combaining..."
    with open(path_feature_tc) as fopen1, open(path_feature_ts) as fopen2, open(path_combain_feature, "w") as fopen3:
        lines1 = fopen1.readlines()
        lines2 = fopen2.readlines()
        verify_num1 = 0
        verify_num2 = 0
        for line1 in lines1:
            st_feature[line1.strip().split('\t', 1)[0]] = line1.strip().split('\t', 1)[1]
        verify_num1 = len(st_feature)
        for line2 in lines2:
            st_feature[line2.strip().split('\t', 1)[0]] = st_feature[line2.strip().split('\t', 1)[0]] + "\t" + line2.strip().split('\t', 1)[1]
            verify_num2 += 1
        if verify_num1 == verify_num2:
            print "Verify Process Done..."
        else:
            print "The IPs of two feature files are not matched..."
        for k,v in st_feature.iteritems():
            n_v = FeatureExchange(v)
            fopen3.write(k + "\t" + n_v + "\n")
    print "combination done, data amount:%d"%(len(st_feature))

if __name__=="__main__":
    # FeatureCombination()
    FeatureCombination(FileNameDef.PATH_ALLFEATURE6_INTERSECTION, FileNameDef.PATH_ALLFEATURE_TS_INTERSECTION, FileNameDef.PATH_COMBINE_FEATURE_INTERSECTION)
    pass
