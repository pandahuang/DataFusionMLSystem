from Data import FileNameDef

def PredictDataGeneration(path_feature = FileNameDef.PATH_FEATURE, path_combain_feature = FileNameDef.PATH_COMBINE_FEATURE, path_predict_data = FileNameDef.PATH_PREDICT_DATA):
    with open(path_feature) as fopen1, open(path_combain_feature) as fopen2, open(path_predict_data, "w") as fopen3:
        temp_dict = {}
        lines1 = fopen1.readlines()
        lines2 = fopen2.readlines()
        for line1 in lines1:
            temp_dict[line1.strip().split('\t')[0]] = 1
        for line2 in lines2:
            if temp_dict.has_key(line2.strip().split('\t')[0]):
                pass
            else:
                fopen3.write(line2.strip() + "\n")
    print "Predict Data Generation Done..."
    pass