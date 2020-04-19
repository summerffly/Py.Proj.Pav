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
        return decision
    elif decision == "N":
        print("")
        print("------------------------------")
        print(">>> 同步已取消 <<<")
        print("------------------------------")
        print("")
    else:
        print("")
        print("------------------------------")
        print(">>> Select Error !!! <<<")
        print("------------------------------")
        print("")
    return decision


### Samba网盘同步 ###
def SyncSambaNetdisk(src_dir_path, dst_dir_path):
    dir_list = list()
    file_list = list()
    DirTraverser(src_dir_path, dir_list, file_list)

    print(">>>>>>>>>><<<<<<<<<<<")
    print(">>> Sync Dir List <<<")
    print(">>>>>>>>>><<<<<<<<<<<")
    for dir_name in dir_list:
        dir_len = len(src_dir_path)
        dst_subdir_path = dst_dir_path + dir_name[dir_len:]
        if os.path.exists(dst_subdir_path) == False:
            print(dst_subdir_path)
    print("")
    print(">>>>>>>>>>><<<<<<<<<<<")
    print(">>> Sync File List <<<")
    print(">>>>>>>>>>><<<<<<<<<<<")
    for file_name in file_list:
        dir_len = len(src_dir_path)
        src_parent_path = os.path.dirname(file_name)
        dst_parent_path = dst_dir_path + src_parent_path[dir_len:]
        src_parent_len = len(src_parent_path)+1
        ffile_name = file_name[src_parent_len:]
        if ffile_name[0] != ".":
            fffile_name = dst_parent_path + '\\' + ffile_name
            if os.path.exists(fffile_name) == False:
                print(fffile_name)

    if MakeDecision() == "Y":
        for dir_name in dir_list:
            dir_len = len(src_dir_path)
            dst_subdir_path = dst_dir_path + dir_name[dir_len:]
            if os.path.exists(dst_subdir_path) == False:
                os.makedirs(dst_subdir_path)
                print(dst_subdir_path)
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

    #srcdirpath = "\\192.168.11.1\samba\2020.BOX.V"
    srcdirpath1 = "\\\\192.168.11.1\\samba\\AD.PornTuTu"
    dstdirpath1 = "W:\\Bakup.Samba\\AD.PornTuTu"
    SyncSambaNetdisk(srcdirpath1, dstdirpath1)

    srcdirpath2 = "\\\\192.168.11.1\\samba\\AD.Kindle书屋"
    dstdirpath2 = "W:\\Bakup.Samba\\AD.Kindle书屋"
    SyncSambaNetdisk(srcdirpath2, dstdirpath2)

    srcdirpath3 = "\\\\192.168.11.1\\samba\\AD.iMagazine"
    dstdirpath3 = "W:\\Bakup.Samba\\AD.iMagazine"
    SyncSambaNetdisk(srcdirpath3, dstdirpath3)

    #srcdirpath4 = "\\\\192.168.11.1\\samba\\2020.BOX.V"
    #dstdirpath4 = "W:\\Bakup.Samba\\2020.BOX.V"
    #SyncSambaNetdisk(srcdirpath4, dstdirpath4)

    print("")
    print("------------------------------")
    print("Samba Sync Success :)")
    print("------------------------------")
    print("")


#------------------------------#
#    River flows in summer     #
#------------------------------#
