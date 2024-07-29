# 제출시 반드시 주석 처리

import sys

sys.stdin = open("input_text.py", "r")

# T=int(input())

T = 10

for tc in range(1, T+1):

    N = int(input())

    lst = list(map(int, input().split()))
    answer = 0

##########################
#풀이
##########################
print(f'#{tc} {answer}')