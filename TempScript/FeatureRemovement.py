def FeatureRemovement(path_old, path_new):
    with open(path_old) as fopen1, open(path_new, "w") as fopen2:
        lines1 = fopen1.readlines()
        lines2 = [line1.strip().split('\t')[0] for line1 in lines1]
        for line2 in lines2:
            fopen2.write(line2 + "\n")
        print len(lines2)

def BlackListFeatureRemovement1(path_old, path_new):
    with open(path_old) as fopen1, open(path_new, "w") as fopen2:
        lines1 = fopen1.readlines()
        lines2 = [line1.strip().split('\t')[0] for line1 in lines1]
        for line2 in lines2:
            fopen2.write(line2 + "\n")
        print len(lines2)

def BlackListFeatureRemovement2(path_old, path_new):
    with open(path_old) as fopen1, open(path_new, "w") as fopen2:
        lines1 = fopen1.readlines()
        lines2 = [line1.strip().split(' ')[1] for line1 in lines1]
        for line2 in lines2:
            fopen2.write(line2 + "\n")
        print len(lines2)

def BlackListCombination(path_dul, path):
    with open(path_dul) as fopen1, open(path, "w") as fopen2:
        lines1 = fopen1.readlines()
        lines2 = list(set([line1.strip() for line1 in lines1]))
        for line2 in lines2:
            fopen2.write(line2 + "\n")
        print len(lines1), len(lines2)
    pass

if __name__=="__main__":
    pass