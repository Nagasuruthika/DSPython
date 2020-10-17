# Python program to 
# demonstrate stack implementation
# using list


stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() fucntion to pop
# element from stack in 
# LIFO order
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are poped:')
print(stack)

# uncommenting print(stack.pop()) 
# will cause an IndexError 
# as the stack is now empty

Output: 

Initial stack:
deque(['a', 'b', 'c'])

Elements poped from stack:
c
b
a

Stack after elements are poped:
deque([])

# Python program to 
# demonstrate stack implementation
# using queue module


from queue import LifoQueue

# Initializing a stack
stack = LifoQueue(maxsize = 3)

# qsize() show the number of elements
# in the stack
print(stack.qsize())

# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full()) 
print("Size: ", stack.qsize()) 

# get() fucntion to pop
# element from stack in 
# LIFO order
print('\nElements poped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())



