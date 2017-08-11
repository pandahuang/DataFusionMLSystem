from Data import FileNameDef

def IsPredictEmpty(path_predict_data = FileNameDef.PATH_PREDICT_DATA):
    is_empty = False
    with open(path_predict_data) as fopen:
        lines = fopen.readlines()
        if len(lines) == 0 or lines[0] == "":
            is_empty = True
    return is_empty

