from typing import List
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    s = sorted(count.keys(),key=lambda x:count[x],reverse=True)
    return s[:k]

print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))



'''

정수 배열 nums과 정수가 주어졌을 때 k, 가장 자주 나타나는 요소를 반환합니다 . k 결과 는 어떤 순서 로든 반환할 수 있습니다 .

예시 1:
입력: nums = [1,1,1,2,2,3], k = 2
 출력: [1,2]

예 2:
입력: nums = [1], k = 1
 출력: [1]

'''