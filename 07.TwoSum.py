def twoSum( nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

print(twoSum(nums = [3,3], target = 6))

# 부루트포스 5284밀리초 (여길 제외한 나머지 풀이는 다 같은 개념을 바탕으로 함)
def twoSum_1(nums: list, target: int) -> list:  # 나랑 같은 방법
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
from typing import List
# in 사용 864 밀리초
def twoSum_2(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

# 키 조회 48 밀리초
def twoSum_3( nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

# 조회 구조 개선 44밀리초
def twoSum_4( nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 하나의 `for`문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

# 투포인터 (얜 리스트가 100% 정렬되어있어야 가능할텐데..) 풀이 불가
def twoSum_5(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]
        


'''
# 두 개의 합
정수 배열 nums 과 정수가 주어지면 target, 두 숫자 의 인덱스를 반환하여 두 숫자의 합이 .가 되도록 합니다target .
각 입력에 대한 해답은 정확히 하나만 있다고 가정할 수 있으며 , 같은 요소를 두 번 사용할 수 없습니다 .
어떤 순서로든 답변을 제출할 수 있습니다.
'''