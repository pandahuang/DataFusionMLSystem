import os
PATH_CURRENT = "E:\\Projects\\DataFusionMLSystem\\Data"

PATH_DATA_GOOD = os.path.join(PATH_CURRENT, "tcp-dip-good-1189.txt")#use
PATH_DATA_BAD = os.path.join(PATH_CURRENT, "tcp-dip-bad-1177.txt")#use
PATH_FEATURE = os.path.join(PATH_CURRENT, "tcp-dip-good-and-bad.txt")#use

PATH_ALLFEATURE6 = os.path.join(PATH_CURRENT, "http-dip-all-6f.txt")
PATH_ALLFEATURE6_TCP = os.path.join(PATH_CURRENT, "tcp-dip-all-6f.txt")
PATH_ALLFEATURE6_INTERSECTION = os.path.join(PATH_CURRENT, "intersection-dip-all-6f.txt")

PATH_ALLFEATURE_TS = os.path.join(PATH_CURRENT, "http-dip-all-ts.txt")
PATH_ALLFEATURE_TS_TCP = os.path.join(PATH_CURRENT, "tcp-dip-all-ts.txt")
PATH_ALLFEATURE_TS_INTERSECTION = os.path.join(PATH_CURRENT, "intersection-dip-all-ts.txt")

PATH_COMBINE_FEATURE = os.path.join(PATH_CURRENT, "intersection-dip-all-combinef.txt")#use
PATH_COMBINE_FEATURE_TCP = os.path.join(PATH_CURRENT, "tcp-dip-all-combinef.txt")
PATH_COMBINE_FEATURE_INTERSECTION = os.path.join(PATH_CURRENT, "intersection-dip-all-combinef.txt")

PATH_LABELED_DATA_GOOD = os.path.join(PATH_CURRENT, "intersection-dip-labeled-data-good.txt")#use
PATH_LABELED_DATA_BAD = os.path.join(PATH_CURRENT, "intersection-dip-labeled-data-bad.txt")#use

PATH_TRAIN_DATA = os.path.join(PATH_CURRENT, "intersection-dip-train-data.txt")#use
PATH_TEST_DATA = os.path.join(PATH_CURRENT, "intersection-dip-test-data.txt")#use

PATH_PREDICT_DATA = os.path.join(PATH_CURRENT, "intersection-dip-predict-data.txt")#use

PATH_RESULTS_RECORD = "E:\\Projects\\DataFusionMLSystem\\Resanalysis\\history-result-record.txt"