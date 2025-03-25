from typing import List
def reorderLogFiles(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 두 개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])


'''
# 로그 파일의 데이터 재정렬
배열이 주어집니다 logs. 각 로그는 공백으로 구분된 단어 문자열이며, 첫 번째 단어는 식별자 입니다 .

통나무에는 두 가지 유형이 있습니다.

문자 로그 : 모든 단어(식별자 제외)는 소문자 영어 문자로 구성됩니다.
숫자 로그 : 모든 단어(식별자 제외)는 숫자로 구성됩니다.
이 로그를 다음과 같이 다시 정렬하세요.

문자 로그는 모든 숫자 로그 보다 앞에 옵니다 .
편지 로그는 내용에 따라 사전순으로 정렬됩니다. 내용이 같으면 식별자에 따라 사전순으로 정렬합니다.
숫자 기록은 상대적인 순서를 유지합니다.
로그의 최종 순서를 반환합니다 .
'''