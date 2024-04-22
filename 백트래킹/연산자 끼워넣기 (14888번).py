import sys
input = sys.stdin.readline

n = int(input())

num_list = list(map(str,input().rstrip().split()))
symbols_cnt = list(map(int,input().rstrip().split()))
symbols = {0:"+",1:"-",2:"*",3:'//'}
res = []
def backtracking(a,n):
    if sum(symbols_cnt) == 0:
        res.append(n)
        return

    for i in range(4):
        if symbols_cnt[i] > 0:
            symbols_cnt[i] -= 1
            if i == 3 and n < 0:
                backtracking(a + 1, eval(str(abs(n)) + symbols[i] + num_list[a + 1])*-1)
            else:
                backtracking(a+1,eval(str(n)+symbols[i]+num_list[a+1]))
            symbols_cnt[i] += 1

backtracking(0,int(num_list[0]))
print(max(res))
print(min(res))