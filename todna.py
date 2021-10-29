from  BaseUtils import transform

class todna():

    def ntNum(num):
        strands = []
        print("开始生成nt")
        #生成num个0
        for i in range(0,pow(4,num)):

            strand = ''
            dig = transform(i,4)
            length = len(dig)
            if length != num:
                temp = ''
                for j in range(num-length):
                    temp += '0'
                dig = temp + dig
            for x in dig:
                if (x) == '0':
                    strand += 'A'
                if (x) == '1':
                    strand += 'C'
                if (x) == '2':
                    strand += 'T'
                if (x) == '3':
                    strand += 'G'

            strands.append(strand)
        print("nt数生成毕")
        return strands