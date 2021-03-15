#0313_04_1149.py
#RGB거리(다이나믹 프로그래밍)


#N번째 집에 대해서 발생하는 최소비용
#N-1번째 집에 어느 색이 칠해져있는지 저장되어있으면 그 색에 대한 인덱스를 제외한 나머지 두 비용중 최소값 더하기

import sys
N = int(sys.stdin.readline())       #첫째줄 입력값 -> 집의 수 N

record = {}

#minimum_indices = []
def cost(N, record):
    #index_minimum = None
    rgb_list = list(map(int, sys.stdin.readline().split()))
    
    if N == 1:                                      #초기조건. record에 아무런 값도 없을 때
        minimum = min(rgb_list)                     #입력받은 세 값중에서 최소비용의 값 찾아 minimum에 저장
        index_minimum = rgb_list.index(minimum)     #index로 minimum값의 인덱스인지 찾기
        record[N] = index_minimum                   #key = N, value = index_minimum 설정
        return rgb_list[index_minimum]
    
    else:                                       #N이 1이 아닐떄, 즉 재귀조건 범위 내에 있을 때
        #del rgb_list(record[N-1])
        #if min_idx:
            #del rgb_list[min_idx[0]]
        temp_list = rgb_list                        #입력받은 rgb_list와 동일한 리스트 생성(temp_list)
        #del temp_list[record[N-1]]                  #temp_list에서 N-1번째 index에 대한 값 삭제 (연속으로 칠하는것을 방지하기 위함)
        del temp_list[record[N-1]]
        min(temp_list)                              #중복이 방지된 리스트인 temp_list에서 최소값 찾기
        index_minimum = rgb_list.index(min(temp_list)) #temp_list에서 찾은 최소값이 rgb_list에서 어느 인덱스인지 찾기
        record[N] = index_minimum
        '''
        if min_idx:
            min_idx = index_minimum
        '''
        #minimum_indices.append(index_minimum)3
    
        return cost(N-1, index_minimum) + min(temp_list)
        # return cost(N-1) + min(rgb_list), index_minimum

print(cost(N))


'''
N = 3
houses [{'r':26,'g':40,'b':83},{'r':49,'g':60,'b':57},{'r':13,'g':89,'b':99}] 

print(minimum_cost(houses))
'''

'''
문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

예제 입력 1 
3
26 40 83
49 60 57
13 89 99
예제 출력 1 
96
'''