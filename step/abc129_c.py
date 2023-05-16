#ステップ
#https://atcoder.jp/contests/abc129/tasks/abc129_c
# coding: utf-8
# Your code here!
n,m=list(map(int,input().split()))

can=[True]*(n+1)
#broken=[]
for i in range(m):
    a=int(input())
    can[a]=False
        
step=[0]*(n+1)
step[0]=1
mod=((10**9)+7)
if can[1]:
    step[1]=1
for i in range(2,n+1):
    if can[i]:
        step[i]=step[i-1]+step[i-2]
    else:
        continue
    
#print(step[n])
ans=step[n]%mod
print(ans)