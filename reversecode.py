import random

import config


char_nt = config.char_nt  #在此设置字库中每个字符对应的nt数
address_nt = config.address_nt #在此设置位置信息的nt数
char_num = config.char_num #在此设置每条连链中存储的字符个数
range_num = config.range_num  #迭代次数
replace_at = config.replace_at #替换字符的模板，
replace_gc = config.replace_gc #替换字符的模板，
strand_len = address_nt + char_num*char_nt #一条链的长度
max_replace = config.max_replace #最大被替换的字符个数

def reversecode():
    strand_gc = ''
    strand_at = ''
    list = ['A', 'T', 'C', 'G']
    for i in range(strand_len - char_nt):
        strand_at += random.choice(list)
        strand_gc += random.choice(list)
    strand_gc += replace_gc
    strand_at += replace_at
    # print(strand_gc)
    # print(strand_at)
    # 截取最末尾中1个字符对应的nt数
    last_gc = temp_decode(strand_gc)[adverse(char_nt):]
    last_at = temp_decode(strand_at)[adverse(char_nt):]
    # print(temp_decode(strand_gc))
    # print(temp_decode(strand_at))
    # print(last_gc)
    # print(last_at)
    return last_at,last_gc

def temp_decode(new_strand):
    for i in range(range_num-1, -1, -1):
        for j in range(len(new_strand)):
            index = (i + 2) * j
            if index < len(new_strand):
                if new_strand[index] == 'C':
                    new_strand = new_strand[:index] + 'A' + new_strand[index + 1:]
                elif new_strand[index] == 'T':
                    new_strand = new_strand[:index] + 'C' + new_strand[index + 1:]
                elif new_strand[index] == 'G':
                    new_strand = new_strand[:index] + 'T' + new_strand[index + 1:]
                elif new_strand[index] == 'A':
                    new_strand = new_strand[:index] + 'G' + new_strand[index + 1:]

    return new_strand

def encrypt(strand):
    new_strand = strand
    global sum
    last = 0
    #迭代次数
    for i in range(0,range_num):
        for j in range(len(new_strand)):
            index = (i+2)*j
            if index < len(new_strand):

                if new_strand[index] == 'A':
                    new_strand = new_strand[:index] + 'C' + new_strand[index+1:]
                elif new_strand[index] == 'C':
                    new_strand = new_strand[:index] + 'T' + new_strand[index+1:]
                elif new_strand[index] == 'T':
                    new_strand = new_strand[:index] + 'G' + new_strand[index+1:]
                elif new_strand[index] == 'G':
                    new_strand = new_strand[:index] + 'A' + new_strand[index+1:]

    percentage_1 = gc(new_strand) #改造前的gc含量
    if percentage_1 < 0.4 or percentage_1 > 0.6 :
        temp_new_strand = ''
        if percentage_1 > 0.6:

            # 替换字符所对应的nt数，假如1个字符对应的char_num=7，替换1个字符，那就是替换最末尾7个nt；替换2个字符，那就是替换最末未14个nt
            for replace_num in range(1,max_replace+1):
                replace_nt_at = ''
                for i in range(replace_num):
                    replace_nt_at += replace_at
                sum += 1
                last = replace_num
                temp_new_strand = new_strand[:adverse(char_nt*replace_num)] + replace_nt_at
                if gc(temp_new_strand) < 0.6:
                    break

        if percentage_1 < 0.4:


            for replace_num in range(1, max_replace + 1):
                replace_nt_gc = ''
                for i in range(replace_num):
                    replace_nt_gc += replace_gc
                sum += 1
                last = replace_num
                temp_new_strand = new_strand[:adverse(char_nt*replace_num)] + replace_nt_gc
                if gc(temp_new_strand) > 0.4:
                    break
        percentage_2 = gc(temp_new_strand) #改造后的gc含量
        if percentage_2 < 0.4 or percentage_2 > 0.6:


            print("改造前", new_strand)
            print("改造前AT含量为", percentage_1)
            print("改造后AT含量为", percentage_2)
            print("改造后", temp_new_strand)

        new_strand = temp_new_strand
    print(new_strand)

# 正整数取反取反函数
def adverse(char_num):
    char_num_num = '-' + str(char_num)
    return int(char_num_num)

# 计算gc含量
def gc(strand):

    gc =  (strand.count('G') + strand.count('C')) / (strand.count('A') + strand.count('T') + strand.count('C') + strand.count('G'))
    return gc


#print(temp_decode('AACGGAGGTTCAGCCAACCTAGCACCATCAAGATACGAAGGAGAAATAT'))
#encrypt('AAATCGATGATGTATCAAACGAGAGATACATGAATGAATCCACACACAG')

