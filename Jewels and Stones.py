from collections import Counter

def numJewelsInStones(jewels: str, stones: str) -> int:
    count = Counter(stones)
    sol = 0
    for i in jewels:
        sol+=count[i]
    return sol

print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))


'''

jewels보석 돌의 종류와 stones당신이 가지고 있는 돌의 종류를 나타내는 문자열이 주어집니다 . 
각 문자는 stones당신이 가지고 있는 돌의 종류를 나타냅니다. 당신이 가지고 있는 돌 중 보석인 돌이 몇 개나 있는지 알고 싶습니다.
대소문자를 구분하므로 .과는 "a"다른 종류의 돌로 간주됩니다 "A".

 

예시 1:
입력: 보석 = "aA", 돌 = "aAAbbbb"
 출력: 3

 예 2:
입력: 보석 = "z", 돌 = "ZZ"
 출력: 0

'''