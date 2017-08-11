def DataFormatting(data_list):
    data_list_float = []
    for data in data_list:
        float_list = [float(item) for item in data.strip().split('\t')[1:]]
        float_list.append(data.strip().split('\t')[0])
        data_list_float.append(float_list)
    return data_list_float
