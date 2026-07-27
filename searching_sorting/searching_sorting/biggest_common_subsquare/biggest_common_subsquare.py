from bisect import bisect_right

n, m = map(int, raw_input().split())
A = [map(int, raw_input().split()) for _ in range(n)]

x, y = map(int, raw_input().split())
B = [map(int, raw_input().split()) for _ in range(x)]

BASE1 = 911
BASE2 = 3571

pow_col = [1] * (max(m, y) + 1)
for i in range(1, len(pow_col)):
    pow_col[i] = pow_col[i - 1] * BASE1

pow_row = [1] * (max(n, x) + 1)
for i in range(1, len(pow_row)):
    pow_row[i] = pow_row[i - 1] * BASE2


def get_hashes(mat, r, c, k):
    if k == 0:
        return set()

    row_hash = [[0] * (c - k + 1) for _ in range(r)]

    for i in range(r):
        h = 0
        for j in range(k):
            h = h * BASE1 + mat[i][j]
        row_hash[i][0] = h

        for j in range(1, c - k + 1):
            h = h - mat[i][j - 1] * pow_col[k - 1]
            h = h * BASE1 + mat[i][j + k - 1]
            row_hash[i][j] = h

    ans = set()

    for j in range(c - k + 1):
        h = 0
        for i in range(k):
            h = h * BASE2 + row_hash[i][j]
        ans.add(h)

        for i in range(1, r - k + 1):
            h = h - row_hash[i - 1][j] * pow_row[k - 1]
            h = h * BASE2 + row_hash[i + k - 1][j]
            ans.add(h)

    return ans


def check(k):
    return len(get_hashes(A, n, m, k) & get_hashes(B, x, y, k)) > 0


low = 0
high = min(n, m, x, y)

while low < high:
    mid = (low + high + 1) // 2
    if check(mid):
        low = mid
    else:
        high = mid - 1

print low
