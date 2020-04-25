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
        return decision
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
    return decision


### 遍历文件列表 ###
def ShowFileList(filepath):
    filenames = os.listdir(filepath)
    for filename in filenames:
        print(filename)


### 批处理增加前缀 ###
def PatchAddPrefix(filepath, aprefix):
    filenames = os.listdir(filepath)
    for filename in filenames:
        filenameA = aprefix + filename
        print(filename, end="")   # 输出不换行
        print(" ==> ", end="")
        print(filenameA)
    if MakeDecision() == "Y":
        for filename in filenames:
            filenameA = aprefix + filename
            os.rename(filepath + "\\" + filename, filepath + "\\" + filenameA)


### 批处理删除字符串 ###
def PatchDeleteSubText(filepath, dsubtext):
    filenames = os.listdir(filepath)
    for filename in filenames:
        filenameD  = re.sub(dsubtext, "", filename)
        print(filename, end="")
        print(" ==> ", end="")
        print(filenameD)
    if MakeDecision() == "Y":
        for filename in filenames:
            filenameD  = re.sub(dsubtext, "", filename)
            os.rename(filepath + "\\" + filename, filepath + "\\" + filenameD)


### 批处理插入字符串 ###
def PatchInsertSubText(filepath, segnum, isubtext):
    filenames = os.listdir(filepath)
    for filename in filenames:
        filenameF = filename[0:segnum]
        filenameP = filename[segnum:]
        filenameI = filenameF + isubtext + filenameP
        print(filename, end="")
        print(" ==> ", end="")
        print(filenameI)
    if MakeDecision() == "Y":
        for filename in filenames:
            filenameF = filename[0:segnum]
            filenameP = filename[segnum:]
            filenameI = filenameF + isubtext + filenameP
            os.rename(filepath + "\\" + filename, filepath + "\\" + filenameI)


### 批处理替换字符串 ###
def PatchReplace(filepath, origintext, repalcetext):
    filenames = os.listdir(filepath)
    for filename in filenames:
        filenameRP  = re.sub(origintext, repalcetext, filename)
        print(filename, end="")
        print(" ==> ", end="")
        print(filenameRP)
        #os.rename(filepath + "\\" + filename, filepath + "\\" + filenameRP)
    if MakeDecision() == "Y":
        for filename in filenames:
            filenameRP  = re.sub(origintext, repalcetext, filename)
            os.rename(filepath + "\\" + filename, filepath + "\\" + filenameRP)


### 批处理切割字符前段 ###
def PatchCutFrontSegment(filepath, segnum):
    filenames = os.listdir(filepath)
    for filename in filenames:
        filenameC = filename[segnum:]
        print(filename, end="")
        print(" ==> ", end="")
        print(filenameC)
    if MakeDecision() == "Y":
        for filename in filenames:
            filenameC  = filename[segnum:]
            os.rename(filepath + "\\" + filename, filepath + "\\" + filenameC)


### 批处理切割字符后段 ###
def PatchCutPostSegment(filepath, segnum):
    filenames = os.listdir(filepath)
    for filename in filenames:
        subtext = filename[-4-segnum:-4]
        filenameC  = re.sub(subtext, "", filename)
        print(filename, end="")
        print(" ==> ", end="")
        print(filenameC)
    if MakeDecision() == "Y":
        for filename in filenames:
            subtext = filename[-4-segnum:-4]
            filenameC  = re.sub(subtext, "", filename)
            os.rename(filepath + "\\" + filename, filepath + "\\" + filenameC)


### 批处理匹配剧集名称 ###
def PatchMatchEpisodeTXT(file_path, ep_txt_path):
    file_list = os.listdir(file_path)
    for file_name in file_list:
        file_match = SingleMatchEpisodeTXT(file_name, ep_txt_path)
        if file_match:
            print(file_name[0:-4] + ' - ' + file_match)
    if MakeDecision() == "Y":
        for file_name in file_list:
            file_match  = SingleMatchEpisodeTXT(file_name, ep_txt_path)
            if file_match:
                new_file_name = file_name[0:-4] + ' - ' + file_match + file_name[-4:]
                print(new_file_name)
                os.rename(file_path + "\\" + file_name, file_path + "\\" + new_file_name)


### 匹配单集剧集名称 ###
### 不能循环嵌套 内层只执行一次 ###
def SingleMatchEpisodeTXT(file_name, ep_txt_path):
    ep_txt_file = open(ep_txt_path, encoding="utf-8")
    file_name_npf = file_name[0:-4]
    for lines in ep_txt_file:
        matchObj = re.search(file_name_npf, lines[0:9])
        if matchObj:
            return lines[9:-1]


### 批处理Clean MacOS ###
def PatchCleanMacOS(filepath):
    filenames = list()
    DirTraverser(filepath, filenames)
    for filename in filenames:
        print(filename)
    if MakeDecision() == "Y":
        for filename in filenames:
            os.remove(filename)


def DirTraverser(filepath, tvfilelist):
    filelist = os.listdir(filepath)
    for file in filelist:
        # 利用os.path.join()方法取得路径全名
        # 否则每次只能遍历一层目录
        fullpath = os.path.join(filepath, file)
        if os.path.isdir(fullpath):
            DirTraverser(fullpath, tvfilelist)
        else:
            if file[0] == ".":
                tvfilelist.append(fullpath)
    #return all_files


###############################
#     MAIN FUNCTION ENTRY     #
###############################
if __name__ == "__main__":
    '''
    if len(sys.argv) == 1:
        print(sys.argv[0])
    elif len(sys.argv) == 2:
        print(sys.argv[1])
    '''

    print("------------------------------")
    print("Patch Rename System")
    print("文件名修改批处理系统")
    print("------------------------------")
    
    filepath = input("输入文件夹路径: ")
    ShowFileList(filepath)
    
    loopflag = 1
    while loopflag == 1:
        print("-----------------------------------")
        print("Mode A >>> 批处理增加前缀")
        print("Mode D >>> 批处理删除字符串")
        print("Mode I >>> 批处理插入字符串")
        print("Mode R >>> 批处理替换字符串")
        print("Mode CF >>> 批处理切割字符前端")
        print("Mode CP >>> 批处理切割字符后端")
        print("Mode MATCH >>> 批处理匹配文件名称")
        print("Mode CMOS >>> 批处理Clean MacOS")
        print("-----------------------------------")
    
        prMode = input("选择批处理Mode: ")
        if prMode == "A":
            aprefix = input("输入增加前缀: ")
            PatchAddPrefix(filepath, aprefix)
        elif prMode == "D":
            dsubtext = input("输入删除字符串: ")
            PatchDeleteSubText(filepath, dsubtext)
        elif prMode == "I":
            segnum = int(input("输入插入字符段标: "))
            isubtext = input("输入插入字符串: ")
            PatchInsertSubText(filepath, segnum, isubtext)
        elif prMode == "R":
            origintext = input("输入被替换字符串: ")
            repalcetext = input("输入替换字符串: ")
            PatchReplace(filepath, origintext, repalcetext)
        elif prMode == "CF":
            segnum = int(input("输入截断字符前段标: "))
            PatchCutFrontSegment(filepath, segnum)
        elif prMode == "CP":
            segnum = int(input("输入截断字符后段标: "))
            PatchCutPostSegment(filepath, segnum)
        elif prMode == "MATCH":
            ep_txt_path = input("输入TXT文本路径: ")
            PatchMatchEpisodeTXT(filepath, ep_txt_path)
        elif prMode == "CMOS":
            PatchCleanMacOS(filepath)
        elif prMode == "exit":
            print("")
            print("------------------------------")
            print(">>> PR System Shutdown <<<")
            print("------------------------------")
            print("")
            exit()
        else:
            print("")
            print(">>> Mode Error !!! <<<")
            print("")
            continue

        print("")
        print("------------------------------")
        print("PR Success :)")
        print("------------------------------")
        print("")
