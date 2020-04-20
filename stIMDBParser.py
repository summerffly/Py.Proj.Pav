# --** coding="UTF-8" **--

##############################
###     Coded by 番茄      ###
###    @ Summer Studio     ###
##############################


import os
import re
import sys


### 确定是否批处理修改 ###
def MakeDecision():
    decision = input("确定更改？(Y/N): ")
    if decision == "Y":
        return 'Y'
    elif decision == "N":
        print("")
        print("------------------------------")
        print(">>> 更改已取消 <<<")
        print("------------------------------")
        print("")
        #exit()
    else:
        print("")
        print("------------------------------")
        print(">>> Select Error !!! <<<")
        print("------------------------------")
        print("")
        #exit()


### 批处理增加剧集名 ###
def PatchAddPrefix(filepath, epname):
    filenames = os.listdir(filepath)
    epindex = 0
    #epindex = 1
    for filename in filenames:
        #if epindex < 13:
        #    epindex = epindex + 1
        #    continue
        filenameFULL = filename[:-4] + epname[epindex] + filename[-4:]
        epindex = epindex + 1
        print(filename, end="")   # 输出不换行
        print(" ==> ", end="")
        print(filenameFULL)
    if MakeDecision() == "Y":
        epindex = 0
        #epindex = 1
        for filename in filenames:
            #if epindex < 13:
            #    epindex = epindex + 1
            #    continue
            filenameFULL = filename[:-4] + epname[epindex] + filename[-4:]
            epindex = epindex + 1
            os.rename(filepath + "\\" + filename, filepath + "\\" + filenameFULL)


###############################
#     MAIN FUNCTION ENTRY     #
###############################
if __name__ == "__main__":

    print("\n--------------------------------")
    print("***   IMDB Episode Parser    ***")
    print("--------------------------------\n")
    # 数据源于IMDB库

    EPflag = 0

    EPnum = []
    EPname = []
    EPfull = []
    
    file = open(sys.argv[1],'rb')
    for line in file:
        matchObj = re.search(r'(ref_=ttep_(ep(\d)*)")', line.decode('utf-8'))
        if matchObj:
            if len(EPnum) == 0 or EPnum[-1] != matchObj.group(2):
                EPnum.append(matchObj.group(2))
                EPfull.append(matchObj.group(2))
                EPflag = 1
            else:
                pass
        elif EPflag == 1:
            mmatchObj = re.search(r'title=\"(.*)\" itemprop=\"', line.decode('utf-8'))
            EPname.append(mmatchObj.group(1))
            EPfull[-1] = EPfull[-1] + ' - ' + mmatchObj.group(1)
            EPflag = 0
        else:
            pass

    for obj in EPfull:
        print(obj)

    file.close()

    print("\n-----------------------------")
    print("-   IMDB Parse Success :)   -")
    print("-----------------------------\n")

    PatchAddPrefix(sys.argv[2], EPname)

    print("\n-------------------------------")
    print("-  IMDB EP Modify Success :)  -")
    print("-------------------------------\n")


#------------------------------#
#    River flows in summer     #
#------------------------------#
