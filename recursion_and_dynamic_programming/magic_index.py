# 마술 인덱스
# 배열 A = [0, ..., n-1] 에서 a[i] = i인 인덱스를 마술 인덱스(magin index)라고 정의한다.
# 정렬된 상태의 배열이 주어졌을 때, 마술 인덱스가 존재한다면 그 값을 찾는 메서드를 작성하라.
# 배열 안에 중복된 값은 없다.

# brute force
# O(n)
class Solution:
    def magic_index(n):
        magic_array = []
        ans = []

        for i in range(len(magic_array)):
            if magic_array[i] == i:
                ans.append(i)
                return ans
            else:
                continue

        return ans
