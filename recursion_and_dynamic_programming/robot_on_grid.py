# 문제 해설
# 일단 문제의 분기점이 되는 어떤 셀의 위치부터 나눈다
# 셀의 위치가 없는 경우 / 셀이 있는 경우의 수를 구한다.
# 격자판에서 (r, c)로 가려면
# (r-1, c) 또는 (r, c-1)로 가서 각각 1칸 이동 하는 경우의 수를 생각 할 수 있다.
# 점화식
# dp[r][c] = dp[r][c-1] + dp[r-1][c]
# O(rc)

import sys

# mp == 중간 지점

r, c, mp = [int(x) for x in sys.stdin.readline().split()]


def find_a_route(y, x):

    dp = [[0 for k in range(x+1)] for k in range(y+1)]

    for i in range(1, y+1):
        for j in range(1, x+1):
            if i == 1 and j == 1:
                dp[i][j] = 1
                continue

            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[y][x]


# 중간 지점 없는 경우는 r, c 까지의 경우의 수 구하면 된다.
if mp == 0:
    print(find_a_route(r, c))

# 중간 지점 있는 경우 => 중간 지점의 인접한 좌표를 점화식으로 두고 (1, 1) 부터 중간지점의 dp들을 더하면 구하는 값이 나온다.
else:
    mpR1 = (mp - 1) // c + 1
    mpC1 = mp - (mpR1 - 1) * c
    mpR2 = r - (mpR1 - 1)
    mpC2 = c - (mpC1 - 1)

    # 오른쪽 아래 경로
    right_down = find_a_route(mpR1, mpC1)
    # 왼쪽 위 경로
    left_up = find_a_route(mpR2, mpC2)

    print(right_down + left_up)
