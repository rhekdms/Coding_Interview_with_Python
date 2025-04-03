from re import sub
def Palindrome_me(P: str) -> bool:  # 자료형 선언
    P = P.lower()
    P = sub("[^a-z0-9]","",P)   # 정규식 사용
    for i in range(len(P)//2):          # 하나하나 비교
        if P[i]!=P[-i-1]:
            return False
    return True

# 리스트로 변환 304밀리초
def Palindrome_1(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():      # isalnum()-> 문자 혹은 숫자로 이루어진 문자열 True
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

# 데큐를 활용한 최적화 64밀리초
from collections import deque
from typing import Deque
def Palindrome_2(s: str) -> bool:
    # 자료형 데크로 선언
    # 어노테이션을 추가하는 부분(안써도 작동은 하지만 코드 보기가 어려울 수 있음)
    strs: Deque = deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

# 슬라이싱 이용 36밀리초
# 제일 내가 쓴 답과 유사함
def Palindrome_3(s: str) -> bool:
    s = s.lower()
    s = sub('[^a-z0-9]', '', s)

    return s == s[::-1]  # 슬라이싱



print(Palindrome_me(input()))

"""
# 유효한 팰린드롬 #
- 소문자 대문자를 구분하지 않으며, 숫자와 영어만 검사한다.
- 앞 뒤를 뒤집었을 때, 처음과 똑같으면 팬린드롬이기에 True를, 아닐 경우 False를 반환한다.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: s = "race a car"
Output: false

Example 3:
Input: s = " "
Output: true


// C로 풀이
bool isPalindrome(char *s) {
    int bias_left = 0;
    int bias_right = 1;

    int str_len = strlen(s);
    for (int i = 0; i < str_len; i++) {
        // 스킵 포인터 처리
        while (!isalnum(s[i + bias_left])) {
            bias_left++;
            if (i + bias_left == str_len)
                return true;
        }
        while (!isalnum(s[str_len - i - bias_right])) {
            bias_right++;
        }

        if (i + bias_left >= str_len - i - bias_right)
            break;
        // 팰린드롬 비교
        if (tolower(s[i + bias_left]) != tolower(s[str_len - i - bias_right]))
            return false;
    }
    return true;
}

"""