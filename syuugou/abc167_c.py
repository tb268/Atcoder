#集合の全探索
#https://atcoder.jp/contests/abc167/tasks/abc167_c
n,m,x=list(map(int,input().split()))
   

a=[]
c=[]
for i in range(n):
    lis=list(map(int,input().split()))
    c.append(lis[0])
    a.append(lis[1:])
#print(c)
#print(a)


alls=1<<n#全パターン

def cal(n,i):
    return n&(1<<i)>0

points=[]
for i in range(alls):
    points.append([0]*m)
    

cost=[0]*alls

for t in range(alls):
    for i in range(n):
        if cal(t,i):
            cost[t]+=c[i]
            for j in range(m):
                points[t][j]+=a[i][j]  

ans=10**100      

isOK=False
for i in range(alls):
    if ans<cost[i]:#暫定最小より小さければ外す
        continue
    if min(points[i])<x:#スキルが十分でなければ無視
        continue
    
    ans=cost[i]
    isOK=True

if isOK:
    print(ans)
else:
    print("-1")
    
    
    
    