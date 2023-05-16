
# 集合
# 半分全列挙

# 半分にするので2**nから{2**(n/2)}*2になるので計算量が少なくなる
# https://atcoder.jp/contests/arc017/tasks/arc017_3
from collections import defaultdict
n, x = list(map(int, input().split()))
# xは大きさの総和
a = []
b = []

for i in range(n):
    w = int(input())
    if i % 2 == 0:
        a.append(w)
    else:
        b.append(w)


def hasbit(t, i):
    return t & (1 << i) > 0


dic = defaultdict(int)
# print(len(a))#3
# print(len(b))#2
# グループB全列挙
allb = 1 << len(b)  # bの集合
for t in range(allb):  # 4回
    s = 0
    for i in range(n):  # 5回
        if hasbit(t, i):
            s += b[i]
    dic[s] += 1  # sは重さ、辞書型の位置に直接+1を加える
    # print(dic[s])
# 同じくグループA全列挙
ans = 0
alla = 1 << len(a)  # aの集合
for t in range(alla):  # 8回
    s = 0
    for i in range(n):  # 5回
        if hasbit(t, i):
            s += a[i]
    ans += dic[x-s]  # ここがグループBの時と違う
    # (許容量)-(aの総和パターンの個数)=(必要なbの総和のパターン)
    # よってその重さでのちょうどのパターンに加える量が決まる
print(ans)
