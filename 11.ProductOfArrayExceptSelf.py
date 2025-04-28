from typing import List

# 부루트포스 시간초과
def productExceptSelf_me(nums: List[int]) -> List[int]:
    n = len(nums)
    sol = [1]*n
    for i in range(n):
        for j in range(n):
            if i!=j:sol[j]*=nums[i]
    
    return sol

print(productExceptSelf_me([-1,1,0,-3,3]))

# 17ms
def productExceptSelf(nums: List[int]) -> List[int]:
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out