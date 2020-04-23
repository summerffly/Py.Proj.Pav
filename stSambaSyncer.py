# --** coding="UTF-8" **--

##############################
###     Coded by 番茄      ###
###    @ Summer Studio     ###
##############################


import os
import re
import sys
import shutil


### 确定是否批处理修改 ###
def MakeDecision():
    print("")
    decision = input(">>> 确定同步？(Y/N): ")
    if decision == "Y":
        pass
    elif decision == "N":
        print("")
        print("------------------------------")
        print(">>> 同步已取消 <<<")
        print("------------------------------")
        print("")
    else:
        print("")
        print("------------------------------")
        print(">>> 选择错误 ! <<<")
        print("------------------------------")
        print("")
    return decision


### Samba网盘同步 ###
def SyncSambaNetdisk(src_dir_path, dst_dir_path):
    dir_list = list()
    file_list = list()
    DirTraverser(src_dir_path, dir_list, file_list)
    print("Path >>> " + src_dir_path)

    dst_dir_list = list()
    DirComparer(src_dir_path, dst_dir_path, dir_list, dst_dir_list)
    dst_file_list = list()
    FileComparer(src_dir_path, dst_dir_path, file_list, dst_file_list)

    if len(dst_dir_list) == 0:
        if len(dst_file_list) == 0:
            print(">>> Dir List Synced : )")
            print(">>> File List Synced : )")
            print("")
            return

    if len(dst_dir_list) != 0:
        print(">>>>>>>>>><<<<<<<<<<<")
        print(">>> Sync Dir List <<<")
        print(">>>>>>>>>><<<<<<<<<<<")
        for dir_name in dst_dir_list:
            print(dir_name)

    if len(dst_file_list) != 0:
        print(">>>>>>>>>><<<<<<<<<<<")
        print(">>> Sync File List <<<")
        print(">>>>>>>>>><<<<<<<<<<<")
        for file_name in dst_file_list:
            print(file_name)

    if MakeDecision() == "Y":
        if os.path.exists(dst_dir_path) == False:
            os.makedirs(dst_dir_path)
        for dir_name in dst_dir_list:
            os.makedirs(dir_name)
        for file_name in file_list:
            #shutil.copyfile(filename, bkfilename)
            #shutil.copy2(filename, dstdirpath)
            dir_len = len(src_dir_path)
            src_parent_path = os.path.dirname(file_name)
            dst_parent_path = dst_dir_path + src_parent_path[dir_len:]
            src_parent_len = len(src_parent_path)+1
            ffile_name = file_name[src_parent_len:]
            if ffile_name[0] != ".":
                fffile_name = dst_parent_path + '\\' + ffile_name
                if os.path.exists(fffile_name) == False:
                    shutil.copy2(file_name, dst_parent_path)
                    print(file_name)
        print("")


### 文件夹 比对 ###
def DirComparer(src_dir_path, dst_dir_path, src_dir_list, dst_dir_list):
    for src_dir_name in src_dir_list:
        src_dir_len = len(src_dir_path)
        dst_subdir_path = dst_dir_path + src_dir_name[src_dir_len:]
        if os.path.exists(dst_subdir_path) == False:
            dst_dir_list.append(dst_subdir_path)


### 文件 比对 ###
def FileComparer(src_dir_path, dst_dir_path, src_file_list, dst_file_list):
    for file_name in src_file_list:
        src_dir_len = len(src_dir_path)
        src_parent_path = os.path.dirname(file_name)
        dst_parent_path = dst_dir_path + src_parent_path[src_dir_len:]
        src_parent_len = len(src_parent_path)+1
        ffile_name = file_name[src_parent_len:]
        if ffile_name[0] != ".":
            fffile_name = dst_parent_path + '\\' + ffile_name
            if os.path.exists(fffile_name) == False:
                dst_file_list.append(fffile_name)


### 文件夹逐层遍历 ###
def DirTraverser(file_path, tv_dir_list, tv_file_list):
    file_list = os.listdir(file_path)
    for file in file_list:
        # 利用os.path.join()方法取得路径全名
        # 否则每次只能遍历一层目录 (?)
        full_path = os.path.join(file_path, file)
        if os.path.isdir(full_path):
            tv_dir_list.append(full_path)
            DirTraverser(full_path, tv_dir_list, tv_file_list)
        else:
            tv_file_list.append(full_path)


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

    srcdirpath1 = "\\\\192.168.11.1\\samba\\AD.PornTuTu"
    dstdirpath1 = "W:\\Bakup.Samba\\AD.PornTuTu"
    SyncSambaNetdisk(srcdirpath1, dstdirpath1)

    srcdirpath2 = "\\\\192.168.11.1\\samba\\AD.Kindle书屋"
    dstdirpath2 = "W:\\Bakup.Samba\\AD.Kindle书屋"
    SyncSambaNetdisk(srcdirpath2, dstdirpath2)

    srcdirpath3 = "\\\\192.168.11.1\\samba\\AD.iMagazine"
    dstdirpath3 = "W:\\Bakup.Samba\\AD.iMagazine"
    SyncSambaNetdisk(srcdirpath3, dstdirpath3)

    srcdirpath4 = "\\\\192.168.11.1\\samba\\2020.BOX.V"
    dstdirpath4 = "W:\\Bakup.Samba\\2020.BOX.V"
    SyncSambaNetdisk(srcdirpath4, dstdirpath4)

    srcdirpath5 = "\\\\192.168.11.1\\samba\\AD.强词有理-建筑300秒"
    dstdirpath5 = "W:\\Bakup.Samba\\AD.强词有理-建筑300秒"
    SyncSambaNetdisk(srcdirpath5, dstdirpath5)

    print("")
    print("------------------------------")
    print("Samba Sync Success :)")
    print("------------------------------")
    print("")


#------------------------------#
#    River flows in summer     #
#------------------------------#
