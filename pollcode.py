#企业编码生成系统

import os

#mkdir()函数
def mkdir(path) :           #创建文件夹函数
    isexists = os.path.exists(path)
    if not isexists :
        os.mkdir(path)

def openfile(filename) :    #读取文件内容函数
    f = open(filename)
    fllist = f.read()       #读取文件内容
    f.close()
    return fllist

#对输入数字，字母和位数进行验证
def inputbox(showstr, showorder, length) :
    instr = input(showstr)
    if len(instr) != 0 :
        if showorder == 1 :     #验证方式1，数字格式，不限位数，大于0的整数
            if str.isdigit(instr) :
                if instr == 0 :
                    print("\033[1;31;40m 输入为零，请重新输入！！\033[0m")      #要求重新输入
                    return "0"
                else :
                    return instr
            else :
                print("\033[1;31;40m 输入非法，请重新输入！！\033[0m")
                return "0"
        if showorder == 2 :     # 验证方式2，要求字母格式且是指定字母
            if str.isalpha(instr) :
                if len(instr) != length :
                    print("\033[1;31;40m必须输入" + str(length) + "个字母，请重新输入！！\033[0m")
                    return "0"
                else :
                    return instr
            else :
                print("\033[1;31;40m 输入非法，请重新输入！！\033[0m")
                return "0"
        if showorder == 3 :     #验证方式3，要求数字格式且输入数字位数有要求
            if str.isdigit(instr) :
                if len(instr) != length :
                    print("\033[1;31;40m必须输入" + str(length) + "个字母，请重新输入！！\033[0m")
                    return "0"
                else :
                    return instr
            else :
                print("\033[1;31;40m 输入非法，请重新输入！！\033[0m")
                return "0"
    else :
        print("\033[1;31;40m 输入为空，请重新输入！！\033[0m")
        return "0"


