def solution(s):
    answer = len(s)
    leng = len(s)
    for i in range(1, int(leng / 2)+1):
        temp=[]
        cnt=[]
        ans = ''
        for j in range(0, int(leng/i)):
            tmp = s[i*j:i*(j+1)]
            # temp 비어있으면
            if temp == []:
                temp.append(tmp)
                cnt.append(1)
                continue
            # 안비어있으면
            l = len(temp)
            if tmp == temp[l-1]:
                cnt[l-1]+=1
            else:
                temp.append(tmp)
                cnt.append(1)
        # 맨뒷부분이랑 다합쳐주기
        for n in range(len(temp)):
            if cnt[n]==1:
                ans+= temp[n]
            else :
                ans += (str(cnt[n])+temp[n])
        ans += s[int(leng/i)*i:]
        if len(ans)<answer:
            answer = len(ans)
    return answer