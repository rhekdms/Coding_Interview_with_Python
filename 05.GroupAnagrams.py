def groupAnagrams_me(strs:list)->list:
    sol = []
    while strs:
        i = 0
        grp = [strs.pop()]
        while i<len(strs):
            if set(strs[i])==set(grp[0]):grp.append(strs.pop(i))
            else:i+=1
        sol.append(grp)
    return sol

print(groupAnagrams_me(strs = ["eat","tea","tan","ate","nat","bat"]))

import collections
from typing import List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    # defaultdict -> 기본 형태를 설정할 수 있는 딕셔너리
    # 이런 방법은 생각도 못했네...
    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

'''
# 그룹 아나그램
문자열 배열이 주어지면 똑같은 알파벳을 가진 문자열끼리 그룹화한다.
출력 순서는 상관없다.
'''