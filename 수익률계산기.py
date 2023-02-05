a = float(input("지금 그 코인이 얼만데요? : "))#현재가격
b = float(input("당신의 평단가는? : "))#평단가
c = (a-b)/b*100
c = round(c, 2)
print(c,'%',sep='')