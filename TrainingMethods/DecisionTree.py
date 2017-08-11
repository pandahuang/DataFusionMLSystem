from sklearn.tree import DecisionTreeClassifier

def DecisionTree(train_data, test_data, predict_data, feature_num, model):
    clf = DecisionTreeClassifier(max_depth=5)
    print "Decision Tree TrainingMethods..."
    if model == 1:
        proba_result, test_proba_result, accurance, precision, recall, F_Score, TP, importances = ModelOne(clf, train_data,
                                                                                              test_data, predict_data,
                                                                                              feature_num)
    elif model == 2:
        proba_result, test_proba_result, accurance, precision, recall, F_Score, TP, importances = ModelTwo(clf, train_data,
                                                                                              test_data, predict_data,
                                                                                              feature_num)
    elif model == 3:
        proba_result, test_proba_result, accurance, precision, recall, F_Score, TP, importances = ModelThree(clf, train_data,
                                                                                                test_data, predict_data,
                                                                                                feature_num)

    return proba_result, test_proba_result, accurance, precision, recall, F_Score, TP, importances

def ModelOne(clf, train_data, test_data, predict_data, feature_num):
    clf = clf.fit([data[:feature_num] for data in train_data], [data[-2] for data in train_data])
    importances = 0.0
    result = clf.predict([data[:feature_num] for data in test_data])
    test_proba_result = clf.predict_proba([data[:feature_num] for data in test_data])
    from Resanalysis import ResultValidation
    accurance, precision, recall, F_Score, TP = ResultValidation.Validate(result, test_data)
    proba_result = clf.predict_proba([data[:feature_num] for data in predict_data])
    return proba_result, test_proba_result, accurance, precision, recall, F_Score, TP, importances

def ModelTwo(clf, train_data, test_data, predict_data, feature_num):
    clf = clf.fit([data[feature_num:-2] for data in train_data], [data[-2] for data in train_data])
    importances = 0.0
    result = clf.predict([data[feature_num:-2] for data in test_data])
    test_proba_result = clf.predict_proba([data[feature_num:-2] for data in test_data])
    from Resanalysis import ResultValidation
    accurance, precision, recall, F_Score, TP = ResultValidation.Validate(result, test_data)
    proba_result = clf.predict_proba([data[feature_num:-1] for data in predict_data])
    return proba_result, test_proba_result, accurance, precision, recall, F_Score, TP, importances

def ModelThree(clf, train_data, test_data, predict_data, feature_num):
    clf = clf.fit([data[:-2] for data in train_data], [data[-2] for data in train_data])
    importances = 0.0
    result = clf.predict([data[:-2] for data in test_data])
    test_proba_result = clf.predict_proba([data[:-2] for data in test_data])
    from Resanalysis import ResultValidation
    accurance, precision, recall, F_Score, TP = ResultValidation.Validate(result, test_data)
    proba_result = clf.predict_proba([data[:-1] for data in predict_data])
    return proba_result, test_proba_result, accurance, precision, recall, F_Score, TP, importances