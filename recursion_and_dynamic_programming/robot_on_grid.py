# 문제 해설
# 일단 문제의 분기점이 되는 어떤 셀의 위치부터 나눈다
# 셀의 위치가 없는 경우 / 셀이 있는 경우의 수를 구한다.
# 격자판에서 (r, c)로 가려면
# (r-1, c) 또는 (r, c-1)로 가서 각각 1칸 이동 하는 경우의 수를 생각 할 수 있다.
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
