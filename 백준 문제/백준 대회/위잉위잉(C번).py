import sys
input = sys.stdin.readline

n = int(input())

human_list = [list(map(int,input().rstrip().split()))for _ in range(n)]
main_human = list(map(int,input().rstrip().split()))

