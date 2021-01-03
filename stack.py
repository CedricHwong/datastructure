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

s = Stack()
print(s.is_empty())
s.push(4)
s.push("dog")
s.push(True)
print(s.peek())
print(s.pop())
print(s.peek())
