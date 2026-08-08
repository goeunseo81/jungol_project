#2진수_10진수
def tlanse(n):
    num=str(n)
    t=1
    sum=0
    for i in range(len(num)-1,-1,-1):
        if num[i]=="1":
            sum+=t
        t*=2
    return sum
print(tlanse(1001))
#10진수_2진수
def jalicsu(n):
    answer = 1
    while True:
        if answer > n:
            return answer//2
        elif answer == n:
            return answer
        answer *= 2

def transe(n,answer):
    result = ""
    while answer>0:
        if answer<=n:
            result+="1"
            n-=answer
        else:
            result+="0"
        answer //=2
    return result

n=int(input())
answer = jalicsu(n)
print(transe(n,answer))

