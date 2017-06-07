# Welcome, this is a simple, pretty useless, test python file.
#The main test legacy code is commented out.
#for i in range(101):
#    for s in range(i):
#        print (s * i)
import random
def ranbinstr(Length):
    def digit():
        BinDigit = ''
        while (len(BinDigit) < Length):
            BinDigit += random.choice('0' '1')
        return BinDigit
    return digit()
def BinaryPyramid(size):
	l = 1
	for i in range(size):
            print (' ' * (size - i) + ranbinstr(l))
            l += 2
BinaryPyramid(40)
