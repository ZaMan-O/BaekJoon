sn = 1
while True:
    o,w = map(int,input().split())
    if o == 0:
        break
    tmp = w
    dead = False
    while True:
        s,num = input().split()
        num = int(num)
        if s == '#':
            if dead:
                print(sn, 'RIP')
            else:
                if o/2 < tmp < o*2:
                    print(sn, ':-)')
                else:
                    print(sn, ':-(')
            sn += 1
            break
        if s == 'E':
            if tmp - num <= 0:
                dead = True
            tmp -= num
        else:
            tmp += num