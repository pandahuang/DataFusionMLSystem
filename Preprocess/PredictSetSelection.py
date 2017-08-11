from Data import FileNameDef

def PredictSetSelection(path_predict_data = FileNameDef.PATH_PREDICT_DATA):
    predict_data = []
    with open(path_predict_data) as fopen:
        lines = fopen.readlines()
        for line in lines:
            predict_data.append(line.strip())
    return predict_data