1. 공통 과일 찾기
fruits = [   
    ["사과", "바나나", "포도"],   
    ["포도", "딸기", "사과"],   
    ["사과", "포도", "수박"]   
]


def solution(n):
    # 모든 사람이 가지고 있는 과일만 반환
    pass


print(solution(fruits))

목표: 모든 리스트에 공통으로 들어있는 과일 찾기

2. 한 번이라도 등장한 숫자
numbers = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]


def solution(n):
    # 전체 숫자를 중복 없이 반환
    pass


print(solution(numbers))

목표: 모든 리스트의 숫자를 합쳐서 중복 제거

3. 첫 번째 목록에만 있는 과목
subjects = [
    ["수학", "영어", "과학", "국어"],
    ["영어", "과학", "체육"]
]


def solution(n):
    # 첫 번째 목록에는 있지만 두 번째에는 없는 과목
    pass


print(solution(subjects))

목표: 차집합 사용

4. 두 반의 공통 학생
students = [
    ["민수", "철수", "영희", "지수"],
    ["영희", "지수", "준호", "민재"]
]


def solution(n):
    # 두 반에 모두 있는 학생
    pass


print(solution(students))

목표: 교집합 사용

5. 두 동아리 중 하나에만 가입한 학생
clubs = [
    ["민수", "철수", "영희"],
    ["영희", "지수", "준호"]
]


def solution(n):
    # 두 동아리 중 정확히 한 곳에만 가입한 학생
    pass


print(solution(clubs))

힌트: 대칭 차집합 ^를 생각해보기

6. 모든 시험에 출제된 단원
chapters = [
    ["1단원", "2단원", "3단원"],
    ["2단원", "3단원", "4단원"],
    ["2단원", "3단원", "5단원"]
]


def solution(n):
    # 모든 시험에 공통으로 등장한 단원
    pass


print(solution(chapters))

목표: set의 교집합을 반복해서 사용

7. 두 번 이상 등장한 메뉴
menus = [
    ["김밥", "라면", "떡볶이"],
    ["라면", "돈까스", "김밥"],
    ["김밥", "우동", "라면"]
]


def solution(n):
    # 2개 이상의 리스트에 등장하는 메뉴
    pass


print(solution(menus))

목표: set을 이용해서 중복 데이터를 찾아보기

8. 모든 사람이 좋아하지 않는 음식
foods = [
    ["치킨", "피자", "햄버거"],
    ["피자", "햄버거", "떡볶이"],
    ["햄버거", "떡볶이", "김밥"]
]


def solution(n):
    # 한 명이라도 좋아하지 않는 음식
    pass


print(solution(foods))

힌트: 전체 음식 집합을 구한 뒤 생각해보기

9. A에는 있고 B에는 없는 기술
skills = [
    ["Python", "Java", "SQL", "Git"],
    ["Java", "SQL", "HTML", "CSS"]
]


def solution(n):
    # A가 가지고 있지만 B는 가지고 있지 않은 기술
    pass


print(solution(skills))

목표: 차집합 -

10. 모든 팀에 존재하는 캐릭터
characters = [
    ["전사", "마법사", "궁수", "도적"],
    ["마법사", "궁수", "도적", "힐러"],
    ["궁수", "도적", "힐러", "전사"]
]


def solution(n):
    # 모든 팀에 공통으로 존재하는 직업
    pass


print(solution(characters))

모든 문제는 지피티에게 부탁하여 뽑았습니다. 코드는 파이썬 파일
