#0308_02_10250.py
#title: ACM 호텔


'''
문제
ACM 호텔 매니저 지우는 손님이 도착하는 대로 빈 방을 배정하고 있다. 고객 설문조사에 따르면 손님들은 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호한다고 한다. 여러분은 지우를 도와 줄 프로그램을 작성하고자 한다. 즉 설문조사 결과 대로 호텔 정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램을 작성하고자 한다.

문제를 단순화하기 위해서 호텔은 직사각형 모양이라고 가정하자. 각 층에 W 개의 방이 있는 H 층 건물이라고 가정하자 (1 ≤ H, W ≤ 99). 그리고 엘리베이터는 가장 왼쪽에 있다고 가정하자(그림 1 참고). 이런 형태의 호텔을 H × W 형태 호텔이라고 부른다. 호텔 정문은 일층 엘리베이터 바로 앞에 있는데, 정문에서 엘리베이터까지의 거리는 무시한다. 또 모든 인접한 두 방 사이의 거리는 같은 거리(거리 1)라고 가정하고 호텔의 정면 쪽에만 방이 있다고 가정한다.



그림 1. H = 6 이고 W = 12 인 H × W 호텔을 간략하게 나타낸 그림

방 번호는 YXX 나 YYXX 형태인데 여기서 Y 나 YY 는 층 수를 나타내고 XX 는 엘리베이터에서부터 세었을 때의 번호를 나타낸다. 즉, 그림 1 에서 빗금으로 표시한 방은 305 호가 된다.

손님은 엘리베이터를 타고 이동하는 거리는 신경 쓰지 않는다. 다만 걷는 거리가 같을 때에는 아래층의 방을 더 선호한다. 예를 들면 102 호 방보다는 301 호 방을 더 선호하는데, 102 호는 거리 2 만큼 걸어야 하지만 301 호는 거리 1 만큼만 걸으면 되기 때문이다. 같은 이유로 102 호보다 2101 호를 더 선호한다.

여러분이 작성할 프로그램은 초기에 모든 방이 비어있다고 가정하에 이 정책에 따라 N 번째로 도착한 손님에게 배정될 방 번호를 계산하는 프로그램이다. 첫 번째 손님은 101 호, 두 번째 손님은 201 호 등과 같이 배정한다. 그림 1 의 경우를 예로 들면, H = 6이므로 10 번째 손님은 402 호에 배정해야 한다.

입력
프로그램은 표준 입력에서 입력 데이터를 받는다. 프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다. 각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다(1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W). 

출력
프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행을 출력하는데, 내용은 N 번째 손님에게 배정되어야 하는 방 번호를 출력한다.

예제 입력 1 
2
6 12 10
30 50 72
예제 출력 1 
402
1203
'''
'''
#오리지날 작성코드
T = int(input())   #T : number of test data. 테스트데이터 수
rooms_num = []
cases = list(len(T))
for i in range(T):
    H, W, N = input().split()
    H = int(H)      #H: 호텔의 층 수
    W = int(W)      #W: 각 층의 방 수
    N = int(N)      #N: N번째 손님
    
    Y = N%H
    X = N//H + 1
    room_num = Y*100+X
    rooms_num.append(room_num)
    #print(f"room_num:{room_num}")
    #N번째 손님은 N%H 층의 N//H + 1 호

    #def allocation(H, W, N):
        # N%H+1 의 연산으로 앞의 두자리 결정
        # N//H 의 연산으로 뒤의 두자리 결정

for room_num in rooms_num:
    #print(f"room_num:{rooms_num[i]}")
    print(room_num)
'''

'''
#초기 퓨어한 인풋만 받기 코드
T = int(input())   #T : number of test data. 테스트데이터 수
#cases = list(range(len(T)))
cases = [None] * len(range(T))
for i in range(T):
    H, W, N = input().split()
    H = int(H)      #H: 호텔의 층 수
    W = int(W)      #W: 각 층의 방 수
    N = int(N)      #N: N번째 손님
    cases[i] = [H, W, N]
    #print(cases[i])

#rooms.num = [None] * len(range(T))
for case in cases:
    H = case[0]
    W = case[1]
    N = case[2]
    
    Y = N%H
    X = N//H + 1
    #room_num = Y*100+X
    #print(f"{room_num}")
    
    #if Y < 10: Y = str(Y).zfill(1)
    #else: Y = str(Y).zfill(2)
    #X = str(X).zfill(2)
    
    #Y = '%d' % Y
    #X = '%2d' % X

    #Y = '{0:d}'.format(Y)
    #X = '{0:02d}'.format(X)
    
    room_num = Y*100+X
    .format()
    print(f" {먼저 선언해놨던 변수}") ->출력O
    

    print(room_num)
    #print("{0}{1:02d}".format(Y, X))
    #rooms_num.append(room_num)
'''   

'''
입력값
2
6 10 12

'''

 
#거품 싹 뺀 코드
T = int(input())
#rooms_num = []
for i in range(T):
    H, W, N = input().split()
    H = int(H)
    W = int(W)
    N = int(N)
    
    Y = N%H         #Y는 층에 관한 정보(몇층인지)
    if Y == 0:
        Y = H
        X = N//H
    else:
        X = N//H + 1    #X는 호수에 관한 정보(몇호인지)
    #room_num = Y*100+X
    #rooms_num.append(room_num)
    print("{0}{1:02d}".format(Y,X))

#for room_num in rooms_num:
    #print(room_num)
