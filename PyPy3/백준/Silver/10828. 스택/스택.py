import sys
n=int(sys.stdin.readline())
stack=list()

for i in range(n):
    all=sys.stdin.readline().split()
    a=all[0]
    if a=="push":
        x=int(all[1])
        stack.append(x)
    elif a=="pop":
        if len(stack)!=0:
            num = stack.pop()
            print(num)
        else:
            print("-1")
    elif a=="size":
        print(len(stack))
    elif a=="empty":
        if len(stack) != 0:
            print("0")
        else:
            print("1")
    else:
        if len(stack)==0:
            print("-1")
        else:
            print(stack[-1])
        
        

