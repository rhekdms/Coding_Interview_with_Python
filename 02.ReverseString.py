def reverseString_me(s: list) -> None:
    print(list(reversed(s)))

reverseString_me(list(input()))

# 투포인터를 이용한 스왑 216밀리초
def reverseString_1(s: list) -> None:
        left, right = 0, len(s) - 1
        while left < right:         # 하나하나 바꾸는 방식
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# 파이썬 기본함수를 활용한 파이썬다운 방식 208밀리초
def reverseString_2(s: list) -> None:    # 내가 한 방식이랑 같음
    s.reverse()

'''
# 역순 문자열
문자열을 반전하는 함수를 작성한다.
입력 문자열은 문자 배열로 주어진다.
'''