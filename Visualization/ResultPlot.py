import matplotlib.pyplot as plt
# from Resanalysis import StatisticsOfResults

def ResultPlot(result_list, label):
    plt.plot(result_list)
    plt.xlabel("iteration time")
    plt.ylabel(label)
    plt.show()

def ResultPlotTogether(tc_result_list, af_result_list, label):
    plot1 = plt.plot(tc_result_list, 'r-.', linewidth=2)
    plot2 = plt.plot(af_result_list, 'y-', linewidth=2)
    plt.xlabel("iteration time")
    plt.ylabel(label)
    plt.show()

def ResultPlotSubgraph(result_lists):
    plt.figure(1)
    ax1 = plt.subplot(221)
    ax2 = plt.subplot(222)
    ax3 = plt.subplot(223)
    ax4 = plt.subplot(224)
    plt.sca(ax1)
    # plt.title("accurance")
    plt.plot(result_lists[0], 'g--', linewidth=2)
    plt.plot(result_lists[1], 'b:', linewidth=2)
    plt.xlabel("iteration time")
    plt.ylabel("accurance")
    plt.sca(ax2)
    # plt.title("precision")
    plt.plot(result_lists[2], 'g--', linewidth=2)
    plt.plot(result_lists[3], 'b:', linewidth=2)
    plt.xlabel("iteration time")
    plt.ylabel("precision")
    plt.sca(ax3)
    # plt.title("recall")
    plt.plot(result_lists[4], 'g--', linewidth=2)
    plt.plot(result_lists[5], 'b:', linewidth=2)
    plt.xlabel("iteration time")
    plt.ylabel("recall")
    plt.sca(ax4)
    # plt.title("f-score")
    plt.plot(result_lists[6], 'g--', linewidth=2)
    plt.plot(result_lists[7], 'b:', linewidth=2)
    plt.xlabel("iteration time")
    plt.ylabel("f-score")
    plt.show()
    pass

def ResultBarSubgraph(result_lists):
    plt.figure(1)
    ax1 = plt.subplot(221)
    ax2 = plt.subplot(222)
    ax3 = plt.subplot(223)
    ax4 = plt.subplot(224)
    plt.sca(ax1)
    plt.title("accurance")
    plt.bar([0.35], [StatisticsOfResults.CountAvg(result_lists[0])], width=0.1, facecolor='blue')
    plt.bar([0.5], [StatisticsOfResults.CountAvg(result_lists[1])], width=0.1, facecolor='green')
    plt.xticks([0.4, 0.55], ('af', 'co'))
    plt.xlim(0,1)
    plt.sca(ax2)
    plt.title("precision")
    plt.bar([0.35], [StatisticsOfResults.CountAvg(result_lists[2])], width=0.1, facecolor='blue')
    plt.bar([0.5], [StatisticsOfResults.CountAvg(result_lists[3])], width=0.1, facecolor='green')
    plt.xticks([0.4, 0.55], ('af', 'co'))
    plt.xlim(0, 1)
    plt.sca(ax3)
    plt.title("recall")
    plt.bar([0.35], [StatisticsOfResults.CountAvg(result_lists[4])], width=0.1, facecolor='blue')
    plt.bar([0.5], [StatisticsOfResults.CountAvg(result_lists[5])], width=0.1, facecolor='green')
    plt.xticks([0.4, 0.55], ('af', 'co'))
    plt.xlim(0, 1)
    plt.sca(ax4)
    plt.title("f-score")
    plt.bar([0.35], [StatisticsOfResults.CountAvg(result_lists[6])], width=0.1, facecolor='blue')
    plt.bar([0.5], [StatisticsOfResults.CountAvg(result_lists[7])], width=0.1, facecolor='green')
    plt.xticks([0.4, 0.55], ('af', 'co'))
    plt.xlim(0, 1)
    plt.show()
    pass

if __name__=="__main__":
    list1 = [135, 194, 203, 232, 256, 251, 265, 282, 295, 323, 333, 325, 321, 330, 309]
    list2 = [222, 223, 224, 226, 247, 237, 269, 259, 280, 266, 292, 287, 293, 289, 292]
    list3 = [199, 207, 218, 228, 236, 239, 270, 257, 275, 268, 292, 289, 289, 290, 293]

    iter1 = [0.80,0.80,0.80,0.80,0.80,0.80,0.80,0.80,0.80,0.802,0.802,0.802,0.802,0.802,
    0.802,0.802,0.802,0.802,0.802,0.802,0.8025,0.8025,0.8025,0.8025,0.8031,0.8031,0.8031,
    0.8031,0.807,0.807,0.807,0.807,0.807,0.8072,0.8072,0.8072,0.8096,0.811,0.811,0.811,0.811
    ,0.811,0.811,0.811,0.811,0.811,0.811,0.811,0.8142,0.8142,0.8142,0.8142,0.8142,0.8169,
    0.8169,0.8169,0.8169,0.8169,0.8169,0.818,0.818,0.818,0.818,0.818,0.818,0.818,0.818]
    iter2 = [0.768,0.768,0.768,0.768,0.768,0.768,0.768,0.768,0.768,0.768,0.768,0.768,0.769,
    0.769,0.769,0.769,0.769,0.769,0.769,0.771,0.771,0.771,0.771,0.774,0.774,0.774,0.7762,
    0.7762,0.7762,0.7762,0.779,0.779,0.779,0.779,0.779,0.779,0.779,0.779,0.779,0.779,0.779,
    0.779,0.779,0.7823,0.7823,0.7823,0.783,0.783,0.783,0.783,0.783,0.783,0.783,0.7864,0.7864,
    0.7864,0.7864,0.787,0.787,0.787,0.787,0.787,0.787,0.787,0.7886,0.7886,0.7886,0.7886,0.789,
    0.789,0.789,0.79,0.79,0.79,0.79,0.79,0.79,0.79,0.79,0.79]
    iter3 = [0.793,0.793,0.793,0.7965,0.7965,0.7965,0.7965,0.7965,0.799,0.799,0.799,0.799,0.806,
    0.806,0.806,0.806,0.806,0.806,0.806,0.806,0.807,0.8074,0.812,0.812,0.812,0.812,0.812,0.812,
    0.812,0.812,0.812,0.812,0.812,0.812,0.812,0.812,0.817,0.817,0.817,0.817,0.817,0.817,0.817,
    0.817,0.817,0.817,0.819,0.819,0.819,0.822,0.822,0.822,0.822,0.822,0.822,0.822,0.8236,0.8236,
    0.8236,0.8236,0.8236,0.8236,0.8236,0.830,0.830,0.830,0.830,0.830,0.8312,0.8312,0.8312,0.8312,0.832,0.832,0.832]

    # plot1 = plt.plot(iter1, 'r-.', linewidth=2,label='GB')
    # plot2 = plt.plot(iter2, 'b--', linewidth=2,label='KNN')
    # plot3 = plt.plot(iter3, 'g:', linewidth=2,label='DT')
    # plt.xlabel("iteration time")
    # plt.ylabel("accuracy")
    # plt.legend()
    # plt.show()

    iter4 = [0.796,0.796,0.796,0.796,0.796,0.7968,0.7968,0.7968,0.7968,0.7968,0.7968,0.798,0.798,
    0.798,0.798,0.798,0.798,0.798,0.798,0.798,0.798,0.798,0.7992,0.7992,0.7992,0.7992,0.802,0.802,
    0.802,0.802,0.802,0.802,0.802,0.807,0.807,0.807,0.807,0.815,0.815,0.815,0.815,0.8155,0.8155,
    0.8155,0.8155,0.818,0.818,0.818,0.818,0.818,0.818,0.8203,0.8203,0.8203,0.8203,0.8203,0.8203,
    0.8203,0.8203,0.8203,0.8215,0.8215,0.8215,0.8215,0.8215,0.8215,0.8215,0.8215,0.822,0.822,0.822,0.822,0.822,0.822,0.822,0.822,0.822,0.822,0.822,0.822,]
    print len(iter4)
    iter5 = [0.785,0.785,0.785,0.785,0.785,0.787,0.787,0.787,0.787,0.787,0.787,0.7886,0.7886,0.7886,
    0.7886,0.7886,0.7886,0.7886,0.792,0.792,0.792,0.792,0.792,0.792,0.792,0.792,0.792,0.7943,0.7943,
    0.7943,0.7943,0.7943,0.7943,0.7943,0.7943,0.7965,0.7965,0.7965,0.7965,0.7965,0.7965,0.7965,
    0.7965,0.80,0.80,0.80,0.80,0.80,0.80,0.80,0.80,0.80,0.80,0.8021,0.8021,0.8021,0.8021,0.8021,
    0.8021,0.8021,0.8045,0.8045,0.8045,0.8045,0.8045,0.806,0.806,0.806,0.806,0.806,0.809,0.809,0.809,0.809,0.809,0.809,0.809,0.809,0.809,0.809,]
    print len(iter5)
    iter6 = [0.79,0.79,0.79,0.79,0.79,0.79,0.79,0.79,0.79,0.7921,0.7921,0.7921,0.7921,0.7921,0.7921,
    0.7921,0.7921,0.7921,0.794,0.794,0.794,0.794,0.794,0.794,0.794,0.794,0.794,0.7972,0.7972,0.7972,
    0.7972,0.7972,0.7972,0.7972,0.7972,0.7972,0.7972,0.7972,0.7972,0.799,0.799,0.799,0.799,0.799,
    0.799,0.799,0.799,0.799,0.799,0.8025,0.8025,0.8025,0.8025,0.8025,0.8025,0.8025,0.8025,0.806,0.806,
    0.806,0.806,0.806,0.806,0.806,0.806,0.806,0.806,0.8082,0.8082,0.8082,0.81,0.81,0.81,0.81,0.81,0.81,0.81,0.81,0.81,0.81,]
    print len(iter6)

    plot4 = plt.plot(iter4, 'r-.', linewidth=2,label='KNN&GB')
    plot5 = plt.plot(iter5, 'g:', linewidth=2,label='DT&GB')
    plot6 = plt.plot(iter6, 'y--', linewidth=2, label='SVM&GB')
    plt.xlabel("iteration time")
    plt.ylabel("accuracy")
    plt.legend()
    plt.show()

    pass