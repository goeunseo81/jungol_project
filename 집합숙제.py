#1
fruits = [
["사과", "바나나", "포도"],
["포도", "딸기", "사과"],
["사과", "포도", "수박"]
]
def solution(fruits):
    n= set(fruits[0])
    for i in range(1,len(fruits)):
        n &= set(fruits[i])
    return n

print(solution(fruits))

#2
numbers = [ [1, 2, 3], [3, 4, 5], [5, 6, 7] ]
def solution(n):
    result = set()
    for i in range(len(n)):
        result.update(n[i])
    return result


print(solution(numbers))

#3
subjects = [ ["수학", "영어", "과학", "국어"], ["영어", "과학", "체육"] ]
def solution(n):
    return set(n[0]) - set(n[1])

print(solution(subjects))

#4
students = [ ["민수", "철수", "영희", "지수"], ["영희", "지수", "준호", "민재"] ]
def solution(n):
    return set(n[0]) & set(n[1])

print(solution(students))

#5
clubs = [ ["민수", "철수", "영희"], ["영희", "지수", "준호"] ]
def solution(n):
    return set(n[0]) ^ set(n[1])

print(solution(clubs))

#6
chapters = [ ["1단원", "2단원", "3단원"], ["2단원", "3단원", "4단원"], ["2단원", "3단원", "5단원"] ]
def solution(n):
    m = set(n[0])
    for i in range(1,len(n)):
        m &= set(n[i])
    return m

print(solution(chapters))

#7
menus = [ ["김밥", "라면", "떡볶이"], ["라면", "돈까스", "김밥"], ["김밥", "우동", "라면"] ]
def solution(n):
    re = set()
    for i in range(len(n)):
        re.update(set(n[i - 1]) & set(n[i]))
    return re
print(solution(menus))

#8
food_list = ["치킨", "피자", "햄버거", "떡볶이", "김밥", "마라탕"]
foods = [ ["치킨", "피자", "햄버거"], ["피자", "햄버거", "떡볶이"], ["햄버거", "떡볶이", "김밥"] ]
def solution(n,n_list):
    re = set()
    for i in range(len(n)):
        re.update(set(n[i]))
    return set(n_list) - re

print(solution(foods, food_list))

#9
skills = [ ["Python", "Java", "SQL", "Git"], ["Java", "SQL", "HTML", "CSS"] ]
def solution(n):
    return set(n[0]) - set(n[1])

print(solution(skills))

#10
characters = [ ["전사", "마법사", "궁수", "도적"], ["마법사", "궁수", "도적", "힐러"], ["궁수", "도적", "힐러", "전사"] ]
def solution(n):
    re = set(n[0])
    for i in range(1,len(n)):
        re &= set(n[i])
    return re

print(solution(characters))