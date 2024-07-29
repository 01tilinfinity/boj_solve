n = int(input())
a = set(map(int,input().split()))
m = int(input())
array = list(map(int,input().split()))

for num in array:
    print(1) if num in a else print(0)
