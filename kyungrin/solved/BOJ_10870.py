# 1. 피보나치의 n을 입력받는다.
# 1-1. 인덱스 기준으로 n을 수정한다.
n = int(input())

# 2. 재귀를 통해 피보나치의 수열을 구현한다.
# 2-1. 종료 조건 1: n이 0일 때 / 종료의 반환값: 0
# 2-2. 종료 조건 2: n이 1일 때 / 종료의 반환값: 1
# 2-3. F(n) = F(n-1) + F(n-2)
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

# 3. 결과를 반환한다.
print(fibo(n))