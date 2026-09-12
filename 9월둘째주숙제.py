
from itertools import permutations
n_list = [0, 1, 2, 3, 4, 5]
r_list = list(permutations(n_list,4))

min_val = float('inf')
for i in r_list:
    s=0
    for j in range(4):
        s+=i[j]*(10**j)
    if s < min_val and s%6==0 and s>=1000:
        min_val = s
print(min_val)

from itertools import combinations
n_list = [10, 20, 33, 40, 55, 61, 78, 80, 91, 100]
r_list = list(combinations(n_list,3))
re = 0
for i in r_list:
    if sum(i)<=150 and 150-sum(i)<150-re:
        re = sum(i)

if re == 0:
    print("불가능")

else:
    print(re)