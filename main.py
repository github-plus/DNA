import time

import encode
import decode

print("请将需要编码的txt放在doc文件内!!!!")


select = input("请输入需要做的操作 1 编码 2解码 输入其他数字将自动结束本程序:")
if select =='1':
    filename = input("请输入需要编码的txt文件名称:")
    start = time.time()
    if encode.encode(filename):
        print(f"文件编码完成，产生的文件名为{filename}.xlsx")
        end = time.time()
        times = end-start
        print(f"总共时间为{times}秒")


if select =='2':
    filename = input("请输入需要解码的excle文件名称:")
    start = time.time()
    decode.decode(filename)
    end = time.time()
    times = end - start
    print(f"总共时间为{times}秒")

