#进制转换函数，n为待转换的十进制数，x为机制，取值为2-16
def transform(n, x):
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'b', 'C', 'D', 'E', 'F']
    b = []
    while True:
        s = n // x  # 商
        y = n % x  # 余数
        b = b + [y]
        if s == 0:
            break
        n = s
    b.reverse()
    dig = '';
    for i in b:
        dig += str(a[i])
        #print(a[i], end='')
    return dig

def four_to_ten(n):
    temp_num = str(n)
    num = 0
    for i in range(len(temp_num)):
        num += int(temp_num[i])*pow(4,len(temp_num)-i-1)
    return num