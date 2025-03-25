from re import sub
def mostCommonWord_me(paragraph:str, banned:list)->str:
    paragraph = sub("[^a-z]"," ",paragraph.lower())
    cnt = {}
    for i in list(paragraph.split()):
        if i in cnt:cnt[i]+=1
        else: cnt[i]=1
    for i in banned:
        del cnt[i]
    
    return max(cnt.items(),key=lambda i: i[1])[0]
    
print(mostCommonWord_me(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))


import collections
import re
from typing import List
def mostCommonWord_1(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
                if word not in banned]

    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    return counts.most_common(1)[0][0]


'''
# 가장 흔한 단어
문자열 paragraph과 금지된 단어의 문자열 배열이 주어지면 banned, 금지되지 않은 가장 빈번한 단어를 반환합니다 .
금지되지 않은 단어가 적어도 하나 있고 답이 고유 하다는 것이 보장 됩니다 .
단어는 paragraph대소 문자를 구분하지 않으며 답변은 소문자 로 반환됩니다 .

'''