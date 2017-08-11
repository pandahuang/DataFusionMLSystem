from Data import FileNameDef
def HistoryResultStorage(result_lists, path=FileNameDef.PATH_RESULTS_RECORD):
    with open(path, "a") as fopen:
        for list in result_lists:
            fopen.write(repr(list) + "\n")
        fopen.write("==========================================================="+"\n")
    print "Result Storage Done..."