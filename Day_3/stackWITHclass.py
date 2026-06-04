class stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,item):
        self.stack.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty!"
    
    def is_empty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    
s =stack()
s.push("A")
s.push("B")
s.push("C")
print(s.size())  # Output: 3
print(s.peek())  # Output: C
print(s.pop())   # Output: C
print(s.pop())   # Output: B
print(s.pop())   # Output: A