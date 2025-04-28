from typing import List

# 브루트포스 시간초과
def threeSum_me_1(nums: List[int]) -> List[List[int]]:
    sol = set([])
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if not (nums[i]+nums[j]+nums[k]):
                    sol.add(tuple(sorted([nums[i],nums[j],nums[k]])))
    return list(map(list,sol))

# 브루트포스 최적화 시간초과
def threeSum_me_2(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        if nums[i]>0:break
        if i>0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if nums[i]+nums[j]>0:break
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            if -(nums[i] + nums[j]) in nums[j+1:]:
                results.append([nums[i], nums[j], -(nums[i] + nums[j])])
    return results

# 투포인터 최적화 444ms
def threeSum_me_3(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()
    n = len(nums)

    for i in range(n - 2):
        # 탐색 종료 조건 (nums[i]가 양수면 이후로는 0을 만들 수 없음)
        if nums[i] > 0:
            break

        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 현재 값이 너무 크면 이후로도 가능성이 없으므로 종료
        if nums[i] + nums[i + 1] + nums[i + 2] > 0:
            break

        # 현재 값이 너무 작으면 스킵 (nums[i]가 너무 작아서 이후로도 가능성 없음)
        if nums[i] + nums[-1] + nums[-2] < 0:
            continue

        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                results.append([nums[i], nums[left], nums[right]])

                # 중복된 값 건너뛰기
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return results

# 브루트포스 최적화(나와 같음) 시간초과
def threeSum_1(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    # 브루트 포스 n^3 반복
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])

    return results

# 투포인터 884ms
def threeSum_2( nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁혀가며 합 `sum` 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # `sum = 0`인 경우이므로 정답 및 스킵 처리
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

        return results