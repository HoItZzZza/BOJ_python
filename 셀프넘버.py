#**1차시도** (실패)
#num이라는 변수에 0을 주고 반복문 만번 돌리고 1씩 늘리면서
#for문 3개 돌려서 num이 만들어지면 continue, num이 안만들어지면
#self_num리스트에 추가
#가보자고
#오케 이거 빠꾸먹었어 지피티가 논리 별로래
#아 문제를 어떻게 풀어야할까요 길을 알려주세요 아?
#list 일일이 만들어서 for문 돌리면 시간초과 걸릴 것 같은데요
#고뇌 시작한다 -----------
#**2차시도** (시간복잡도)
#li=[0]*0만들고 10000번 for문 돌리면서 
#숫자가 두 자리 수면 각 자리수 랜덤 조합으로  2개 빼고
#숫자가 세 자리 수면 각 자리수 랜덤 조합으로 3개 빼고...
#그렇게 하려고 했는ㄷ ㅔ 그러면 시간 복잡도 너무 올라가고
#근데 시간 제한만 없으면 맞았음!-! (어쨌든 굴러가면 됐지)
#셀프넘버가 아닌 수를 찿기보다 셀프넘버인 수를 찾는 방향으로 가야하는데...
#다시 고뇌 ---------------
#**3차시도**
#아이디어를 얻었다! 함수를 이용해보라는 말을 들었따!

def f(n):
    #(changing 변수로 True, False로 while문 돌렸는데
    #False로 바뀌니까 while이 False에서 멈춘 것 같다
    #일단 문제점 발견~)
    #(그래서 return num 밑에 changing = True해서 하면 다시
    #while문이 돌 줄 알았는데 아니었다
    #그냥 changing 안쓰고 다른 방법 찾아야 할 듯 !-!) --> n>0 이용해보자
    #여기에서 셀프넘버가 아닌 수(=num)를 찾고
    num = n
    while n>0:
        num+=n%10
        n//=10
        #if 1<=n<10: --> 이걸 삭제해야했다 필요없는 조건이었네
            #num+=n
    return num

#if num in li(1~10000까지 들어있는 리스트 만들고)
#li.remove(num) 해야지
li = [_ for _ in range(1,10001)]

for i in range(1, 10001):
    #isnt_that_selfnum = f(i)
    if f(i) in li:
        li.remove(f(i))


for j in li:
    print(j)