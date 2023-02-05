a = float(input("얼마에 물리셨습니까? : "))
b = float(input("지금 그 코인이 얼만데요? : "))
c = (b/a-1)*100
c = round(c, 2)
print(c,'%',sep='')