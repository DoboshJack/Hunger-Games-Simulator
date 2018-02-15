n1 = 1
#    ^- First number in sequence

n2 = 1
#    ^- Second Number in sequence

y = 10
#   ^- Number of Fibbonacci numbers wanted


print(n1)
print(n2)
x = (y - 2) / 2
for i in range( int(x) ):

    n3 = (n1 + n2)
    print(n3)
    n1 = n3

    n4 = (n1 + n2)
    print(n4)
    n2 = n4
