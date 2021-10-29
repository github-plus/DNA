import xlrd

def test():
    workbook = xlrd.open_workbook('doc/jia_encode.xls')
    sheet = workbook.sheet_by_index(0)

    rows = sheet.nrows
    err = []
    for i in range(rows):
        strand = sheet.cell_value(i,0)

        per = gc(strand)
        print(per)
        if per<0.4 or per >0.6:
            err.append(per)
    print(err)

def gc(strand):

    gc =  (strand.count('G') + strand.count('C')) / (strand.count('A') + strand.count('T') + strand.count('C') + strand.count('G'))
    return gc
test()