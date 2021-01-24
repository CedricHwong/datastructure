'''
栈的实现，其策略是一种后进先出的概念（last in, first out）

'''
class Stack(object):
    # 初始化栈为空
    def __init__(self):
        self.items = []
    
    # 判断栈是否为空， 返还bool value
    def is_empty(self):
        return self.is_empty == []

    # 返回栈顶（stack.top）元素
    def peek(self):
        return self.items[len(self.items) - 1]
    
    # 返回栈的大小
    def size(self):
        return len(self.items)
    
    # 入栈
    def push(self, item):
        self.items.append(item)
    
    # 出栈
    def pop(self):
        return self.items.pop()

# s = Stack()
# print(s.is_empty())
# s.push(4)
# s.push("dog")
# s.push(True)
# print(s.peek())
# print(s.pop())
# print(s.peek())

'''
Bracket matching

Leetcode 20 :
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

'''
def isVaild(s: str) -> bool:
    if len(s) % 2 == 1:
        return False
    
    parirs_dic = {')':'(',']':'[','}':'{'}
    temp_stack = []

    for ch in s:
        if ch in parirs_dic:
            if not temp_stack or temp_stack[-1] != parirs_dic[ch]:
                return False
            temp_stack.pop()
        else:
            temp_stack.append(ch)

    return not temp_stack      

s1 =  "()[]{}"
s2 =  "([)]"
s3 =  "{[]}"

print(isVaild(s1))
print(isVaild(s2))
print(isVaild(s3))

'''
682. Baseball Game
You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
"C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
Return the sum of all the scores on the record.

'''

# def calPoints(ops: List[str]) -> int:
#     temp = []
#     for i in ops:
#         if n == '+':
#             temp.append(temp[-1] + temp[-2])
#         elif n == 'C':
#             temp.pop()
#         elif n == 'D':
#             temp.append(2 * temp[-1])
#         else:
#             temp.append(int(n))
#     return sum(temp)      

'''
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two
 adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is
the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent
characters that make the string bad and remove them. 
You can keep doing this until the string becomes good.

Return the string after making it good. 
The answer is guaranteed to be unique under the given constraints.
'''
def makeGood(s: str) -> str:
    for i in range(len(s)s, 1):
        for j in range(len(s)-1, 0):
            if s(i).islower() == True and s(i).upper == s(j):
                s.pop(i) and s.pop(j)
            if s(i).isupper() == True and s(i).lower == s(j):
                s.pop(i) and s.pop(j)
    return s
    

s = "leEeetcode"
print(makeGood(s))