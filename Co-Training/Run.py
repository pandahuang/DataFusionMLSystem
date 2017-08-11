import IsPredictEmpty
import LabelDataMoving
from Preprocess import DataGeneration
from Preprocess import PredictDataGeneration
from Resanalysis import CoTrainingValidation, HistoryResultStorage
from TrainingMethods import GradientBoosting, RandomForest, SVM, KNN, DecisionTree
from Visualization import ResultPlot

if __name__=="__main__":
    PredictDataGeneration.PredictDataGeneration()
    import os
    from Data import FileNameDef
    if os.path.exists(FileNameDef.PATH_TRAIN_DATA):
        os.remove(FileNameDef.PATH_TRAIN_DATA)
    if os.path.exists(FileNameDef.PATH_TEST_DATA):
        os.remove(FileNameDef.PATH_TEST_DATA)

    feature_num = 9
    threshold = 50
    iter_num = 0
    add_num = 0

    tc_accurance_list = []
    tc_precision_list = []
    tc_recall_list = []
    tc_f_score_list = []
    tc_tp_list = []
    tc_feature_imporatnce = []
    ts_accurance_list = []
    ts_precision_list = []
    ts_recall_list = []
    ts_f_score_list = []
    ts_tp_list = []
    ts_feature_imporatnce = []
    af_accurance_list = []
    af_precision_list = []
    af_recall_list = []
    af_f_score_list = []
    af_tp_list = []
    af_feature_imporatnce = []
    co_accurance_list = []
    co_precision_list = []
    co_recall_list = []
    co_f_score_list = []
    co_tp_list = []

    while(1):
        iter_num += 1
        if iter_num == 1:
            print "Co-Training Starting..."
        if IsPredictEmpty.IsPredictEmpty() == False and iter_num <= threshold:
            print "The %dth Iteration..."%(iter_num)
            train_data, test_data, predict_data = DataGeneration.DataGeneration()

            proba_result_tc, test_proba_result_tc, accurance_tc, precision_tc, recall_tc, f_score_tc, tp_tc, importances_tc = DecisionTree.DecisionTree(
                train_data, test_data, predict_data, feature_num, 1)
            proba_result_ts, test_proba_result_ts, accurance_ts, precision_ts, recall_ts, f_score_ts, tp_ts, importances_ts = KNN.KNN(
                train_data, test_data, predict_data, feature_num, 2)
            proba_result_af, test_proba_result_af, accurance_af, precision_af, recall_af, f_score_af, tp_af, importances_af = KNN.KNN(
                train_data, test_data, predict_data, feature_num, 3)

            print "Co-Training Validation Result..."
            accurance_co, precision_co, recall_co, f_score_co, tp_co = CoTrainingValidation.CoTrainingValidate(
                test_proba_result_tc, test_proba_result_ts, test_data)

            tc_accurance_list.append(accurance_tc)
            tc_f_score_list.append(f_score_tc)
            ts_accurance_list.append(accurance_ts)
            ts_f_score_list.append(f_score_ts)
            af_accurance_list.append(accurance_af)
            af_precision_list.append(precision_af)
            af_recall_list.append(recall_af)
            af_f_score_list.append(f_score_af)
            af_tp_list.append(tp_af)
            co_accurance_list.append(accurance_co)
            co_precision_list.append(precision_co)
            co_recall_list.append(recall_co)
            co_f_score_list.append(f_score_co)
            co_tp_list.append(tp_co)

            if iter_num == 1:
                add_num = LabelDataMoving.DataMoving(predict_data, proba_result_tc, proba_result_ts, 100, 100)

            if iter_num >= 2:
                if accurance_co >= co_accurance_list[-2]:
                    add_num = LabelDataMoving.DataMoving(predict_data, proba_result_tc, proba_result_ts, 100, 100)
                elif accurance_co < co_accurance_list[-2]:
                    if add_num > 0:
                        LabelDataMoving.DataRemovement(add_num)
                    af_accurance_list.pop()
                    af_precision_list.pop()
                    af_recall_list.pop()
                    af_f_score_list.pop()
                    af_tp_list.pop()
                    co_accurance_list.pop()
                    co_precision_list.pop()
                    co_recall_list.pop()
                    co_f_score_list.pop()
                    co_tp_list.pop()
                    add_num = 0

        elif IsPredictEmpty.IsPredictEmpty() == True:
            print "Predict Data is empty, Co-Training Finish..."
            break
        elif iter_num > threshold:
            print "Iteration times are out of threshold(%d), Co-Training Stop..."%(threshold)
            break

    HistoryResultStorage.HistoryResultStorage(
        [tc_accurance_list, tc_f_score_list, ts_accurance_list, ts_f_score_list, af_accurance_list, af_precision_list,
         af_recall_list, af_f_score_list, co_accurance_list, co_precision_list, co_recall_list, co_f_score_list])

    # print af_feature_imporatnce
    plot_lists = [af_accurance_list, co_accurance_list, af_precision_list, co_precision_list, af_recall_list, co_recall_list,
                 af_f_score_list, co_f_score_list]
    ResultPlot.ResultPlotSubgraph(plot_lists)

    ResultPlot.ResultBarSubgraph(plot_lists)
    # ResultPlot.ResultPlotTogether(tc_accurance_list, af_accurance_list, "accurance")
    # ResultPlot.ResultPlotTogether(ts_accurance_list, af_accurance_list, "accurance")
    # ResultPlot.ResultPlotTogether(tc_f_score_list, af_f_score_list, "f-score")
    # ResultPlot.ResultPlotTogether(ts_f_score_list, af_f_score_list, "f-score")

    pass