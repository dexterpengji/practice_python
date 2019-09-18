# Use mac/ubuntu to run this script

import os
import matplotlib.pyplot as plt
import numpy as np


# get a sentence from a line of whole source text
def getSentence(singleLine, beg):
    index_begin = singleLine.find(beg)
    if index_begin is not -1:
        # cut to get raw sentence
        sentence_raw = single_line[index_begin + l_sub_beg:-5]
        # remove redundant punctuations
        sentence_ret = sentence_raw.replace(",", " ")
        sentence_ret = sentence_ret.replace(".", " ")
        sentence_ret = sentence_ret.replace("?", " ")
        sentence_ret = sentence_ret.replace("\"", " ")
        sentence_ret = sentence_ret.replace(":", " ")
        sentence_ret = sentence_ret.replace("-", " ")
        sentence_ret = sentence_ret.replace("!", " ")
        return sentence_ret
    else:
        return None


if __name__ == "__main__":
    # var settings
    path_source = 'source/'
    sub_beg_all = "{\\fnTahoma\\fs11\\bord1\\shad1\\1c&HC0C0C0&\\b0}"
    sub_beg = "{\\fnTahoma"
    l_sub_beg = len(sub_beg_all)
    dic = {}
    error_decode = []

    # get the list of file names
    fileList = os.listdir(path_source)
    fileList.sort()

    # get the words from all files
    for x in fileList:
        # read single file
        print("processing file: %s" % x)
        if x[0] != "S":
            print("skip file: %s" % x)
            continue
        with open(path_source + os.sep + x, mode="r+") as file:
            try:
                content_fulltext = file.readlines()
            except UnicodeDecodeError:
                error_decode.append(x)
                continue

        # get valid sentences as a list
        for single_line in content_fulltext:
            sentence_got = getSentence(single_line, sub_beg)
            if sentence_got:
                for single_word in sentence_got.split(" "):
                    if len(single_word) != 0:
                        single_word = single_word.lower()
                        try:
                            dic[single_word] += 1
                        except KeyError:
                            dic[single_word] = 1
        print(dic)

    # print report
    print("")
    print("==== decode error ====")
    print(error_decode)

    print("")
    print("==== sorted ====")
    sorted_list = sorted(dic.items(), key=lambda obj: obj[1])
    print(sorted_list[::-1])

    print("")
    print("==== 100 most popular words ====")

    # start to plot
    Xs = []
    Ys = []
    TextPlt = []
    for i in range(100):
        print(sorted_list[-i-1])
        TextPlt.append(sorted_list[-i-1][0])
        Xs.append(i)
        Ys.append(sorted_list[-i - 1][1])
    print(len(Xs))
    print(len(Ys))

    plt.figure(figsize=(10, 30))

    plt.ylim(-1, 100)
    plt.yticks(())
    plt.xlim(0, 25000)
    plt.xticks(())

    plt.barh(Xs, Ys[::-1], facecolor='#9999ff', edgecolor='gray')

    for y, x, t in zip(Ys[::-1], Xs, TextPlt[::-1]):
        # ha: horizontal alignment
        # va: vertical alignment
        # plot numbers
        plt.text(y, x, "  " + str(y), ha='left', va='center', color="#555555")
        # plot words
        plt.text(0, x, t + "  ", ha='right', va='center', color="#333333")

    plt.title('100 most popular words in Friends', loc='center', fontsize='10', fontweight='bold', color='gray')
    plt.savefig("result.png", dpi=300)
