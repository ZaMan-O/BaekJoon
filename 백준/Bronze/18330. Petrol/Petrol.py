A=int(input())
B=int(input())
if A>B+60:
    print((B+60)*1500 + 3000*(A-B-60))
else:
    print(A*1500)