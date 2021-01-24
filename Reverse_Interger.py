def reverse(x:int):
    res = 0
    while x != 0:
        if x > 0:
            res = res * 10 + x % 10
            x //= 10
        else:
            res = res * 10 + x % -10
            x = -(x // -10)
    return res if -2 ** 31 < res < 2 ** 31 -1 else 0

x = 8812622462
print(reverse(x))