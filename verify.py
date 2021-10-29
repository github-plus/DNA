filename1 = 'doc/bl_fr_encode.txt'
filename2 = 'doc/bl_fr_decode.txt'
log = open('log/verify.log',mode='w',encoding='utf-8')
with open(filename1,encoding='utf-8') as file:
    f1 = file.read()
with open(filename2,encoding='utf-8') as file:
    f2 = file.read()
flag = True
for i in range(len(f1)):

    try:
        if f1[i] != f2[i]:
            # print("数据不一样")
            # print(f"在第{i}个位置数据不一样,编码内容是:{f1[i]}，解码内容是:{f2[i]}")
            # break
            log.write(f"在第{i}个位置数据不一样,编码内容是:{f1[i]}，解码内容是:{f2[i]}")
            flag = False
    except:
        print("两个文件数据大小不一样")


if flag:
    print("校准完毕，编码解码数据一样")
else:
    print("校准完毕，编码解码数据不一，详情请查看日志verify.log")