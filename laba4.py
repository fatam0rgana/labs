import pandas as pd
import os
from datetime import datetime
import urllib.request as ur

PART = "C:\\Users\\ogur4\\PycharmProjects\\untitled6\\"

def download(pId, y1, y2):
    now = datetime.now()
    o = str(pId)
    name = "_" + o + "_" + datetime.strftime(datetime.now(), "%Y.%m.%d_%H-%M-%S")
    name = name + "_" + str(y1) + "-" + str(y2) + ".csv"
    s = ur.urlopen("https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID=" + pId + "&year1=" + str(y1) + "&year2=" + str(y2) + "&type=Mean")
    s1 = open(name, 'wb')
    s1.write(s.read())

    s1 = open(name,'r+')
    d = s1.readlines()
    s1.seek(0)
    for i in d:
        if i == d[0]:
            t = 0
            while t < i.find("year"):
                i = i[:t] + " " + i[t + 1:]
                t = t + 1
            i = i.replace(' ', '')
            i = i.replace("provinceID,",'')

        i = i.replace("  "," ")
        i = i.replace(" ",",")
        i = i.replace(",,",",")
        if i != d[len(d)-1]:
            s1.write(i)

    s1.truncate()
    s1.close()

    return name



def download_all():
    os.chdir('data')
    name_O = [download(1, "2000", "2001")]
    for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
        name_O.extend(download(i, "1995", "2017"))
    os.chdir(PART)

def us_swap(i):
    if i == 1:
        return 24
    if i == 2:
        return 25
    if i == 3:
        return 5
    if i == 4:
        return 6
    if i == 5:
        return 27
    if i == 6:
        return 25
    if i == 7:
        return 25
    if i == 8:
        return 26
    if i == 9:
        return 25

def read_pId(i):
    i="_"+str(i)
    csv_files = [f for f in os.listdir("data") if f.endswith('.csv') & f.endswith(i,0,len(i))]
    return csv_files


def new_fr(f):
    files = read_pId(5)
    print(PART+files[0])
    df = pd.read_csv(PART+"data\\"+files[0],index_col=False, header=0)
    return df



print(min(new_fr(read_pId(5))["VHI"]))

