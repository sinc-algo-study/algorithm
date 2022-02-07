import sys
'''
summuus
^     ^
1. 맨 앞, 맨 뒤 문자 비교해서 같으면
    -> 앞+1, 뒤-1 문자 계속해서 비교
2. 비교해서 다르면
    1) 앞~뒤-1 까지의 문자열 만들어서 비교과정 반복
    2) 앞+1~뒤 까지의 문자열 만들어서 비교과정 반복
    -> 비교과정 성공 : 비교회문 / 실패 : 일반문자열

* isPalindrome 함수 설명
while문으로
- left : 0, right: length-1부터 시작
- 같은 문자인지 확인
- 같은 문자면 left+1, right-1 이동해서 다시 비교
while문 끝났는데
- left<right가 크면
    ex. summuus
          l r
- left~right까지 문자열 return (ex. mmu)
'''
def isPalindrome(word,left,right):
    while left<=right and word[left]==word[right]:
        left+=1;
        right-=1;

    if right-left>0:
        return word[left:right+1]

    return ''

def solution(words):
    answer = []
    for word in words:
        palindrome = 0
        word=isPalindrome(word,0,len(word)-1)

        if len(word)>0:
            palindrome=1
            #앞,뒤-1 문자열 확인
            word1=word[0:len(word)-1]
            word1=isPalindrome(word1,0,len(word1)-1)
            #앞+1,뒤 문자열 확인
            word2=word[1:len(word)]
            word2=isPalindrome(word2,0,len(word2)-1)

            if len(word1)>0 and len(word2)>0:
                palindrome=2
        answer.append(palindrome)
    return answer


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    words = []
    for _ in range(T):
        words.append(sys.stdin.readline().rstrip())
    answer = solution(words)
    for i in range(len(answer)):
        print(answer[i])
