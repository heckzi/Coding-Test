while(1):
    word=input()
    if word=='0':
        break
    check=True
    for w in range(len(word)//2):
        if word[w]!=word[-(1+w)]:
            print('no')
            check=False
            break
    if check:
        print('yes')