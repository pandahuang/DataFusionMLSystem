import os

from Data import FileNameDef
from Preprocess import DataFormatting
from Preprocess import DataLabelling
from Preprocess import PredictSetSelection
from Preprocess import TestSetSelection
from Preprocess import TrainSetSelection


def TrainDataConsistant(train_data):
    with open(FileNameDef.PATH_TRAIN_DATA, "w") as fopen:
        for data in train_data:
            fopen.write(data + "\n")

def TestDataConsistant(test_data):
    with open(FileNameDef.PATH_TEST_DATA, "w") as fopen:
        for data in test_data:
            fopen.write(data + "\n")

# def DataGeneration(path_good = FileNameDef.PATH_DATA_GOOD, path_bad = FileNameDef.PATH_DATA_BAD, path_feature = FileNameDef.PATH_COMBINE_FEATURE, train_good_num = 883, train_bad_num = 728, test_good_num = -588, test_bad_num = -486):

def DataGeneration(path_good=FileNameDef.PATH_DATA_GOOD, path_bad=FileNameDef.PATH_DATA_BAD,
                       path_feature=FileNameDef.PATH_COMBINE_FEATURE, train_good_num=713, train_bad_num=706,
                       test_good_num=-476, test_bad_num=-471):
    train_data_f = []
    test_data_f = []
    predict_data_f = []
    if not os.path.exists(FileNameDef.PATH_TRAIN_DATA):
        print "Co-TrainingMethods dataset initalization..."
        label_data_g, label_data_b = DataLabelling.Labelling(path_good, path_bad, path_feature)
        train_data = TrainSetSelection.TrainSetSelection(label_data_g, label_data_b, train_good_num, train_bad_num)
        test_data = TestSetSelection.TestSetSelection(label_data_g, label_data_b, test_good_num, test_bad_num)
        predict_data = PredictSetSelection.PredictSetSelection()
        print "Train data first consistant, Test data first consistant..."
        TrainDataConsistant(train_data)
        TestDataConsistant(test_data)

        train_data_f = DataFormatting.DataFormatting(train_data)
        test_data_f = DataFormatting.DataFormatting(test_data)
        predict_data_f = DataFormatting.DataFormatting(predict_data)
    else:
        print "Trainset and Testset is existing, loading data from local file..."
        with open(FileNameDef.PATH_TRAIN_DATA) as fopen1, open(FileNameDef.PATH_TEST_DATA) as fopen2:
            lines1 = fopen1.readlines()
            lines2 = fopen2.readlines()
            train_data = [line1.strip() for line1 in lines1]
            test_data = [line2.strip() for line2 in lines2]
            predict_data = PredictSetSelection.PredictSetSelection()
            import random
            random.shuffle(train_data)
            random.shuffle(test_data)
            train_data_f = DataFormatting.DataFormatting(train_data)
            test_data_f = DataFormatting.DataFormatting(test_data)
            predict_data_f = DataFormatting.DataFormatting(predict_data)
    return (train_data_f, test_data_f, predict_data_f)