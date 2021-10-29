#可自主添加适配数
def match(num):
    if num<=9:
        return 2
    if num<=36:
        return 3
    if num<=135:
        return 4
    if num<=540:
        return 5
    if num<=2133:
        return 6
    if num<=8424:
        return 7
    if num <= 33291:
        return 8
    if num <= 131544:
        return 9
    if num <= 519777:
        return 10
    if num <= 2053836:
        return 11

def dna_to_num(seq):
    num = ''

    for i in range(len(seq)):
        if seq[i] == 'A':
            num += '0'
        if seq[i] == 'C':
            num += '1'
        if seq[i] == 'T':
            num += '2'
        if seq[i] == 'G':
            num += '3'
    return num
