import pyautogui
import requests
import xlrd
import xlwt
from selenium import webdriver

path = r'chromedriver.exe'
bro = webdriver.Chrome(executable_path=path)

url = 'https://go.drugbank.com/drugs'
bro.get(url)

#读取S1
workBook = xlrd.open_workbook('S1.xlsx')
#写入文件
f = xlwt.Workbook() #创建工作簿
S2 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)#创建sheet

#获取读取的数据
S1 = workBook.sheet_by_index(0)

#获取总共行数
rows = S1.nrows
#遍历行数，用以搜索
drug = ''
ATC = ''
for i in range(rows):
    #获取药物名称
    temp_drug = S1.cell_value(i,0)
    S2.write(i, 0, temp_drug) #写入药物名称
    #获取疾病名称
    temp_disease = S1.cell_value(i,2)
    S2.write(i, 2, temp_disease)#写入疾病名称

    #如果该药物与上个药物名称相同,则直接使用上次搜索的ATC结果
    if drug == temp_drug:
        S2.write(i,1,ATC)
    # 如果不一样,则在drugban搜索
    else:
        #搜索框输入新的药物名称
        drug = temp_drug
        bro.find_element_by_name('query').send_keys(drug)
        pyautogui.typewrite(['enter'])
        #查找到ATC
        value = bro.find_element_by_xpath('/html/body/main/div/div/div[2]/div[2]/dl[5]/dd[1]/a').text
        #截取前七个数据
        ATC = value[0:7]
        #写入文档
        S2.write(i,1,ATC)
    print(i,rows)

f.save('S2.xls')