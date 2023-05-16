# ある始点から他の頂点への最短距離
# ダイクストラ法(距離が異なり、一方通行の場合)
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_d
import heapq as hq
n, m = list(map(int, input().split()))

edges = []
for i in range(n):
    edges.append([])
# uvc=[]
# 行き先
for i in range(m):
    u, v, c = list(map(int, input().split()))
    edges[u].append([v, c])

roots = [-1]*n  # そこへの最短距離
roots[0] = 0
done = [False]*n  # そこへの最短距離
q = []
hq.heappush(q, (0, 0))  # 最短時間、頂点位置の順

# print(edges)
while len(q) > 0:
    i, j = hq.heappop(q)
    if done[j]:
        continue
    done[j] = True
    for k in edges[j]:
        x = k[1]
        if roots[k[0]] == -1 or roots[k[0]] > roots[j]+x:
            roots[k[0]] = roots[j]+x
            hq.heappush(q, (roots[k[0]], k[0]))

print(roots[n-1])
