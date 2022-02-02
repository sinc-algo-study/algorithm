def is_palindrome(left, right, w):
    while left <= right:
        if w[left] != w[right]:
            return False
        left += 1
        right -= 1
    return True


def is_pseudo_palindrome(left, right, w):
    while left < right:
        if w[left] != w[right]:
            is_delete_left_palindrome = is_palindrome(left + 1, right, w)
            is_delete_right_palindrome = is_palindrome(left, right - 1, w)

            if is_delete_left_palindrome or is_delete_right_palindrome:
                return True
            else:
                return False
        else:
            left += 1
            right -= 1


def solution(word):
    if is_palindrome(0, len(word) - 1, word):
        return 0

    if is_pseudo_palindrome(0, len(word) - 1, word):
        return 1
    return 2


if __name__ == '__main__':
    T = int(input())
    words = [input() for _ in range(T)]
    for word in words:
        print(solution(word))
