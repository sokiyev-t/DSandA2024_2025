
# a=-15
# b=-7
# c=12
#
# m=a
# if m<b:
#    m=b
# if m<c:
#    m=c
# result=m*2
# print(result)

a=[2,34,45,5,6,7]
m=a[0]
l= len(a)
for i in range(1, l):
    if a[i]>m:
        m=a[i]
print(m)