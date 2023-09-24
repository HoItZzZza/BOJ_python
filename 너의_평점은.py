gra = ["A+","A0","B+","B0","C+","C0","D+","D0","F"]
sco = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
zzin_sco = []
score = 0
hak = 0
sub_su = 20 #P때문에 과목 수 빠지면 갱신하랴고

for _ in range(20):
    a, b, c = map(str, input().split())
    zzin_sco.append([float(b),c])

for i in range(20):
    for j in range(9):
        if zzin_sco[i][1] == gra[j]:
            zzin_sco[i][1] = sco[j]
        elif zzin_sco[i][1] == "P": #P 나오면 sub_su 1씩 빼기
            zzin_sco[i][0] = 0 #여기가 문제였넹
            zzin_sco[i][1] = 0 #학점이랑 평점 고려해서 둘 다 P 빼는게 관건이었음 ^_^
            sub_su-=1

#print(zzin_sco)

for k in range(20):
    hak+=zzin_sco[k][0]
    score+=zzin_sco[k][0]*zzin_sco[k][1]

print(round(score/hak,6))
