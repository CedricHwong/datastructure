# 回文判断

def checkPalindrome(x:int):
    """
    docstring
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    revertedNumber = 0
    while x > revertedNumber:
        revertedNumber = revertedNumber * 10 + x % 10
        x //= 10
    return (x == revertedNumber or x == revertedNumber // 10)

x1 = 121
x2 = 123
x3 = -121
print(checkPalindrome(x1))
print(checkPalindrome(x2))
print(checkPalindrome(x3))