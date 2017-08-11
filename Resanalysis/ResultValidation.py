def Validate(result, test_data):
    TP = 0
    FP = 0
    FN = 0
    AR = 0
    F_Score = 0
    label_list = [data[-2] for data in test_data]
    for (data, res) in zip(label_list, result):
        if data == res:
            AR += 1
        if data == 1 and res == 1:
            TP += 1
        if data == 0 and res == 1:
            FP += 1
        if data == 1 and res == 0:
            FN += 1
    accurance = float(AR) / len(test_data)
    print "The accurance is %f" % (float(accurance))

    print "TotalRight:%d, TP:%d, FP:%d, FN:%d" % (AR, TP, FP, FN)

    if TP + FP > 0:
        precision = float(TP) / (TP + FP)
        print "The precision is %f" % (precision)
    if TP + FN > 0:
        recall = float(TP) / (TP + FN)
        print "The recall is %f" % (recall)
    if (precision + recall) == 0:
        F_Score = 0
    else:
        F_Score = (2*precision*recall)/(precision + recall)
    return accurance, precision, recall, F_Score, TP