'''

用来生成码表(字符库)

'''
import config
import binascii
import random
import xlwt
from todna import todna
import reversecode
import getchar
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
sheet = workbook.add_sheet(u'char_dna',cell_overwrite_ok=True)#创建sheet
char_nt = config.char_nt

# remove_strands = ['ATATATATATATATATATATA','ATATATATATATAT','TATATAT','CGCGCGCGCGCGCGCGCGCGC','CGCGCGCGCGCGCG','GCGCGCG']
# 在制作码表时需要剔除的序列
remove_strands = []
for remove_char_nt in reversecode.reversecode():
    remove_strands.append(remove_char_nt)

def char_to_dna():

    print("正在生成字符对应nt数字")
    char_strands = todna.ntNum(char_nt)
    print("生成完毕")

    #总共生成的长度
    start_len = len(char_strands)
    #对字符dna链进行预处理
    #剔除掉不需要编码的DNA链
    print("正在预处理字符链")
    for remove_strand in remove_strands:
        try:
            char_strands.remove(remove_strand)
        except:
            print("要删除的",remove_strand,"不在字符链中")

    #预处理过后剩余的长度
    end_len = len(char_strands)
    print(f"预处理完毕，总共剔除了{start_len-end_len}个DNA序列。")

    #总共字符长度
    strs = getchar.getchar()
    char_total = len(strs)
    if char_total >end_len:
        print(f"生成字库的DNA序列不够用，当前拥有的DNA序列数为{end_len},字库拥有{char_total}个字符.生成当前DNA序列的nt数为{char_nt},请提高nt!!!")
        return

    # 开始给每个字符分配DNA序列
    print("开始给每个字符分配DNA序列")
    for i in range(char_total):
        #获取字符
        char = strs[i]
        #获取dna序列
        char_dna = char_strands[i]
        try:
            sheet.write(i,0,char)
            sheet.write(i,1,char_dna)
        except:
            print("写入失败")
    workbook.save('char/char_dna.xls')
    print("字库对应DNA序列生成完成")

char_to_dna()