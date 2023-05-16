# coding: utf-8
#ダイクストラ法
#https://atcoder.jp/contests/abc068/tasks/arc079_a

import heapq
n,m=list(map(int,input().split()))


edges=[]
for i in range(n):
    edges.append([])
    
for i in range(m):
    a,b=list(map(int,input().split()))
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

kyori=[-1]*n
kyori[0]=0
q=[]

heapq.heappush(q,(0,0))#そこににかかる距離（暫定）、頂点の順
#
#
#ヒープは第一引数で最小値を取り出すので必ず距離を先にする。
#
#
#print(edges)
while len(q)>0:
    #print(q)
    #print("------------------")
    d,i=heapq.heappop(q)
    for j in edges[i]:
        x=1
        if kyori[j]==-1 or kyori[j]>kyori[i]+x:
            kyori[j]=kyori[i]+x
            heapq.heappush(q,(kyori[j],j))
        
#print(kyori)
if kyori[n-1]==2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
    
    