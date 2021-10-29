print("Enter the amount of variables displayed: ")
nfib = int(input())
a = 0
b = 1
nfib = 0
while nfib <= 10000:
    nfib = a + b
    a = b
    b = nfib
    print(nfib)
