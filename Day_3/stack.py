stack = []
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
print("Stack elements are:", stack)

print("Top element is:", stack[-1])

popped_element = stack.pop()
popped_element = stack.pop()
print("popped element is:",popped_element)
print("stack after pop operation:",stack)
pushed_element = 60
stack.append(pushed_element)    
print("stack after pushing an element:",stack)
print("Top element is:", stack[-1])
print("is stack empty?", len(stack) == 0)
