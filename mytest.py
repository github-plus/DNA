import random

# from todna import todna
# todna.ntNum(5)
# arry = todna.ntNum(3)
# print(arry)
# arry.remove('AAA')
# print(arry)
# import char_to_dna
# char_to_dna.char_to_dna()
'''
head = random.randint(0xb0, 0xf7)
print(head)
body = random.randint(0xa1, 0xfe)
print(body)
val = f'{head:x} {body:x}'
print(val)
print(bytes.fromhex(val))
str = bytes.fromhex(val).decode('gb2312')
print(str)
'''
# 176-247
# 161-254
# 215
# strs = []
# sum = 0
# for head in range(int(0xa0),int(0xf7)+1):
#     for body in range(int(0xa1),int(0xfe)+1):
#         var = f'{head:x} {body:x}'
#         try:
#             str = bytes.fromhex(var).decode('gb2312')
#             strs.append(str)
#         except:
#             sum+=1
#             print(f"遇到无法解码字符,head={head},body={body}")
# print(len(strs))
# print(sum)
# head = 0xa0
# for i in range(32,127):
#     print(chr(i))
# import encode
# encode.encode()
# import decode
# decode.decode()
# strand = 'abcdefghijk'
# a = 3
# b = len(strand)-a
# print(strand[a:b])
#
# with open("doc/mytest.txt",mode='r',encoding='utf-8') as f:
#     data = f.read()
#     print(len(data))
# for i in data:
#     print(i)
#
# def test():
#     char_nt = 7
#     strand= 'ATCGATCGATCGATCGATCGATCGATCGATGCGCGCGGCGCGTGGCTCGCG'
#     max_replace=3
#     for replace_num in range(max_replace,-1,-1):
#
#         replace_nt_at = ''
#         replace_nt_gc = ''
#         if replace_num == 0:
#             return 0
#         for i in range(replace_num):
#             replace_nt_at += 'ATATATA'
#             replace_nt_gc += 'GCGCGCG'
#         if strand[adverse(replace_num*char_nt):] == replace_nt_at or strand[adverse(replace_num*char_nt):] == replace_nt_gc:
#             return replace_num
#
# def adverse(char_num):
#     char_num_num = '-' + str(char_num)
#     return int(char_num_num)
#
# print(test())
