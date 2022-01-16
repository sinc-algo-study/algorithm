def solution(s):
    answer = len(s)
    for i in range(1,len(s)):
        compress=""
        pattern=s[0:i]
        count=1
        j=i
        #패턴 길이만큼씩 비교
        while j<len(s):
            if pattern==s[j:j+i]:
                count+=1
            else:
                compress=compress+(str(count) if count>1 else "")+pattern
                pattern=s[j:j+i]
                count=1
            j+=i
        
        #마지막 패턴 합치기
        compress=compress+(str(count) if count>1 else "")+pattern
        
        answer=min(answer,len(compress))

    return answer