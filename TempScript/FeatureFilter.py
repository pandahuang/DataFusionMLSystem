from Data import FileNameDef

def FeatureFilter(path_feature_old, path_feature_new, filter_pos):
    with open(path_feature_old) as fopen1, open(path_feature_new, "w") as fopen2:
        lines1 = fopen1.readlines()
        for line1 in lines1:
            features = line1.strip().split('\t')
            for f_pos in filter_pos:
                features.pop(f_pos)
            features_string = ""
            for pos in range(len(features)):
                if pos == 0:
                    features_string = features[pos]
                else:
                    features_string = features_string + "\t" + features[pos]
            fopen2.write(features_string + "\n")
    print "Feature Filtering Done..."

if __name__=="__main__":
    pass