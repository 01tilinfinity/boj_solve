N = int(input())
tmp_list = []

for i in range(N):
    lst = list(map(int,input().split()))
    tmp_list.append(lst)

def manhattan_dist(l1,l2):
    return abs(l1[0]-l2[0])+abs(l1[1]-l2[1])

total_dist = 0 

for i in range(1,N):
    total_dist += manhattan_dist(tmp_list[i-1],tmp_list[i])

min_dist = total_dist 

for i in range(1,N-1):
    skip_dist = total_dist
    skip_dist -= manhattan_dist(tmp_list[i-1],tmp_list[i])
    skip_dist -= manhattan_dist(tmp_list[i], tmp_list[i+1])
    skip_dist += manhattan_dist(tmp_list[i-1],tmp_list[i+1])
    
    min_dist = min(skip_dist, min_dist)

print(min_dist)