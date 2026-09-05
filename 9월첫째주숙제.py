'''
import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    a,b =  map(int, input().split())
    print(a**b%10)
'''
import sys
import math
input = sys.stdin.readline #입력 속도 빠르게
T = int(input())

for i in range(T):
    a,b =  map(int, input().split())

    #a와 b의 제곱을 10으로 나눈 나머지를 구합니다
    #pow쪽이 a**b%10보다 빠릅니다
    result = pow(a, b, 10)

    #나머지가 0이면 10번 컴퓨터입니다
    if result == 0:
        print(10)

    else:
        print(result)