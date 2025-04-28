import collections
from typing import List
def groupAnagrams_me(strs:list)->list:
    sol = []            # 시간초과
    while strs:
        i = 0
        base = strs.pop()
        grp = [base]
        sorted_base = sorted(base)
        while i < len(strs):
            if sorted(strs[i]) == sorted_base:
                grp.append(strs.pop(i))
            else:
                i += 1
        sol.append(grp)
    return sol

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    word = {}           # 15ms
    for i in strs:
        temp = list(i)
        temp.sort()
        k = str(temp)
        if k not in word:
            word[k] = []
        word[k].append(i)
    return list(word.values())

print(groupAnagrams_me(strs = ["eat","tea","tan","ate","nat","bat"]))


def groupAnagrams_1(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    # defaultdict -> 기본 형태를 설정할 수 있는 딕셔너리
    # 이런 방법은 생각도 못했네... 7ms
    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

def groupAnagrams_ktr(strs: List[str]) -> List[List[str]]:
    l = dict()      # 17ms

    for elm in sorted(strs):
        item = f"{sorted(list(elm))}"
        if l.get(item):l[item].append(elm)
        else:l[item] = [elm]

    result = []
    for value in l.values():
        result.append(value)

    if result:return result
    else: return [[""]]

'''
# 그룹 아나그램
문자열 배열이 주어지면 똑같은 알파벳을 가진 문자열끼리 그룹화한다.
출력 순서는 상관없다.
'''
'''
< 정렬 알고리즘 별 시간 복잡도 >
퀵정렬      nlogn   nlogn   n^2
병합정렬    nlogn   nlogn   nlogn
팀소트      n       nlogn   nlogn   (실제 데이터는 이미 정렬되어 있을 것이다를 가정하고 최적화)
'''