import math

for _ in range(int(input())):
    a,b = map(int,input().split())
    #print(a, b, abs(a-b), (a-b) / 10, math.ceil(abs( (a-b) / 10)))
    print(math.ceil(abs((a-b)/10)))