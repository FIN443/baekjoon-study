# 회문
T = int(input())


def check_symmetry(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False

    return True


def check_palindrome(word, left, right):
    while left < right:
        if word[left] != word[right]:
            # 왼쪽 제거
            check_left = check_symmetry(word, left + 1, right)
            # 오른쪽 제거
            check_right = check_symmetry(word, left, right - 1)
            if check_left or check_right:
                return 1
            else:
                return 2

        else:
            left += 1
            right -= 1

    return 0


for _ in range(T):
    word = input()
    result = check_palindrome(word, 0, len(word) - 1)
    print(result)
