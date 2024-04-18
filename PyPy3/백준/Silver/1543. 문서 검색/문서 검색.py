doc = input() 
word = input() 
cnt = 0
i = 0

while i<=len(doc):
    if doc[i:i+len(word)] == word:
        i += len(word)
        cnt += 1
    else:
        i += 1
print(cnt)
        