#すべての頂点の組についての最短距離
#ワーシャルフロイド法
#すべての頂点の組について調べるのはダイクストラ法よりはやい
#https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_e
import heapq as hq
inf=10**100
n,m = list(map(int,input().split()))

dist=[]#最短距離記録用
for i in range(n):
    dist.append([])
    for j in range(n):
        dist[i].append(inf)#すべてのルートにいくコストをinfとする（仮置き）
        
        

for i in range(m):
    u,v,c=list(map(int,input().split()))
    dist[u][v]=c#uからvにいくコストをcとする
    
for i in range(n):
    dist[i][i]=0#iからiの移動はありえないので0としておく
    
    
#ワーシャルフロイド法

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
            
#すべての頂点の組について最短距離を合計する
ans=0
for i in range(n):
    for j in range(n):
        ans+=dist[i][j]

print(ans)            
    
    