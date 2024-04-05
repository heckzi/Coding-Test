from collections import deque

n=int(input())

deck=deque()
for i in range(1,n+1):
    deck.append(i)

while(len(deck)!=1):
    deck.popleft()
    deck.rotate(-1)
print(deck[0])