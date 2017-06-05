# Welcome, this is a simple, pretty useless, test python file.
for i in range(101):
    for s in range(i):
        print (s * i)
def BinaryPyramid(size):
	l = 1
	for i in range(size):
		if i % 2 == 0:
			print (' ' * (size - i) + '1' * l)
		else:
			print (' ' * (size - i) + '0' * l)
		l += 2
BinaryPyramid(40)
