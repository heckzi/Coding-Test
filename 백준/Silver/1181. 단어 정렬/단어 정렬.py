n=int(input())
words=set()
for _ in range(n):
    words.add(input())
    
words=list(words)
words.sort()
words.sort(key=len)
# print(words)
for w in words:
    print(w)