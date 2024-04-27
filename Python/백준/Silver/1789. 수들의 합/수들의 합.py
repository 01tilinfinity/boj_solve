s = int(input())
n = 1
sum = 0
while True:
    sum += n 
    if sum <= s:
        n += 1
    else:
        break 
print(n-1)
    