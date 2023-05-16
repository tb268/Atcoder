# 集合
# 巡回セールスマン問題
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_c


n = int(input())  # n=4

a = []

for i in range(n):
    a.append(list(map(int, input().split())))

alls = 1 << n  # いったことのある都市の集合パターン

inf = 10**100

cost = []
for i in range(alls):
    cost.append([inf]*n)
cost[0][0] = 0
# cost[i][j]#jがいったことのある都市の集合,iが行った都市数


def cal(x, y):  # すでに集合xがyに訪問済みかどうか
    return x & (1 << y) > 0


for i in range(alls):  # 集合
    for j in range(n):  # 今の場所
        for k in range(n):  # 次の場所
            if j == k or cal(i, k):  # 訪問済みまたは重複なら飛ばす
                continue
            # 以下超重要ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            # cost
            # [集合の和or→今までの訪問場所+kへ訪問した時の場所の集合]
            # [次の場所]
            # になる
            # ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            cost[i | (1 << k)][k] = min(
                cost[i | (1 << k)][k], cost[i][j]+a[j][k])


print(cost[alls-1][0])
