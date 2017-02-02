# l = [1, 2, 3, 4]
#
# for n in range 20:
#     for x in l:
#         if n/# XXX:

def isfactor(number, factor):
    if number%factor==0:
        return 1
    else:
        return 0

# print isfactor(20, 4)
l=[]
def multifactors(number, nofacts):
    count = 0
    for i in range(1, nofacts+1):
        count += isfactor(number, i)
    if count == nofacts:
        return True
    else:
        return count

print multifactors(1, 10)
# l=[]
# def rangechecker(n):
#     for i in range(1, n+1):
#         l.append(i)
#     print l
#
# rangechecker(4)

def multifactortest(n):
    x=2520
    while True:
        x += 1
        if multifactors(x, n):
            return x
            break


print multifactortest(10)



# def iter(n):
#     for i in n
