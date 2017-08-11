from sklearn.ensemble import VotingClassifier
from sklearn.neighbors  import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


def Voting(train_data, test_data, predict_data, feature_num, model):
    clf1 = DecisionTreeClassifier(max_depth=9)
    clf2 = KNeighborsClassifier(n_neighbors=7)
    clf3 = SVC(kernel='rbf', probability=True)
    eclf = VotingClassifier(estimators=[('dt', clf1), ('knn', clf2), ('svc', clf3)], voting='soft')
    print "Voting TrainingMethods..."
    if model == 1:
        proba_result, test_proba_result, accurance, precision, recall, F_Score, TP = ModelOne(eclf, train_data,
                                                                                              test_data, predict_data,
                                                                                              feature_num)
    elif model == 2:
        proba_result, test_proba_result, accurance, precision, recall, F_Score, TP = ModelTwo(eclf, train_data,
                                                                                              test_data, predict_data,
                                                                                              feature_num)
    elif model == 3:
        proba_result, test_proba_result, accurance, precision, recall, F_Score, TP = ModelThree(eclf, train_data,
                                                                                                test_data, predict_data,
                                                                                                feature_num)

    return proba_result, test_proba_result, accurance, precision, recall, F_Score, TP

def ModelOne(clf, train_data, test_data, predict_data, feature_num):
    clf = clf.fit([data[:feature_num] for data in train_data], [data[-2] for data in train_data])
    result = clf.predict([data[:feature_num] for data in test_data])
    test_proba_result = clf.predict_proba([data[:feature_num] for data in test_data])
    from Resanalysis import ResultValidation
    accurance, precision, recall, F_Score, TP = ResultValidation.Validate(result, test_data)
    proba_result = clf.predict_proba([data[:feature_num] for data in predict_data])
    return proba_result, test_proba_result, accurance, precision, recall, F_Score, TP

def ModelTwo(clf, train_data, test_data, predict_data, feature_num):
    clf = clf.fit([data[feature_num:-2] for data in train_data], [data[-2] for data in train_data])
    result = clf.predict([data[feature_num:-2] for data in test_data])
    test_proba_result = clf.predict_proba([data[feature_num:-2] for data in test_data])
    from Resanalysis import ResultValidation
    accurance, precision, recall, F_Score, TP = ResultValidation.Validate(result, test_data)
    proba_result = clf.predict_proba([data[feature_num:-1] for data in predict_data])
    return proba_result, test_proba_result, accurance, precision, recall, F_Score, TP

def ModelThree(clf, train_data, test_data, predict_data, feature_num):
    clf = clf.fit([data[:-2] for data in train_data], [data[-2] for data in train_data])
    result = clf.predict([data[:-2] for data in test_data])
    test_proba_result = clf.predict_proba([data[:-2] for data in test_data])
    from Resanalysis import ResultValidation
    accurance, precision, recall, F_Score, TP = ResultValidation.Validate(result, test_data)
    proba_result = clf.predict_proba([data[:-1] for data in predict_data])
    return proba_result, test_proba_result, accurance, precision, recall, F_Score, TP