def countdown(i):
    if i>=0:
        print(i)
        countdown(i-1)


countdown(4)


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(5))