arr=[2,3,5,0,9]
def sumArray(a):
    if len(a)==0:
        return 0
    else:
        return a.pop()+sumArray(a)

# print(sumArray(arr))
def quickSort(a):
    if len(a)<2:
        return a
    else:
        pivot = a[0]
        less=[]
        greater=[]
        for e in a[1:]:
            if e<=pivot:
                less.append(e)
            else:
                greater.append(e)
        # less=[i for i in a[1:] if i<=pivot]
        # greater = [i for i in a[1:] if i > pivot]
        return quickSort(less)+[pivot]+quickSort(greater)

print(quickSort(arr))