
# 二分探索
# https://atcoder.jp/contests/arc050/tasks/arc050_b

R, B = list(map(int, input().split()))

x, y = list(map(int, input().split()))


def cal(t):  # 花束がt個ぴったりの時
    # どのパターンでも1つはマイナスされる
    r = R-t
    b = B-t
    if r < 0 or b < 0:
        return False
    # 上により一つづつマイナスしたので、残りの花取り方がが(x-1,0)(0,y-1)のパターンになる
    # 残りの花数を人組みの消費花数で組みで割ったものの数
    zan = r//(x-1)+b//(y-1)

    if zan >= t:
        return True
    else:
        return False


ng = 10**18+1
ok = 0

while abs(ok-ng) > 1:
    mid = (ng+ok)//2  # 中間点取得
    if cal(mid):
        ok = mid
    else:
        ng = mid

print(ok)
