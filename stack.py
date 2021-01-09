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