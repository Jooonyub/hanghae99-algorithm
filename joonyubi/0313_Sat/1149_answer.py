import sys
input = sys.stdin.readline

n = int(input())
RGB = []
for i in range(n):
    RGB.append(list(map(int, input().strip().split())))

for i in range(1,n):
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]

    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1]

    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2]

print(min(RGB[n-1]))

'''
예제 입력 1 
3
26 40 83
49 60 57
13 89 99
예제 출력 1 
96
'''