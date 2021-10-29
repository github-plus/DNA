'''

用以查找码表中是否存在某个字符

'''

# 读取字符库
import xlrd

workBook = xlrd.open_workbook('char/char_dna.xls')
# 获取读取的数据
char_to_dna = workBook.sheet_by_index(0)
global result
result = {}

# 获取总共行数
rows = char_to_dna.nrows
print("正在开始将字库写入字典中")
for i in range(rows):
    cha = char_to_dna.cell_value(i,0)
    dna = char_to_dna.cell_value(i,1)
    result[cha]=dna
print("字典写入完成")
print(result)
while True:
    char = input("请输入要查找的码表字符:")
    print(result.get(char))