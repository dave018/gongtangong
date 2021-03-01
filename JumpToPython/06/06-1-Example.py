
#06-1
def GuGu(n):
    ret = []
    for i in range(1,10): ret.append(i*n)
    return ret
print(GuGu(3))

#06-2
a = sum(list(filter(lambda x: x%3==0 or x%5==0, range(1,1000))))
print(a)

#06-3
#skip

#06-5
