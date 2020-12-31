s=int(input("Enter the number of stack variables to be inputed"))
q=int(input("Enter the number of queue variables to be inputed"))
stack=[]
queue=[]
for i in range(s):
    st=input("Enter stack elements")
    stack.append(st)
for j in range(q):
    qu=input("Enter queue elements")
    queue.append(qu)

print(stack)
print(queue)
for k in range(s):
    print(stack.pop())
for l in range(s):
    print(queue.pop())
