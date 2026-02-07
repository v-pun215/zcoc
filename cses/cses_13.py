def generateGrayCode(n):
    total = 2**n
    for i in range(total):
        grayValue = i^(i>>1)
        print(format(grayValue, f'0{n}b'))
    
n = int(input())
generateGrayCode(n)