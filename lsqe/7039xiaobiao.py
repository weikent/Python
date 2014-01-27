#!/usr/bin/env python
#encoding=utf8

import re                       # 正则表达式
import os                       # for os.remove()  删除文件

import lsqe
import median

# print os.getcwd()
if os.path.isfile(os.getcwd() + "/xiaobiao"):
    os.remove(os.getcwd() + "/xiaobiao")

result = open("xiaobiao", 'w')
result_k_i = open("result_k_i", 'w')
result_b_i = open("result_b_i", 'w')
result_k_p = open("result_k_p", 'w')
result_b_p = open("result_b_p", 'w')
result_k_u = open("result_k_u", 'w')
result_b_u = open("result_b_u", 'w')



for i in range(1,12):
    u_X = open('uX', 'w')
    u_Y = open('uY', 'w')

    for j in ["100-0.5L","100-1", "220-0.5L", "220-1"]:
        filename = "校%s—%s.txt" % (i, j)
        # print filename

        i_X = open('iX', 'w')
        i_Y = open('iY', 'w')

        p_X = open('pX', 'w')
        p_Y = open('pY', 'w')


        num_line = 0
        for line in open(filename).readlines():
            pattern_stand_i = re.compile("^Irms")
            pattern_combo_i = re.compile("^COMBO_Irms")
            pattern_stand_p = re.compile("^PowerP")
            pattern_combo_p = re.compile("^COMBO_Prms")
            pattern_stand_u = re.compile("^Urms")
            pattern_combo_u = re.compile("^COMBO_Urms")
            if num_line < 8:
                num_line += 1
                continue
            if pattern_combo_i.match(line):
                arr_combo_i = line.split(' ')
                print >> i_X, arr_combo_i[1],
            elif pattern_stand_i.match(line):
                arr_stand_i = line.split(' ')
                print >> i_Y, arr_stand_i[2],
            elif pattern_combo_p.match(line):
                arr_combo_p = line.split(' ')
                print >> p_X, arr_combo_p[1],
            elif pattern_stand_p.match(line):
                arr_stand_p = line.split(' ')
                print >> p_Y, arr_stand_p[2],
            elif pattern_combo_u.match(line):
                arr_combo_u = line.split(' ')
                print >> u_X, arr_combo_u[1],
            elif pattern_stand_u.match(line):
                arr_stand_u = line.split(' ')
                print >> u_Y, arr_stand_u[2],


        i_X.close()
        i_Y.close()
        p_X.close()
        p_Y.close()
        
        print >> result, filename + ":"
        print >> result, "    电流:"
        print >> result, "        combo值:",
        print >> result, open('iX', 'r').readline()
        print >> result, "        标准表值:",
        print >> result, open('iY', 'r').readline()
        print >> result, "        最小二乘法结果:",
        print >> result_k_i, lsqe.lsqe("iX", "iY").split(' ')[2]
        print >> result_b_i, lsqe.lsqe("iX", "iY").split(' ')[6]
        print >> result, lsqe.lsqe("iX", "iY")
        
        os.remove("iX")
        os.remove("iY")

        print >> result, "    功率:"
        print >> result, "        combo值:",
        print >> result, open('pX', 'r').readline()
        print >> result, "        标准表值:",
        print >> result, open('pY', 'r').readline()
        print >> result, "        最小二乘法结果:",
        print >> result_k_p, lsqe.lsqe("pX", "pY").split(' ')[2]
        print >> result_b_p, lsqe.lsqe("pX", "pY").split(' ')[6]
        print >> result, lsqe.lsqe("pX", "pY")

        os.remove("pX")
        os.remove("pY")

    u_X.close()
    u_Y.close()

    print >> result, "表%d电压:" % (i)
    print >> result, "        combo值:",
    print >> result, open('uX', 'r').readline()
    print >> result, "        标准表值:",
    print >> result, open('uY', 'r').readline()
    print >> result, "        最小二乘法结果:",
    print >> result_k_u, lsqe.lsqe("uX", "uY").split(' ')[2]
    print >> result_b_u, lsqe.lsqe("uX", "uY").split(' ')[6]
    print >> result, lsqe.lsqe("uX", "uY")


    os.remove("uX")
    os.remove("uY")

    print >> result, "======================================================================"
    print >> result, "======================================================================"
    print >> result, "======================================================================"
    print >> result, "======================================================================"


result_k_i.close()
result_b_i.close()
result_k_p.close()
result_b_p.close()
result_k_u.close()
result_b_u.close()


print >> result, "最终的中位数:"
print >> result, "    电流的K值的中位数:",
print >> result, median.median("result_k_i")
os.remove("result_k_i")

print >> result, "    电流的B值的中位数:",
print >> result, median.median("result_b_i")
os.remove("result_b_i")

print >> result, "    功率的K值的中位数:",
print >> result, median.median("result_k_p")
os.remove("result_k_p")

print >> result, "    功率的B值的中位数:",
print >> result, median.median("result_b_p")
os.remove("result_b_p")

print >> result, "    电压的K值的中位数:",
print >> result, median.median("result_k_u")
os.remove("result_k_u")

print >> result, "    电压的B值的中位数:",
print >> result, median.median("result_b_u")
os.remove("result_b_u")
