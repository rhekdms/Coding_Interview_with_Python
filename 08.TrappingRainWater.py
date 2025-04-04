from typing import List
def trap_me(height: List[int]) -> int:  # 51ms
    sol = 0
    ck = 0
    h1 = 0
    for i in height:
        if h1>i:
            ck+=(h1-i)
        else:
            sol+=ck
            ck = 0
            h1 = i
        print(sol,ck,h1)
    ck = 0
    h2 = 0
    for i in height[::-1]:
        if h2==h1:break
        if h2>i:
            ck+=(h2-i)
        else:
            sol+=ck
            ck = 0
            h2 = i
    return sol

print(trap_me([0,1,0,2,1,0,1,3,2,1,2,1]))

# two pointer 52ms 나와 같은 개념 적용
def trap_1(height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume
    
# 스택 56ms
def trap(height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        return volume