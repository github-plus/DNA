'''

此为存入码表的字符，可在其中自定义添加

'''


def getchar():
    strs = []
    sum = 0
    #根据gb2312获取到中文字符编码
    print("正在获取中文字库")
    for head in range(int(0xb0), int(0xf7) + 1):
        for body in range(int(0xa1), int(0xfe) + 1):
            var = f'{head:x} {body:x}'
            try:
                str = bytes.fromhex(var).decode('gb2312')
                strs.append(str)
            except:
                sum += 1
                print(f"遇到无法解码字符,head={head},body={body}")
    print(f"中文字库获取完毕,总共获取到{len(strs)}个中文字库,其中有{sum}不能编码(为gb2312问题)")


    sum = 0
    print("正在生成aci码表")
    #生成aci码表从32到126之间的字符
    for i in range(32, 127):
        try:
            str = chr(i)
            strs.append(str)
        except:
            sum+=0
            print("aci码表字库生成出错")
    print("aci码表生成完毕")
    if sum != 0:
        print(f"aci码表总共发生{sum}个生成错误")


    sum = 0
    print("正在生成常用标点符号")
    china_char ="、。〔〕〈〉《》？：！，“”‘’…；—−□―"

    for i in china_char:
        try:
            strs.append(i)
        except:
            sum+=0
            print(f"{i}常用标点添加失败")
    print(f"常用标点符号生成完毕，总共{sum}个发生错误")

    # 添加法语字库
    sum = 0
    print("正在生成法语字库")
    franch_char = "ÂÁÀÅÆÇÈÉÊËÌÍÎÏÐÑØÒÔÕÖÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ"

    for i in franch_char:
        try:
            strs.append(i)
        except:
            sum += 0
            print(f"{i}常用标点添加失败")
    print(f"常用标点符号生成完毕，总共{sum}个发生错误")

    #添加换行符
    sum = 0
    strs.append(chr(10))

    # 判断是否有重复字符
    if verfy(strs):
        print("所有字符没有重复，请安心使用")
    else:
        print("有重复字符，建议重新审查获取字符方式")
    return strs

def get_en_char():
    strs = []
    sum = 0
    print("正在生成aci码表")
    # 生成aci码表从32到126之间的字符
    for i in range(32, 127):
        try:
            str = chr(i)
            strs.append(str)
        except:
            sum += 0
            print("aci码表字库生成出错")
    print("aci码表生成完毕")
    if sum != 0:
        print(f"aci码表总共发生{sum}个生成错误")

    # 添加法语字库
    sum = 0
    print("正在生成法语字库")
    franch_char = "ÂÁÀÅÆÇÈÉÊËÌÍÎÏÐÑØÒÔÕÖÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ−"
    for i in franch_char:
        try:
            strs.append(i)
        except:
            sum += 0
            print(f"{i}常用标点添加失败")
    print(f"常用标点符号生成完毕，总共{sum}个发生错误")

    # 添加换行符
    sum = 0
    strs.append(chr(10))

    # 判断是否有重复字符
    if verfy(strs):
        print("所有字符没有重复，请安心使用")
    else:
        print("有重复字符，建议重新审查获取字符方式")
    return strs

def verfy(strs):
    for i in range(len(strs)):
        for j in range(i+1,len(strs)):
            if strs[i] == strs[j]:
                print(f"重复字符为{strs[i]}")
                return False
    return  True
