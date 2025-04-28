from typing import List

def arrayPairSum_me(nums: List[int]) -> int:
    nums.sort()
    sol = 0
    for i in range(len(nums)-1,-1,-2):
        sol+=nums[i-1]
    return sol

print(arrayPairSum_me([6,2,6,5,1,2]))


'''
nums정수 배열이 주어지면 , 모든 정수 의 합이 최대가 되도록 정수 들을2n 쌍으로 묶습니다 n.
 최대화 된 합을 반환합니다 .(a1, b1), (a2, b2), ..., (an, bn)min(ai, bi)i
'''