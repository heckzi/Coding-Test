words=input()
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt=0

for c in croatia:
    words=words.replace(c,'!')
cnt=len(words)
print(cnt)