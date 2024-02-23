def solution(s):
    answer = ''
    strlist = list(map(str,s.split(" ")))
    # print(strlist)
    for i in strlist:
        for j in range(len(i)):
            if j==0:
                if 97<=ord(i[j])<=122:
                    l =list(i)
                    l[j]= chr(ord(l[j])-32)
                    i = "".join(l)
            else:
                if 65<=ord(i[j])<=90:
                    l =list(i)
                    l[j]=chr(ord(l[j])+32)
                    i = "".join(l)
        answer+=i
        answer+=" "
                    
    if answer[len(answer)-1] == " ":
        answer = answer[:len(answer)-1]
    return answer