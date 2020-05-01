# --** coding="UTF-8" **--

##############################
###     Coded by 番茄      ###
###    @ Summer Studio     ###
##############################


import os
import re
import sys
import shutil   # 文件拷贝模块


### Samba网盘同步 ###
def SyncSambaNetdisk(src_dir_base, dst_dir_base, sync_dir):
    print("Sync Dir >>> " + src_dir_base + sync_dir)

    src_dir_list = list()
    src_file_list = list()
    DirTraverser(src_dir_base, sync_dir, src_dir_list, src_file_list)

    sync_dir_list = list()
    DirComparer(dst_dir_base, src_dir_list, sync_dir_list)

    sync_file_list = list()
    FileComparer(dst_dir_base, src_file_list, sync_file_list)

    if len(sync_dir_list) == 0:
        if len(sync_file_list) == 0:
            print(">>> Dir List Synced : )")
            print(">>> File List Synced : )")
            print("")
            return

    if len(sync_dir_list) != 0:
        print(">>>>>>>>>><<<<<<<<<<<")
        print(">>> Sync Dir List <<<")
        print(">>>>>>>>>><<<<<<<<<<<")
        for dir_name in sync_dir_list:
            print(dir_name)

    if len(sync_file_list) != 0:
        print(">>>>>>>>>><<<<<<<<<<<")
        print(">>> Sync File List <<<")
        print(">>>>>>>>>><<<<<<<<<<<")
        for file_name in sync_file_list:
            print(file_name)

    if MakeDecision("同步") == "Y":
        if os.path.exists(dst_dir_base + sync_dir) == False:
            os.makedirs(dst_dir_base + sync_dir)
        for dir_name in sync_dir_list:
            os.makedirs(dst_dir_base + dir_name)
        for file_name in sync_file_list:
            #shutil.copyfile(filename, bkfilename)
            shutil.copy2(src_dir_base + file_name, dst_dir_base + file_name)
            print(file_name)
        
        print("")


### 文件夹逐层遍历 ###
def DirTraverser(src_dir_base, sync_dir, tv_dir_list, tv_file_list):
    src_base_len = len(src_dir_base)
    file_list = os.listdir(src_dir_base + sync_dir)
    for file in file_list:
        # 利用os.path.join()方法取得路径全名
        # 否则每次只能遍历一层目录 (?)
        full_path = os.path.join(src_dir_base + sync_dir, file)
        if os.path.isdir(full_path):
            sync_sub_dir = full_path[src_base_len:]
            tv_dir_list.append(sync_sub_dir)
            DirTraverser(src_dir_base, sync_sub_dir, tv_dir_list, tv_file_list)
        else:
            sync_file = full_path[src_base_len:]
            tv_file_list.append(sync_file)


### 文件夹 比对 ###
def DirComparer(dst_dir_base, src_dir_list, sync_dir_list):
    for dir_name in src_dir_list:
        dst_sub_dir = dst_dir_base + dir_name
        if os.path.exists(dst_sub_dir) == False:
            sync_dir_list.append(dir_name)


### 文件 比对 ###
def FileComparer(dst_dir_base, src_file_list, sync_file_list):
    for file_name in src_file_list:
        dst_file_name = dst_dir_base + file_name
        if os.path.exists(dst_file_name) == False:
            ffile_name = dst_file_name.split("\\")[-1]
            if ffile_name[0] != ".":
                sync_file_list.append(file_name)


### 确定是否进行批处理 ###
def MakeDecision(tips):
    print("")
    decision = input(">>> 确定" + tips + "？(Y/N): ")
    if decision == "Y":
        pass
    elif decision == "N":
        print("")
        print("------------------------------")
        print(">>> " + tips + "已取消 <<<")
        print("------------------------------")
        print("")
    else:
        print("")
        print("------------------------------")
        print(">>> 选择错误 ! <<<")
        print("------------------------------")
        print("")
    return decision


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
    print("Samba Sync System")
    print("Samba网盘同步助手")
    print("------------------------------")
    print("")

    src_dir_base = "\\\\192.168.11.1\\samba\\"
    dst_dir_base = "W:\\Bakup.Samba\\"

    sync_dir_list = list()
    sync_dir_list.append("AD.PornTuTu")
    sync_dir_list.append("AD.Kindle书屋")
    sync_dir_list.append("AD.iMagazine")
    sync_dir_list.append("2020.BOX.V")
    sync_dir_list.append("AD.强词有理-建筑300秒")

    for sync_dir in sync_dir_list:
        SyncSambaNetdisk(src_dir_base, dst_dir_base, sync_dir)

    print("")
    print("------------------------------")
    print("Samba Sync Success :)")
    print("------------------------------")
    print("")


#------------------------------#
#    River flows in summer     #
#------------------------------#
