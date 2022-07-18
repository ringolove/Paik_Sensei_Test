import sys
n = int(sys.stdin.readline())
stack = []

def push(k):
    stack.append(k)
    
def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[0])
        stack.remove(stack[0])
        
def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[0])

def back():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


for i in range(n):
    input = sys.stdin.readline().split()
    command = input[0]
    
    if command == "push":
        value = input[1]
        push(value)
    
    elif command == "pop":
        pop()
    
    elif command == "size":
        size()
    
    elif command == "empty":
        empty()
        
    elif command == "front":
        front()
    
    elif command == "back":
        back()