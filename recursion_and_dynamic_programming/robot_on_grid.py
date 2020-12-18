# 문제 해설
# 중복을 없애고 목적지까지 가는 수를 계산한다면
# r-1, c / r, c-1 에서의 최댓값을 계산한 다음에 리턴해주면 된다.
# dp[i][j] == 0 인 경우, 금지 구역까지 가는 거리에 해당된다.
# 점화식
# dp[r][c] = dp[r][c-1] + dp[r-1][c]
# O(rc)

def find_a_route(n):
    route = 0
    dp = [[0 for _ in range(r+1)] for _ in range(c+1)]

    for i in range(0, n):
        for j in range(0, n):
            route = max(dp[i][j-1], dp[i-1][j])

            if dp[i][j] == 0:
                dp[i][j] == route

            else:
                dp[i][j] = route + 1

            return dp[c][r]
